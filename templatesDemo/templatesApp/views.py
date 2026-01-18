from django.shortcuts import render

# Create your views here.

def renderTemplates(request):
    return render(request,'templatesApp/firstTemplate.html')

def render_data(request):
    myDict={"name":"Elango"}
    return render(request,'templatesApp/tempdata.html',context=myDict)

def render_Employee(request):
    myDict={"id":"007",
            "name":"Elango",
            "role":"Software developer",
            "salary":"18000"}
    return render(request,'templatesApp/employeedata.html',context=myDict)