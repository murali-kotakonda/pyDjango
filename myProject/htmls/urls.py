from django.urls import path

from . import views


"""
# 1st arg is url
# 2nd arg is function name
# 3rd arg is alis name for url
"""
urlpatterns = [
    path('ex1/', views.htmls_ex1,name="htmls_ex1 page"),
    path('ex2/', views.htmls_ex2,name="htmls_ex2 page"),
    path('alert/', views.htmls_alert,name="htmls_ex2 page"),
    path('form/', views.htmls_form,name="htmls_ex2 page"),
    path('window/', views.htmls_window,name="htmls_window page"),
    path('xpath1/', views.htmls_xpath1,name="htmls_xpath1 page"),
    path('xpath2/', views.htmls_xpath2, name="htmls_xpath1 page"),
    path('xpath3/', views.htmls_xpath3, name="htmls_xpath1 page"),
    path('xpath4/', views.htmls_xpath4, name="htmls_xpath1 page"),
    path('mouse1/', views.htmls_mouse1,name="htmls_mouse1 page"),
    path('mouse2/', views.htmls_mouse2,name="htmls_mouse2 page"),
    path('frames/', views.htmls_frames,name="htmls_frames page"),
    path('table/', views.htmls_table,name="htmls_table page"),
    path('links/', views.htmls_links,name="htmls_links page"),
    path('drag/', views.htmls_drag,name="htmls_drag page"),
    path('locators/', views.locators,name="htmls_drag page"),

    path('', views.htmls_index,name="htmls_index page"),

]
