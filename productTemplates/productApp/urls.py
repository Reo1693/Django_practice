from django.urls import path
from productApp.views import electronics,toys,shoes,index

urlpatterns = [
    path('',index),
    path('electronics/' ,electronics ),
    path('toys/' ,toys ),
    path('shoes/' ,shoes ),
]
