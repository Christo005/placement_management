from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import register
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings

def studentlogin(request):
    return render(request,"studentlogin.html")

def index(request):
    name = request.POST.get('name')

    email = request.POST.get('email')
    subject=request.POST.get('subject')  
    message=request.POST.get('message')
    if subject and message and email and name:
        try:
            send_mail(subject,message,email,['bhooshitpradeep9112@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid Header found.')
        return redirect(request,'index.html')
    else:
        return render('Make sure all fields are entered valid')
    
def adminlogin(request):
    return render(request,"adminlogin.html")
def pologin(request): 
    return render(request,"pologin.html")

def registration(request):
    if request.method=="POST":
        post=register()
        post.firstname=request.POST['firstname']
        post.lastname=request.POST['lastname']
        post.email=request.POST['email']
        post.password=request.POST['password']
        post.confirmpassword=request.POST['confirmpassword']
        post.save()
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')



