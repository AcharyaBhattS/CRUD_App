from django.contrib import admin
from django.urls import path

from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HelloApp, name="Hello"),    
    path('index', views.show, name="Index"),
    path('contact', views.address, name="Contact"),
]
