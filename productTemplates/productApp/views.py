from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict={
        'product1':'MacBook',
        'product2':'Iphone 16',
        'product3':'Samsung S25',
    }
    return render(request,'productApp/products.html',product_dict)

def toys(request):
    product_dict={
        'product1':'Remote Car',
        'product2':'Shinchan crawler',
        'product3':'Trucks',
    }
    return render(request,'productApp/products.html',product_dict)

def shoes(request):
    product_dict={
        'product1':'Nike',
        'product2':'Puma',
        'product3':'Reebok',
    }
    return render(request,'productApp/products.html',product_dict)

def index(request):
    return render(request ,'productApp/index.html')
