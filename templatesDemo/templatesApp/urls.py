
from django.urls import path
from templatesApp.views import renderTemplates

urlpatterns = [
    path('temp/',renderTemplates),
]
