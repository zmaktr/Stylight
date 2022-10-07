import imp
from django.db import models

class Shops(models.Model):
    a_id                = models.AutoField(primary_key=True)
    a_name              = models.CharField(max_length=255)
    a_online            = models.BooleanField() # models.IntegerField()

    class Meta:
        managed         = False
        db_table        = 't_shops'

class Budgets(models.Model):
    a_id                = models.AutoField(primary_key=True)
    a_shop_id           = models.ForeignKey(Shops, on_delete=models.CASCADE) 
    a_month             = models.DateField()
    a_budget_amount     = models.DecimalField(max_digits=10, decimal_places=2)
    a_amount_spent      = models.DecimalField(max_digits=10, decimal_places=2)
    a_notify_at_half    = models.BooleanField(null=True, blank=True)

    # def get_a_percentage_spent(self):
    #     return ( self.a_amount_spent * self.a_budget_amount ) * 100
    class Meta:
        managed         = False
        db_table        = 't_budgets'
        unique_together = (('a_shop_id', 'a_month'),)

