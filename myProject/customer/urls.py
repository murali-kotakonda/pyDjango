from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.handleLogin,name="login-page"),  #welcome page
    path('create/', views.handleCreate1, name="create-page"),  # welcome page
    path('getemp/', views.handleGet, name="getEmp-page"),  # welcome page
    path('getemp1/', views.handleGet1, name="getemp1 page"),  # welcome page
    path('dltemp/', views.handleDlt, name="delete-page"),  # welcome page
    #path('dltemp/', views.handleDlt1, name="index page"),  # welcome page
    path('getall/', views.handleGetall, name="getall-page"),  # welcome page
    path('editEmployee/', views.handleUpdate, name="index page"),  # welcome page
    path('updateEmployee/', views.handleUpdate1, name="updateEmployee page"),  # welcome page
    #path('sortEmployee/', views.handleSort, name="index page"),  # welcome page
    path('loginEmployee/', views.handleLogin, name="loginEmployee-page"),  # welcome page
    path('pagination/', views.handlePagination, name="pagination-page"),
    path('logoutEmployee/', views.handleEmpLogout, name="logout-Employee"),


]
