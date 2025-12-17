from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Celery('mail', broker='redis://localhost:6379/0')

app.conf.update(
    task_default_queue='default',
    task_create_missing_queues=True,
    worker_pool='solo',
    result_backend='redis://localhost:6379/0'  
)

@app.task
def send_email(subject, body, to_emails):
    from_email = 'kala.ammu1979@gmail.com'  
    password = 'ifpd pndw qwxm uekh'  

    results = {}  
    for to_email in to_emails:
        try:
            
            message = MIMEMultipart()
            message['From'] = from_email
            message['To'] = ", ".join(to_emails)  
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()  
                server.login(from_email, password)
                server.sendmail(from_email, to_email, message.as_string())

            results[to_email] = 'Email sent successfully!'
        except Exception as e:
            results[to_email] = f'Failed to send email: {e}'

    return results  