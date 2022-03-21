from django.db import models

#Models
from common.models import DataControl

from users.models import User

class Shipping(DataControl):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField('Texto' , max_length=100)

class SendSale(models.Model):
    text=models.CharField('texto', max_length=100)
