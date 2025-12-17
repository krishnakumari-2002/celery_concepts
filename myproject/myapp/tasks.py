from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(to_email,subject,body):
    if not subject or not body or not to_email:
        raise ValueError("Missing required parameters: subject, message, or recipients")
    
    if isinstance(to_email, str): #check that it will be the list of email if not convert that
        to_email = [to_email] 
    
    send_mail(
        subject,
        body,
        'kala.ammu1979@gmail.com',  #send the mail must match with the settings configuration
        to_email,
        fail_silently=False, #if fails error while sending raise the error
    )
    return "Email Sent!"
