from django.urls import path
from .views import trigger_email

urlpatterns = [
    path('send-email/', trigger_email, name='send-email'),
]
