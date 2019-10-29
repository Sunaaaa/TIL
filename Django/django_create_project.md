# Django 프로젝트

### 프로젝트 생성

![1572308747118](https://user-images.githubusercontent.com/39547788/67731576-0c214700-fa3c-11e9-9392-6592ad22395e.png)

<br>

![1572308775486](https://user-images.githubusercontent.com/39547788/67731577-0c214700-fa3c-11e9-8deb-54e50fccb2cc.png)

<br>

![1572309018303](https://user-images.githubusercontent.com/39547788/67731578-0c214700-fa3c-11e9-9123-c11f16b97e70.png)

<br>

![1572309031204](https://user-images.githubusercontent.com/39547788/67731579-0c214700-fa3c-11e9-8bc6-ed1391dbf04e.png)

<br>



### Application 생성

![1572309156043](https://user-images.githubusercontent.com/39547788/67731581-0cb9dd80-fa3c-11e9-855c-fddc7702c7f3.png)



<br>

![1572309188781](https://user-images.githubusercontent.com/39547788/67731583-0cb9dd80-fa3c-11e9-8090-4617f3b85f31.png)

<br>

#### settings.py

##### 앱 등록

![1572309306227](https://user-images.githubusercontent.com/39547788/67731584-0cb9dd80-fa3c-11e9-8c89-63163faa501a.png)

<br>

##### 한글로 설정 변경

```python  
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

<br>

##### 한글 로켓 

![1572309379045](https://user-images.githubusercontent.com/39547788/67731585-0cb9dd80-fa3c-11e9-9cbc-27f779f93cd2.png)

<br>

##### templates 폴더 생성

![1572311335089](https://user-images.githubusercontent.com/39547788/67731636-3a9f2200-fa3c-11e9-87dd-b704314ca45e.png)

<br>

### index 페이지 작성

- view 함수 지정

  - views.py

    ```python 
    from django.shortcuts import render
    
    # Create your views here.
    def index(request):
        context = {
            'god' : "폴킴"
        }
        return render(request, 'index.html', context)
    ```

    <br>

- urls.py

  ```python 
  from django.contrib import admin
  from django.urls import path
  from myapp import views
  
  urlpatterns = [
      path('', views.index),
      path('index/', views.index),
      path('admin/', admin.site.urls),
  ]
  ```

<br>

- index.html

  ```html
  <h1>안녕 ~ 노래의 신 {{god}} 님 </h1>
  ```

  <br>

- 실행 화면 ('/')

​	![1572310226565](https://user-images.githubusercontent.com/39547788/67731639-3e32a900-fa3c-11e9-8b6c-8547679313b2.png)

<br>

- 실행 화면 ('/index')

​	![1572310243741](https://user-images.githubusercontent.com/39547788/67731640-3e32a900-fa3c-11e9-9a0a-d0b016012c15.png)

<br><br>