#use of strftime
from datetime import datetime
name=input("enter your name")
now=datetime.now()
formatted=now.strftime("%y-%m-%d %H:%M:%S")
hours=int (now.strftime("%H"))
if hours <10:
    print("Good morning ", name)
elif hours <15:
    print("good afternoon",name)
elif hours <21:
    print ("good evening" , name)
else:
    print("good night",name) 
