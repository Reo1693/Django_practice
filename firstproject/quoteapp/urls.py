from django.urls import path
from quoteapp.views import quote

urlpatterns = [
    path('quote/',quote)
]
