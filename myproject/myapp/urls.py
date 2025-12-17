from django.urls import path
from .views import send_email_view

urlpatterns = [
    path('send-email/', send_email_view  , name='send_email'),
]

#api usrl for my app