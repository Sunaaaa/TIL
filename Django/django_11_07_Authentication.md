# Authentication (인증)

> **Authentication (인증) --> 신원 확인**
>
> Django에서 이미 Authentication  관련 기능을 만들었고, 우리는 자연스럽게 사용하고 있었다. `createsuperuser`를 통해 관리자 계정도 만들었고, Admin 페이지에서 로그인 기능도 사용하고 있었다.

<br>

## 1. Accounts

> 기존 Application에서 구현해도 되지만, Django에서는 기능 단위로 Application을 나누는 것이 일반적이므로 **accounts** 라는 새로운 Application을 만들어보자!

<br>

- acounts Application 생성 및 등록

  ```bash
  # 생성
  $ python manage.py startapp acounts
  ```

  <br>

  ```python 
  # settings.py INSTALLED_APP 등록 
  INSTALLED_APPS = [
      'articles',
      'acounts',
      'imagekit',
      'bootstrap4',
      
      .
      .
  ]
  ```

  <br>

- urls 분리

  - config/ urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('acounts/', include('acounts.urls')),
        path('articles/', include('articles.urls')),
        path('admin/', admin.site.urls),
    ]
    ```

    <br>

  - acounts/urls.py

    ```python 
    from django.urls import path
    from . import views
    
    app_name="acounts"
    urlpatterns = [
        
    ]
    ```

<br>

<br>

## 2. Sign Up

- django가 가지고 있는 회원가입 Form을 가져온다.

  ```python 
  from django.contrib.auth.forms import UserCreationForm
  ```

- views.py

  - `form = UserCreationForm(request.POST)` : django 에서 제공하는 회원가입 Form을 가져온다. 

  - `form.is_valid()` 를 통해 유효성 검사를 수행한다.

    ```python 
    def signup(request):
        
        # 사용자를 만드는 로직
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
    
                # 회원가입 후 바로 로그인 되어 메인페이지로 이동
                auth_login(request, user)
    
                return redirect('articles:index')
    
    
        # 회원가입 Form을 던지는 로직
        else:
            form = UserCreationForm
        
        context = {
            'form' : form,
        }
    
        return render(request, 'acounts/signup.html', context)
    ```

- signup.html

  ```django
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  {% block body %}
  <h1>회원가입</h1>
  
  <hr>
  <form action="" method="POST">
  {% csrf_token %}
    {% bootstrap_form form layout="inline" %}
    {% buttons submit='가입' reset='초기화' %}
    {% endbuttons %}
  
  </form>
  
  {% endblock  %}
  ```

  <br>

- 실행 화면

  - signup.html

    - 초기화면 

      ![1573129312576](../AppData/Roaming/Typora/typora-user-images/1573129312576.png)

      <br>

    - 유효성 검증 실패 시 화면

      ![1573129333422](../AppData/Roaming/Typora/typora-user-images/1573129333422.png)

      <br>

    - admin 페이지를 통해 회원가입 확인!

      ![1573129375367](../AppData/Roaming/Typora/typora-user-images/1573129375367.png)

      <br>

      <br>

    



## 3. Login

### 3.1 로그인 하기

- django에 내장된 login view 함수를 사용하기 위해 import한다.

  ```python 
  from django.contrib.auth import login as auth_login
  ```

<br>

- 로그인 Form 가져오기

  ```python 
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
  ```

<br>

- views.py

  - `form = AuthenticationForm(request, request.POST)` 

    - django 에서 제공하는 로그인 Form을 가져온다. 
    - POST 방식으로 제공되는 사용자 정보를 가져오기 위해 Form의 인자로 `request`와 `request.POST`를 제공한다.

  - `form.is_valid()` 를 통해 유효성 검사를 수행한다.

  - `auth_login(request, form.get_user())`

    - 인증 과정 마무리 단계를 담당
      - 로그인 양식을 토대로 이용자 정보를 가져와서 HTTP Request(`request`) 정보와 함께 사용해 서버 세션 정보를 만든다. 세션 정보를 만들지 않으면 로그인 정보는 유지되지 않아서 다른 페이지에 방문할 때마다 매번 로그인을 해야 한다.
    - 장고의 미들웨어 중에 `'django.contrib.sessions.middleware.SessionMiddleware'` 와 `'django.contrib.auth.middleware.AuthenticationMiddleware'` 는 사용자 인증에 관한 처리를 담당한다. `SessionMiddleware` 는 로그인함수(`auth_login`)를 통해 생성된 세션을 관리한다. 
    - 확인된 사용자는 `request.user` 객체에 해당 사용자의 모델 인스턴스를 저장합니다.

  - `form.get_user()` : 인증에 성공한 사용자를 반환할 때 사용한다.

    ```python 
    def login(request):
    
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('articles:index')
        else : 
            form = AuthenticationForm()
    
        context = {
            'form' : form,
        } 
    
        return render(request, 'acounts/login.html', context)
    ```

  <br>

- login.html

  ```django
  {% extends 'base.html' %}
  
  {% load bootstrap4 %}
  
  {% block body %}
  <h1>로그인</h1>
  <hr>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit='로그인'  %}
    {% endbuttons %}
  </form>
  
  {% endblock  %}
  ```

  

<br>

- 실행 화면

  - login.html

    - 로그인 할 사용자 정보 입력

      - 로그인 성공

        ![1573129555042](../AppData/Roaming/Typora/typora-user-images/1573129555042.png)

        <br>

      - 로그인 실패

        ![1573129594610](../AppData/Roaming/Typora/typora-user-images/1573129594610.png)

        <br>

  - articles/ index

    - 로그인이 성공한 경우, article의 index 페이지로 이동한다.

      ![1573129637708](../AppData/Roaming/Typora/typora-user-images/1573129637708.png)

      <br>



### 3.2 로그인 심화 

> 로그인 이후, 로그인 로직과 회원가입 로직에 접근 불가능하도록 막아보자!
>
> - 로그인 한 사용자가  URL을 통해 로그인 혹은 회원가입 로직에 접근하면, 다시 index 페이지로 이동시킨다. 

<br>

- `request.user.is_authenticated`

  - 사용자인지 여부를 판단 -> Boolean 값 반환

    - True이면 로그인한 사용자

    - False이면 로그인하지 않은 사용자

      ```python 
      if request.user.is_authenticated:
              return redirect('articles:index')
      ```

  <br>

- views.py 

  ```python 
  def signup(request):
      
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      # 사용자를 만드는 로직
      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              # 회원가입 후 바로 로그인 되어 메인페이지로 이동
              auth_login(request, user)
              return redirect('articles:index')
  
      # 회원가입 Form을 던지는 로직
      else:
          form = UserCreationForm
      
      context = {
          'form' : form,
      }
  
      return render(request, 'acounts/signup.html', context)
  
  def login(request):
  
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == "POST":
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              return redirect('articles:index')
      else : 
          form = AuthenticationForm()
  
      context = {
          'form' : form,
      } 
  
      return render(request, 'acounts/login.html', context)
  ```

  <br>

## 4. Logout

> 로그아웃 버튼을 생성하여 로그아웃 기능을 구현해보자!
>
> - 로그인 한 상태 또는 로그인을 하지 않은 상태에 맞게 로그인 & 회원가입 또는 로그아웃 버튼을 보이도록 한다. 

<br>

- base.html

  - `user.is_authenticated` :로그인한 사용자 인지 판단 

    - 로그인한 사용자 -> 로그아웃 버튼

      로그인하지 않은 사용자 -> 회원가입 / 로그인 버튼

      ```django
      {% if user.is_authenticated  %}
      <h2>어서오세요, {{user.username}}</h2>
      <a href="{% url 'acounts:logout' %}">로그아웃</a>    
      
      {% else %}
      <h3>로그인 하셔야 서비스 이용이 가능합니다.</h3>
      <a href="{% url 'acounts:signup' %}">회원가입</a>    
      <a href="{% url 'acounts:login' %}">로그인</a>    
      {% endif %}
      ```

      

  - User 모델 Class

    - username : 사용자의 ID

      ```django
      <h2>어서오세요, {{user.username}}</h2>
      ```

    - password : 비밀번호 

    <br>

    ```django
    {% load bootstrap4 %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Article</title>
      {% bootstrap_css %}
    </head>
    <body>
      <div class="container">
        {% if user.is_authenticated  %}
          <h2>어서오세요, {{user.username}}</h2>
          <a href="{% url 'acounts:logout' %}">로그아웃</a>    
    
        {% else %}
          <h3>로그인 하셔야 서비스 이용이 가능합니다.</h3>
          <a href="{% url 'acounts:signup' %}">회원가입</a>    
          <a href="{% url 'acounts:login' %}">로그인</a>    
        {% endif %}
        <hr>
        {% block body %}
        {% endblock  %}
      </div>
      {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    ```

    <br>

- views.py

  ```python 
  def logout(request):
      # 이 서버를 보고 있는 사용자의 정보가 자동으로 들어가서 로그아웃을 수행한다.
      auth_logout(request)
      return redirect('articles:index')
  ```

  <br>

- 실행 화면

  - index.html

    - 로그인 한 사용자의 index 페이지에 로그아웃 버튼이 보여진다. 

      ![1573130825142](../AppData/Roaming/Typora/typora-user-images/1573130825142.png)

      <br>

    - 로그아웃 한 사용자의 index 페이지에 회원가입 과 로그인 버튼이 보여진다.

      ![1573130872598](../AppData/Roaming/Typora/typora-user-images/1573130872598.png)

<br>