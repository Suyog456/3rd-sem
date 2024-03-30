from django.shortcuts import render,redirect 
import requests 
import os
from a import settings 
#from .models import table names 
import random 
from datetime import date,timedelta
from django.http import JsonResponse , HttpResponse
import json 

def homepage(request):
    return render(request, "homepage.html")
def form_func(request):
    return render(request , "form.html")

        