from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Place
# Create your views here.
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid input")
            return redirect('login')

    return render(request,"login.html")

def demo(request):
   obj=Place.objects.all()
   return render(request,"index.html",{'result':obj})

def register(request):
   if request.method== 'POST':
      username=request.POST['username']
      first_name= request.POST['first_name']
      email = request.POST['email']
      passowrd = request.POST['password']
      password1 = request.POST['password1']
      if passowrd==password1:
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'EMAIL Taken')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,first_name=first_name,password=passowrd,email=email)
            user.save();
            return redirect('login')
            print("user created")
      else:
         messages.info(request,"Password noy matched")
         return redirect('register')
      return redirect('/')
   return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):

    return render(request,"about.html")

def home(request):
    return render(request,"index.html")