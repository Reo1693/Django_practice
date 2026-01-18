from django.urls import path
from quoteapp.views import quote,renderTemplates

urlpatterns = [
    path('quote/',quote),
    path('qtemp/',renderTemplates),
]
