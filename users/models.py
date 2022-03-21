#Django
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

#Django Crum
from crum import get_current_user

#DateTimeNative
from datetime import datetime

#imports from my models

from common.models import DataControl



class Sucursal(DataControl):
    name = models.CharField('Nombre' , max_length=30)
    address=  models.CharField('Direccion' , max_length=150)
    phone = models.CharField('Telefono' , max_length=8)
    phone_extra = models.CharField('Telefono Extra' , max_length=8 , blank=True, null=True)
    logo = models.ImageField(
    upload_to = 'user/sucursal/images',
    blank= True,
    null = True
    )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(TypeSize, self).save()

class User(AbstractUser):
    is_customer = models.BooleanField('Cliente' , default=False)
    sucursal = models.ForeignKey(Sucursal, blank=True, null=True, on_delete=models.CASCADE)
