#Django
from django import forms

#Models
from usuario.models import User, Sucursal

#Datetime native Python
from datetime import *

class SignUpForm(forms.ModelForm):
    """For signup new users"""
    class Meta:
        model = User
        fields = '__all__'
    def clean_date_joined(self):
        """Add Date now"""
        date_joined = self.cleaned_data['date_joined']
        now = datetime.now()
        date_joined = now
        return date_joined


class UpdateUserForm(forms.ModelForm):
    """Update data for user registred"""
    class Meta:
        model = User
        fields = ('sucursal' , 'first_name' , 'last_name' , 'email' , 'groups' )


class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = '__all__'


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = Sucursal
        fields = ('__all__' )
