from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import Shops, Budgets

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%Y-%m-%d')
        date = self.stdout.write(f"Hello! The date today is {time}.")
        q0 = Budgets.objects.all().order_by('-a_id').values('a_month')[:1]
        q1 = q0[0]
        q2 = q1['a_month']
        print(f"\nI will be working on the 'stylight' dataset provided to me through e-mail.\nAccording to the dataset provided latest entries are from {q2.month}-{q2.year}. So I will be working on this month and avoid previous month entries!")
        q3= Budgets.objects.filter(a_month=str(q2))
        print(f'\nTotal number of brands that have signed up for advertisement on our platform for {q2.month}-{q2.year} are {q3.count()}.')
        q4 =q3.filter(a_shop_id__a_online=1)
        print(f'Out of these {q3.count()} shops currently {q4.count()} are active.')
        print(f"Now lets inspect these {q4.count()} active shops and notify them if they have reached above 50% or 100% of budget!\n")
        for a in q4.iterator():
            consumtion_percentage = round((a.a_amount_spent / a.a_budget_amount) * 100,0)
            if consumtion_percentage > 50 and consumtion_percentage < 100 and a.a_notify_at_half != True:
                print(f"message to client=> Hi, its {time} today. Your shop named {a.a_shop_id.a_name} having id {a.a_shop_id.a_name} has utilized {consumtion_percentage}% of budget allocated for this month. Your budget was set to {a.a_budget_amount} for this month and you have currently used {a.a_amount_spent}. You will be notified again once the budget is exhaused.")
                i = Budgets.objects.get(a_id=a.a_id)
                i.a_notify_at_half = True
                i.save()
            elif consumtion_percentage >= 100 and a.a_shop_id.a_online == True:
                print(f"Hi, its {time} today. Your shop named {a.a_shop_id.a_name} having id {a.a_shop_id.a_name} has utilized {consumtion_percentage}% of its allocated budget of this month. Your budget was set to {a.a_budget_amount} for this month and you have currently used {a.a_amount_spent}. Your shop is currently offline.")
                i = Shops.objects.get(a_id=a.a_shop_id.a_id)
                i.a_online = False
                i.save()
            elif consumtion_percentage < 50 and a.a_shop_id.a_online == True and a.a_notify_at_half is None:
                print(f"Shop {a.a_shop_id.a_name} has not used more than 50% of its budget and need not to be notified yet." )
        # print(f"\nTo avoid duplication of messages sent when budget consumption is greater than 50% we have created an additional coloum in our 't_budgets' table named 'a_notify_at_half'.\nWe will mark 'True' this colum row once the shop is sent notification message. The coloum accepts boolian field and default set to 'Null'.")
# py manage.py loaddata ./app/fixtures/db.json
# py manage.py dumpdata > ./app/fixtures/db.json