from django.contrib import admin
from django.urls import path,include
from.import views
from django.views.generic import TemplateView


urlpatterns = [
    path('',views.index,name = "index"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('search/', views.search, name="search"),
]
