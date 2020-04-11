from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.loginV, name='loginV'),
    path('main/', views.home, name='home'),
    path('req/', views.req, name='req'),
    path('logout/', views.logoutV, name='logoutV')
    #path('register/', views.registration, name='registration'),


]