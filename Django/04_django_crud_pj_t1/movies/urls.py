from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update', views.update, name='update'),
    path('<int:movie_pk>/delete', views.delete, name='delete'),
    path('<int:movie_pk>/comments', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),
    path('', views.index, name='index'), # READ Logic - Index

]
