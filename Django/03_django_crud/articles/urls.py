from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_pk>/', views.detail),
    path('new/', views.new),
    path('create/', views.create),
    path('', views.index),

]
