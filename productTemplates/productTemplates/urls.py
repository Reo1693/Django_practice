from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from productApp.views import electronics,toys,shoes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('productApp.urls')),
    path('electronics/' ,electronics ),
    path('toys/' ,toys ),
    path('shoes/' ,shoes ),
]
