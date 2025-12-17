from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .tasks import send_bulk_email

def trigger_email(request):
    """
    API endpoint to trigger bulk email sending.
    """
    subject = "Test Email from Django & Celery"
    message = "This is a test email sent using Celery and Redis."
    recipient_list = ["kk5749664@gmail.com"]

    # Call the Celery task
    send_bulk_email.delay(subject, message, recipient_list)

    return JsonResponse({"message": "Emails are being sent!"})
