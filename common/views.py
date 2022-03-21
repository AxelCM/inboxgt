from django.shortcuts import render , HttpResponseRedirect , HttpResponse
from django.urls import reverse , reverse_lazy

from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin ,PermissionRequiredMixin
from django.contrib.auth import views as auth_views

#Models
from shipping.models import SendSale, Shipping

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self , *args , **kwargs):
        data = Shipping.objects.all()
        return {"data":data}

class BlankView(LoginRequiredMixin,TemplateView):
    template_name = 'common/blank.html'

    def get_context_data(self , *args , **kwargs):
        pass
