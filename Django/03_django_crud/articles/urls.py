from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('<int:article_pk>/update/', views.update, name='update'), # GET (edit) / POST (update)
    path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic 
    path('<int:article_pk>/', views.detail, name='detail'), # READ Logic - Detail
    path('create/', views.create, name='create'), # GET (new) / POST (create)
    path('', views.index, name='index'), # READ Logic - Index

]
