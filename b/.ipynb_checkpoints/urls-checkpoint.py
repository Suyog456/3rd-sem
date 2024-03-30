from django.contrib import admin 
from django.urls import path , include 
from . import views
from django.conf import settings



urlpatterns = [
    path("Homepage" , views.homepage , name = "homepage"),
    path("form" , views.form_func , name = "form"),
]