from django.db import models
from django.utils.translation import gettext_lazy as _

class Trxn(models.Model):
    
    class AccountChoices(models.TextChoices):
        CreditCard = 'CC', _('Credit Card')
        Chequing = 'CQ', _('Chequing')
    
    class CategoryChoices(models.TextChoices):
        Rent = 'RT', _('Rent')
        Groceries = 'GC', _('Groceries')

    Date = models.DateField(auto_now=False,auto_now_add=False)
    Amount = models.DecimalField(max_digits=10,decimal_places=2)
    Account = models.CharField(
        max_length=2,
        choices=AccountChoices.choices,
        default=AccountChoices.CreditCard,
        )

    Category = models.CharField(
        max_length=2,
        choices=CategoryChoices.choices,
        default=None,
    )

    Notes = models.CharField(
        max_length=240,
        null=True
    )