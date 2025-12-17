from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
app = Celery('tasks', broker='redis://localhost:6379/0' ,backend='redis://localhost:6379/0')
app.conf.update(
    task_default_queue='default',
    task_create_missing_queues=True,
    worker_pool='solo',  
)
 
 
@app.task
def send_email(subject, body, to_email):
    from_email = 'kala.ammu1979@gmail.com'  
    password = 'ifpd pndw qwxm uekh'
 
   
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
 
   
    message.attach(MIMEText(body, 'plain'))
    print("Sending email...")
 
   
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  
            server.login(from_email, password)
            text = message.as_string()
            server.sendmail(from_email, to_email, text)
            return 'Email sent successfully!'
    except Exception as e:
        return f'Failed to send email: {e}'