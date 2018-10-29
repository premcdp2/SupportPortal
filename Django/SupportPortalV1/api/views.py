from django.shortcuts import render
from .models import Activity
from api.serializers import ActivitySerializers
from rest_framework import viewsets

# serializing Linux activities.
class Activity_view(viewsets.ModelViewSet):
    queryset=Activity.objects.all()
    serializer_class = ActivitySerializers

