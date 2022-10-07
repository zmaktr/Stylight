import imp
from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Shops(models.Model):
    a_id                = models.AutoField(primary_key=True)
    a_name              = models.CharField(max_length=255)
    a_online            = models.BooleanField() # models.IntegerField()

    class Meta:
        managed         = False
        db_table        = 't_shops'

class Budgets(models.Model):
    a_shop_id           = models.ForeignKey('Shops', db_colum='a_id', on_delete=models.CASCADE) # models.IntegerField(primary_key=True)
    a_month             = models.DateField()
    a_budget_amount     = models.DecimalField(max_digits=10, decimal_places=2)
    a_amount_spent      = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed         = False
        db_table        = 't_budgets'
        unique_together = (('a_shop_id', 'a_month'),)

