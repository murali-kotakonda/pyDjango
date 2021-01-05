from django.urls import path
from django.conf.urls import include, url
from . import views, restviews
from rest_framework import routers

#rest web services
router = routers.DefaultRouter()
router.register(r'users', restviews.UserViewSet)
router.register(r'groups', restviews.GroupViewSet)

urlpatterns = [
    path('rest/', include(router.urls)),
    path('rest1/welcome', restviews.welcome),
    path('rest1/getusers', restviews.get_users),
    path('rest1/adduser', restviews.add_user),
    #path('rest1/updateuser/<int:id>', restviews.update_book),
    #path('rest1/deleteuser/<int:id>', restviews.delete_book),

    path('', views.handleIndex,name="login-page"),
    path('registerAccount/', views.handleRegisterAccount, name="registerAccount-page"),
    path('accountLogin/', views.handleAccountLogin, name="accountLogin-page"),

    path('myAccountProfile/', views.handleShowMyAccount, name="myAccountProfile-page"),
    path('getAccount/', views.handleGetAccount, name="getAccount-page"),
    path('accountLogout/', views.handleAccountLogout, name="accountLogout-Employee"),
]


