from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('request_form/', views.request_form, name='request'),
    path('login/', views.my_login, name='my_login'),
    path('logout/', views.my_logout, name='logout'),
]