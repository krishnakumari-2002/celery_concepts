from dmail import send_email
 
 
result = send_email.delay('Test Subject', 'This is a test email body', 'kk5749664@gmail.com')
 
try:
    print(result.get())  
except Exception as e:
    print(f"Error occurred: {e}")
 