import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # Replace `myproject` with your actual project name

app = Celery("myproject") #app instance to register celery to our project

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY") #--------say celery to where the celery settings are there-----#
app.autodiscover_tasks() #----------automatically find the tasks file to process the task only the names tasks.py----#

@app.task(bind=True) #---if the task was failed that will wait for 5mins and try again-----""
def debug_task(self):
    print(f"Request: {self.request!r}") #------debug the error in the code show in the terminal---#
