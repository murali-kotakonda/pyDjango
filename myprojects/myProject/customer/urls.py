from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.handleLogin,name="index page"),  #welcome page
    path('create/', views.handleCreate1, name="index page"),  # welcome page
    path('getemp/', views.handleGet, name="index page"),  # welcome page
    path('getemp1/', views.handleGet1, name="index page"),  # welcome page
    path('dltemp/', views.handleDlt, name="index page"),  # welcome page
    #path('dltemp/', views.handleDlt1, name="index page"),  # welcome page
    path('getall/', views.handleGetall, name="index page"),  # welcome page
    path('editEmployee/', views.handleUpdate, name="index page"),  # welcome page
    path('updateEmployee/', views.handleUpdate1, name="index page"),  # welcome page
    #path('sortEmployee/', views.handleSort, name="index page"),  # welcome page
    path('loginEmployee/', views.handleLogin, name="index page"),  # welcome page
    path('logoutEmployee/', views.handleLogout, name="index page"),  # welcome page




]
