from django.urls import path

from shipping.views import CreateShip ,new_sendsale

urlpatterns= [
    path('ingresar/' , CreateShip.as_view() , name='ingresar'),
    path('new/' , new_sendsale , name='new')
]
