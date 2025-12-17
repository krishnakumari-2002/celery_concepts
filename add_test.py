from dmail import add
 
result = add.delay(4, 6)  
print(result.get())  
 