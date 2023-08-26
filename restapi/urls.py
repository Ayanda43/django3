from django.urls import path
from restapi import views

urlpatterns =[
    path('users/', views.UserList.as_view()),
    path('dataset/', views.DataList.as_view())
]