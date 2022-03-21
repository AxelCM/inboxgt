#Django
from django.urls import path

#Views
from common.views import IndexView, BlankView

urlpatterns= [
    path('', IndexView.as_view(), name='index'),
    path('blank/', BlankView.as_view(), name='blank')
]
