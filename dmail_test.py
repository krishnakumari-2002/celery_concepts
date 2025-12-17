from dmail import send_email


recipients = [
    "kk5749664@gmail.com",
    "krishnakuamri.g@medyaan.com",
    "gkrishnakumari269@gmail.com",
    "950620cs36@einsteincollege.ac.in"
]


result = send_email.delay("Happy to sent you", "This is a celery email", recipients)
print("Task ID:", result.id)
