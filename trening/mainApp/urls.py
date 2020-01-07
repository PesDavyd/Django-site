from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('contacts/', views.contacts, name='Contacts'),
    path('docs/', views.docs, name='Docs')
]
