from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from accounts.forms import activity_new


def resource(request):
    context = {}
    return render(request, "windows/resource.html", context)

def access_ar(request):
    context = {}
    return render(request, "windows/access_ar.html", context)

def installV(request):
    context = {}
    return render(request, "windows/install.html", context)

def testV(request):
    form = New_services.objects.all()
    context = {"form": form}
    return render(request, "windows/test.html", context)

def activityV(request):
    if request.POST:
        new_row=New_services(service_name=request.POST['activity_name'])
        new_row.save()
        return redirect('req')
    form=activity_new()
    context = {"form":form}
    return render(request, "windows/activity.html", context)