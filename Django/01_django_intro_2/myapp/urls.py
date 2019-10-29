from django.urls import path
# 같은 경로 안에 있는 views.py
from . import views

urlpatterns = [
    path('static_sample/', views.static_sample),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('art/', views.art),
    path('result/', views.result),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('', views.index),
]
