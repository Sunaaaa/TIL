from django.urls import path
from . import views

app_name='students'
urlpatterns = [
    path('', views.index, name='index'), # READ Logic - Index
    path('new/', views.new, name='new'), 
    path('create/', views.create, name='create'), 
    path('<int:student_pk>', views.detail, name='detail'), 
    path('<int:student_pk>/edit', views.edit, name='edit'), 
    path('<int:student_pk>/update', views.update, name='update'), 
    path('<int:student_pk>/delete', views.delete, name='delete'), 
]
