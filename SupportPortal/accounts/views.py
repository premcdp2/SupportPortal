from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from request_fulfillment.models import New_services

def index(request):
    context={}
    return render(request, 'accounts/index.html', context)

def home(request):
    context={}
    return render(request, 'accounts/main.html', context)

@login_required(login_url="loginV")
def req(request):
    form=New_services.objects.all()
    context={'form':form}
    return render(request, 'accounts/req.html', context)

def loginV(request):
    if request.POST:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            return redirect('index')

    else:
        form=login1()
    context={"form": form}
    return render(request,'registration/login.html', context)

def logoutV(request):
    if request.POST:
        logout(request)
        return redirect('loginV')