from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus/', views.contactus, name='contactus'),
    path('course/', views.course, name='course'),
    path('explore/', views.explore, name='explore'),
    path('zm_branch/', views.zm_branch, name='zm_branch')
]
