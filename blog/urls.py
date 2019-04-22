from django.urls import path
#import views here
from . import views

urlpatterns = [
    path('', views.home, name = "blog-home"),
    path('about/', views.about, name = "blog-about"),
]
