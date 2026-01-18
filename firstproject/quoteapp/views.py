from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def quote(request):
    return HttpResponse("Time is gold")

def renderTemplates(request):
    return render(request,'quoteapp/quote.html')
