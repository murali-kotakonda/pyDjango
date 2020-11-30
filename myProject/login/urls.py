from django.urls import path

from . import views


"""
# 1st arg is url
# 2nd arg is function name
# 3rd arg is alis name for url
"""
urlpatterns = [
    path('ex1/', views.ex1,name="ex1 page"),
    path('hello/', views.handleHello,name="ex2 page"),
    path('process/', views.process, name="ex3 page"),
    path('responseData/', views.handleResponseData,name=" page"),
    path('responseMultiData/', views.handleMultipleResponse,name="ex1 page"),
    path('show1/', views.handleShow1, name="show1-page"),
    path('show2/', views.handleShow2, name="show2-page"),
    path('show3/', views.handleShow3, name="show3 page"),
    path('show4/', views.handleShow4, name="show4 page"),
    path('show5/', views.handleShow5, name="show5 page"),
    path('show6/', views.handleShow6, name="show6 page"),
    path('', views.handleIndex,name="index page"),
    path('show7/', views.handleShow7, name="IF-page"),
    path('request1/', views.handleRequest1, name="request1-page"),
    path('submit1/', views.handleSubmit1, name="request1 page"),
    path('request11/', views.handleRequest1, name="request11-page"),
    path('submit11/', views.handleSubmit11, name="request1 page"),

    path('request2/', views.handleRequest2, name="request2 page"),
    path('submit2/', views.handleSubmit2, name="request2 page"),
    path('request3/', views.handleRequest3, name="request3 page"),
    path('submit3/', views.handleSubmit3, name="request3 page"),
    path('register/', views.handleRegister, name="request4 page"),
    path('reuse/', views.handleReuse, name="reuse page"),
    path('form1/', views.handleForm1, name="ex2 page"),
    path('processForm1/', views.handleForm2, name="ex2 page"),
    path('pdf/', views.getpdf, name="ex3 page"),
    path('csv/', views.getCsv, name="ex3 page"),
    path('setcookie/', views.handleSetCookie, name="ex3 page"),
    path('getcookie/', views.handleGetCookie, name="ex3 page"),
    path('person/', views.handlePerson, name="ex3 page"),
    path('onetoone/', views.handleOnetoone, name="ex3 page"),
    path('manytoone/', views.handleManytoone, name="ex3 page"),
    path('manytomany/', views.handleManytomany, name="ex3 page"),



]
