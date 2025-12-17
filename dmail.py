from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')


app.conf.update(
    task_default_queue='default',
    task_create_missing_queues=True,
    broker_connection_retry_on_startup = True,
    result_backend='redis://127.0.0.1:6379/0',
    worker_pool="eventlet",   
    worker_concurrency=4,    
    worker_autoscale=(10, 3) 
)

@app.task
def send_email(subject, body, to_emails):
    from_email = 'kala.ammu1979@gmail.com'  
    password = 'mexy obdb gbqx lpil' 

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
