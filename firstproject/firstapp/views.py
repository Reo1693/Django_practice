from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def Home(request):
    return HttpResponse("My first django application")

def date_and_time(reuest):
    dt=datetime.datetime.now()
    s="<b>Current Date and Time: </b>"+str(dt)
    return HttpResponse(s)
    
