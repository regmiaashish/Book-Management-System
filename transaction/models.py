from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    class Transactionstatus(models.IntegerChoices):
        COMPLETED = 1 ,'COMPLETED'
        FAILURE = 2 , 'FAILURE'
        INITIATED = 3, 'INITIATED'
        PENDING = 4, 'PENDING'
    
    class PaymentMethod(models.IntegerChoices):
        ESEWA = 1 ,'ESEWA'
        KHALTI = 2 , 'KHALTI'
        ADMIN = 3, 'ADMIN'

    name = models.CharField(max_length=50, null=True, blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2 )
    transaction_id = models.UUIDField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_email = models.CharField(max_length=40, null=True , blank=True) # optional field
    status = models.IntegerField(choices=Transactionstatus.choices, default=Transactionstatus.PENDING)
    _from = models.CharField(max_length=100, null=True, blank=True)
    to = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.IntegerField(choices=PaymentMethod.choices)
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name