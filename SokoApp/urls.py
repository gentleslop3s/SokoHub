
from django.contrib import admin
from django.urls import path

from SokoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home),

    path('contact/', views.contact),

    path('about/', views.about),

    path('services/', views.services)

]
