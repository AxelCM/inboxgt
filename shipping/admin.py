from django.contrib import admin

# Register your models here.
from shipping.models import Shipping, SendSale

admin.site.register(Shipping)
admin.site.register(SendSale)
