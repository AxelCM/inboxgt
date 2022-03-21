from django.shortcuts import render
from django.views.generic import TemplateView , CreateView, UpdateView
from django.urls import reverse, reverse_lazy

#use this imports by show in the form Groups
from django.contrib.auth.models import Group , Permission

#Validation imports
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from ordenes.views import NotPermissionsRule
from django.contrib.auth.hashers import make_password
from django.views.generic import TemplateView

#imports from models
from users.models import User, Sucursal

from users.forms import SignUpForm , UpdateUserForm

#date and time library
from datetime import *

#from django rest framework
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from users.serializers import UserSerializer

class SignUp(NotPermissionsRule, SuccessMessageMixin, CreateView):
    permission_required = 'ordenes.managaer_full_view'
    template_name = 'users/forms/signup.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    form_class = SignUpForm
    success_message = "Usuario creado satisfactoriamente!"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        now = datetime.now()
        self.object.date_joined = now
        password_plain = self.object.password
        password_hash = make_password(password_plain)
        self.object.password = password_hash
        self.object.save()
        return super(SignUp ,self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(SignUp , self).get_context_data(**kwargs)
        context['sucursals'] = Sucursal.objects.all()
        context['groups'] = Group.objects.all()
        context['now'] = datetime.now()
        return context

    def get_success_url(self):
        return reverse('home')

class UpdateUserView(NotPermissionsRule , SuccessMessageMixin, UpdateView):
    permission_required = "ordenes.managaer_full_view"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'users/update/update_user_form.html'
    model = User
    fields = ['sucursal' , 'first_name' , 'last_name' , 'email' , 'groups']
    success_message = 'Usuario Actualizado!'
    error_message = "Algo salio mal, no se ejecuto correctamente"
    success_url = reverse_lazy('user_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_service = self.get_object()
        context['sucursals'] = Sucursal.objects.all()
        context['groups'] = Group.objects.all()
        return context

class UserList(NotPermissionsRule , TemplateView):
    permission_required = "ordenes.managaer_full_view"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'users/user_list.html'

    def get_context_data(self , *args, **kargs):
        sucursals = Sucursal.objects.all()
        users = User.objects.filter(is_superuser=False)
        return {'sucursals': sucursals , 'users': users}
