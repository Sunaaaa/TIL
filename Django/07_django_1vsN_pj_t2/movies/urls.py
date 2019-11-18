from django.urls import path
from . import views

app_name="movies"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('<int:movie_pk>/', views.detail, name="detail"),
    path('<int:movie_pk>/delete/', views.delete, name="delete"),
    path('<int:movie_pk>/edit/', views.edit, name="edit"),
    path('<int:movie_pk>/ratings/new', views.rating, name="rating"),
    path('<int:movie_pk>/ratings/<int:rating_pk>/delete', views.rating_delete, name="rating_delete"),

]
