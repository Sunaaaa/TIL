from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('<int:article_pk>/update/', views.update, name='update'), # UODATE Logic - 폼 전달
    path('<int:article_pk>/edit/', views.edit, name='edit'), # UODATE Logic - 폼 전달
    path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic 
    path('<int:article_pk>/', views.detail, name='detail'), # READ Logic - Detail
    path('new/', views.new, name='new'), # CREATE Logic - 데이터 베이스에 저장
    path('create/', views.create, name='create'), # CREATE Logic - 사용자에게 폼 전달
    path('', views.index, name='index'), # READ Logic - Index

]
