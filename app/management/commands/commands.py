from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import Shops, Budgets

class Command(BaseCommand):
    help = 'Displays current time'

    def date_today(self, *args, **kwargs):
        time = timezone.now().strftime('%Y-%m-%d')
        self.stdout.write(f"Hello! The date today is {time}.")

    def current_month(self, *args, **kwargs):
        q0 = Budgets.objects.all().order_by('-a_id').values('a_month')[:1]
        q1 = q0[0]
        q2 = q1['a_month']
        print(f"I will be working on the 'stylight' dataset provided to me through e-mail.\nAccording to the dataset provided month {q2.month} of year {q2.year} has the latest entries. We will be working on this and avoid older entries!")
        q3= Budgets.objects.filter(a_month=str(q2))
        print(f'Total number of brands that have signed up for advertisement on our platform for this month are {q3.count()}.')
        q4 =q3.filter(a_shop_id__a_online=1)
        print(f'Out of these {q3.count()} shops currently {q4.count()} are active.')
        print(f"Now lets inspect these {q4.count()} active brands and notify them if they have reached above 50% or 100% of budget!")
        q5 = q4
        print(q5)


    def briefing(self, *args, **kwargs):
        pass

    def populate_percentage(self, *args, **kwargs):
        pass

    def notification_at_half(self, *args, **kwargs):
        pass

    def budget_exhaust(self, *args, **kwargs):
        pass

    def handle(self, *args, **kwargs):
        print('--end--')

i = Command() 
i.date_today() 
i.current_month()
# py manage.py loaddata ./app/fixtures/db.json
# py manage.py dumpdata > ./app/fixtures/db.json