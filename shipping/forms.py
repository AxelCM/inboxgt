from django import forms

#from Models
from shipping.models import Shipping, SendSale

class ShipForm(forms.ModelForm):

    class Meta:

        model = Shipping
        fields = ('__all__')

class SendForm(forms.ModelForm):

    class Meta:

        model = SendSale
        fields = ('__all__')
