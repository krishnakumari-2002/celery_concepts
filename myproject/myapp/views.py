import json
from django.http import JsonResponse
from myapp.tasks import send_email_task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt #If you disable CSRF protection, Django will not check if the request comes from a trusted source.
def send_email_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            subject = data.get("subject")
            message = data.get("message")
            recipients = data.get("recipients")
          

            if not subject or not message or not recipients:
                return JsonResponse({"error": "Missing required fields"}, status=400)
                
            if isinstance(recipients,str): #if it was a single mail convert that into the list 
                recipients = [recipients]
                
            data=send_email_task.delay(recipients,subject,message) #delay process the task background in asynchronously

            return JsonResponse({"message": "Email task sent to Celery"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
