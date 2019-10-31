from django.urls import path
from . import views

app_name='jobs'
urlpatterns = [
    path('', views.index, name='index'), # READ Logic - Index
    path('job/', views.job, name='job'), 
]
