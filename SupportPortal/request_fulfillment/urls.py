from . import views
from django.urls import path

urlpatterns = [

    path('resource/', views.resource, name='resource'),
    path('access/', views.access_ar, name='access_ar'),
    path('install/', views.installV, name='installV'),
    path('activity/', views.activityV, name='activityV'),
    path('testing/', views.testV, name='testV'),
]