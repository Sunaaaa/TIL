"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    # 동적 라우팅을 위한 변수 설정
    path('hello/<str:name>/', views.hello),
    path('index/', views.index),

    # path('introduce/', views.introduce),
    # 동적 라우팅을 위한 변수 설정
    path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),

    # 동적 라우팅을 위한 변수 설정
    path('times/<int:num1>/<int:num2>', views.times),

    # 동적 라우팅을 위한 변수 설정
    path('radius/<int:rad>', views.radius),

    # 동적 라우팅을 위한 변수 설정
    path('imageSize/<str:width>/<str:height>', views.imageSize),

    path('dinner/', views.dinner),
    path('image/', views.image),
    path('admin/', admin.site.urls),
]
 