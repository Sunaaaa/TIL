from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
        # URI : 자원에 대한 정보
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'), # POST (comments_create)
    path('<int:article_pk>/update/', views.update, name='update'), # GET (edit) / POST (update)
    path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic 
    path('<int:article_pk>/', views.detail, name='detail'), # READ Logic - Detail
    path('create/', views.create, name='create'), # GET (new) / POST (create)
    path('', views.index, name='index'), # READ Logic - Index

]
