from django.urls import path, include
from .views import webhooks, home


urlpatterns = [
    path('',home , name='home')
    path('webhook/', webhooks , name = 'webhook' ),   
]