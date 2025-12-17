from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_bulk_email(subject, message, recipient_list):
    """
    Send emails to multiple users asynchronously using Celery.
    """
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email="kala.ammu1979@gmail.com",
            recipient_list=recipient_list,
            fail_silently=False,
        )
        return f"Emails sent to: {', '.join(recipient_list)}"
    except Exception as e:
        return str(e)
