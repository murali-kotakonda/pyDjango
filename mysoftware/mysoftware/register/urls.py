from django.urls import path

from . import views


urlpatterns = [
    path('', views.handleIndex, name="index page"),
    path('myProfile/', views.handleMyProfile, name="index page"),
    path('editPerson/', views.handleUpdate, name="index page"),
    path('updatePerson/', views.handleUpdate1, name="index page"),
    path('loginAdmin/', views.handleLogin, name="index page"),  # welcome page
    path('logoutAdmin/', views.handleLogout, name="index page"),
    path('reg/', views.handlePerson, name="ex1 page"),
    #path('editpsw/', views.handleUpdate2, name="ex1 page"),
    #path('updatePassword/', views.handleUpdate3, name="index page"),


    ]