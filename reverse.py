from celery import Celery
from time import sleep


app = Celery('reverse', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
@app.task
def reversed(text):
    sleep(2)  
    return text[::-1] 

if __name__ == "__main__":
    result = reversed.delay("hello")  
    print("Task result:", result.get()) 
