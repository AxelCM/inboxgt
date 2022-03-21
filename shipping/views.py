from django.shortcuts import render
from django.views.generic import TemplateView , CreateView , DetailView
from django.contrib.auth import views as auth_views
from django.urls import reverse , reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse

from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from shipping.forms import ShipForm, SendForm
# Create your views here.

#fuction for can use ModelUser property Django FrameWork
from django.contrib.auth import get_user_model , logout, login

User = get_user_model()

def new_sendsale(user, text, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "gossip", {"type": "user_gossip",
                   "event": "new_created",
                   "user": user,
                   "text": text})


class CreateShip(CreateView):
    success_url = reverse_lazy('blank')
    success_message = 'GRACIAS POR REPORTAR EL INDICENTE, EL CUERPO DE BOMBEROS ESTA ENTERADO DE TU AVISO. ES POSIBLE QUE LA ESTACION SE COMUNIQUE CONTIGO PARA CONFIRMAR DATOS'
    template_name = 'shipping/create_ship.html'
    form_class = ShipForm
    # form_class = SendForm

    """ Validación y agregación de datos"""
    def form_valid(self, form):
        self.object = form.save(commit=False)
        me = self.request.user.pk
        user = User.objects.get(pk=me)
        full_name = "{} {}".format(user.first_name, user.last_name)
        # sucursal = Sucursal.objects.get(pk=user.sucursal.pk)
        """replace user form by user logged"""
        self.object.user = user
        self.object.save()
        new_sendsale(full_name, self.object.text)
        return super(CreateShip, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    #     """Retorno de vista luego del guardado"""
    # def get_success_url(self):
    #     return reverse('blank' , kwargs={'pk':self.object.id_service})
    #
    # def get_form_kwargs(self , *args , **kwargs):
    #     kwargs = super(CreateService, self).get_form_kwargs(*args , **kwargs)
    #     return kwargs
