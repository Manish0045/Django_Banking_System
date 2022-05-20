from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('',views.home),
    path('Customers',views.customers,name='Customers'),
    path('Transactions',views.trans,name='Transactions')
]