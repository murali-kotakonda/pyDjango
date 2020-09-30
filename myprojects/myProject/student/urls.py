from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.handleLogin,name="index page"),  #welcome page
    path('create/', views.handleCreate1, name="index page"),  # welcome page
    path('getstd/', views.handleGet, name="index page"),  # welcome page
    path('getstd1/', views.handleGet1, name="index page"),  # welcome page
    path('dltstd/', views.handleDlt, name="index page"),  # welcome page
    #path('dltemp/', views.handleDlt1, name="index page"),  # welcome page
    path('getall/', views.handleGetall, name="index page"),  # welcome page
    path('editStudent/', views.handleUpdate, name="index page"),  # welcome page
    path('updateStudent/', views.handleUpdate1, name="index page"),  # welcome page
    path('loginStudent/', views.handleLogin, name="index page"),  # welcome page
    path('logoutStudent/', views.handleLogout, name="index page"),  # welcome page
    path('csv/', views.getCsv, name="index page"),

]