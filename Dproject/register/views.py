from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid user")
            return redirect('login')

    return render(request,"login.html")
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        special_characters="!@# $%^&*()-+?=,<>.;:/"
        my_string=username[0]
        if my_string.isdigit()==True:
            messages.info(request,'The username does not start with numbers')
            return redirect('signup')
        else:
            pass
        if any(c in special_characters for c in username):
            messages.info(request, 'Username does not allow special characters except " _ "')
            return redirect('signup')
        else:
            pass
        if len(password) < 6:
            messages.info(request, 'password must 6 letters or above')
            return redirect('signup')
        else:
            pass
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Is Already Taken!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already Taken')
                    return redirect('signup')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('signup')
        return redirect('/')


    return render(request,"signup.html")