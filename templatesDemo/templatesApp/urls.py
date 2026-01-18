
from django.urls import path
from templatesApp.views import renderTemplates,render_data,render_Employee

urlpatterns = [
    path('temp/',renderTemplates),
    path('tempdata/',render_data),
    path('empdata/',render_Employee),
]
