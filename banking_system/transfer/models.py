import re
from statistics import mode
from django.db import models
from django.dispatch import receiver

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    current_balance = models.FloatField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Transfer(models.Model):
    sender = models.ForeignKey(Customer, null=True, related_name='sender', on_delete=models.SET_NULL)
    receiver = models.ForeignKey(Customer, null=True, related_name='receiver', on_delete=models.SET_NULL)