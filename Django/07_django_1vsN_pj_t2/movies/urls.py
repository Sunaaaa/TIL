from . import views
from django.urls import path

app_name="movies"
urlpatterns = [
    path('', views.index, name="index"),
]
