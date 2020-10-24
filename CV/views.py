from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def submit(request):
    if request.method=="POST":
         #print("hello from is submitted")
        name=request.POST["name"]
        email=request.POST["Email"]
        subject=request.POST["Subject"]
        message=request.POST["message"]

        #Resume_info = Resume(fname=fname,lname=lname,email=email,subject=subject,message=message)
        #Resume_info.save()
        #send an email
        send_mail(
            subject+' - '+email, #subject
            name+' - '+message, #message
            'Profile <mohitedinesh363@gmail.com>', #from email
            ['richadhane1998@gmail.com'],#to email
         )
        return render(request,'index.html', {'name': name})
    else:
        return render(request,'index.html')