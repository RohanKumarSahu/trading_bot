from django.urls import path, include
from .views import webhooks


urlpatterns = [
    path('webhook/', webhooks , name = 'webhook' ),   
]