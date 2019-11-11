# Authentication (인증)

> **Authentication (인증) --> 신원 확인**
>
> Django에서 이미 Authentication  관련 기능을 만들었고, 우리는 자연스럽게 사용하고 있었다. `createsuperuser`를 통해 관리자 계정도 만들었고, Admin 페이지에서 로그인 기능도 사용하고 있었다.

<br>



## [ Session (세션) ]

> 클라이언트가 서버에 접속하면, 서버가 특정한 session_id를 발급한다. 클라이언트는 session_id를 쿠키를 사용해 저장한다.
>
> 클라이언트가 서버 측 여러 페이지에 이동할 때마다, 해당 쿠기 (session_id)를 이용해서 서버레 session_id를 전달한다.
>
> - 따라서 서버는 페이지가 바뀌더라도 같은 사용자임을 인지할 수 있다.
>
> **로그인하자마자 request를 통해 세션 정보를 가져올 수 있다!!!!!!!!!!!!!!**

<br>

### [ 쿠키 VS 세션 ]

#### 쿠키

- 클라이언트 로컬에 **파일**로 저장

<br>

#### 세션

- **서버**에 저장

- session_id는 쿠키 형태로 클라이언트 로컬에 저장됨

<br>



#### 세션 정보 확인하기

- 아무도 로그인이 되어 있지 않은 경우

  ```python 
  In [3]: request.session.items()
  Out[3]: dict_items([])
  
  In [4]: request.session._session
  Out[4]: {}
  ```

  <br>

- 현재 로그인하고 있는 사용자가 있는 경우

  ```python 
  In [3]: request.session._session
  Out[3]:
  {'_auth_user_id': '1',
  '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
  '_auth_user_hash': 'b3bd805335e5bcec99e9aef8476bd76776476ca8'}
  
  In [4]: request.session.items()
  Out[4]: dict_items([('_auth_user_id', '1'), ('_auth_user_backend', 'django.contrib.auth.backends.ModelBackend'), ('_auth_user_hash', 'b3bd805335e5bcec99e9aef8476bd76776476ca8')])
  ```

<br>

- **request를 통해 session정보가 들어오기 때문에 <u>User Class</u>를 통해 사용자 정보를 얻어올 수 있다.** 

  ```
  In [1]:  request
  Out[1]: <WSGIRequest: GET '/articles/'>
  
  In [2]:  request.user
  Out[2]: <SimpleLazyObject: <User: admin>>
  
  In [3]: request.user.is_authenticated
  Out[3]: True
  
  In [4]: request.user.is_superuser
  Out[4]: True
  
  In [5]: request.user.is_anonymous
  Out[5]: False
  ```

  <br>

  ![1573436036170](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573436036170.png)



<br>

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

> 회원가입 로직은 CRUD 중에 'CREATE'에 가깝다.
>
> **User 클래스**는 이미 장고가 만들어 두었고, User 클래스와 연동되는 ModelForm인 UserCreationForm도 장고가 이미 준비해 두었다. 

<br>

- django가 가지고 있는 회원가입 Form을 가져온다.

  ```python 
  from django.contrib.auth.forms import UserCreationForm
  ```

- views.py

  - `form = UserCreationForm(request.POST)` : django 에서 제공하는 회원가입 Form을 가져와 사용자로부터 데이터를 받아온다.

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

      ![1573129312576](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573129312576.png)

      <br>

    - 유효성 검증 실패 시 화면

      ![1573129333422](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573129333422.png)

      <br>

    - admin 페이지를 통해 회원가입 확인!

      ![1573129375367](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573129375367.png)

      <br>

      

#### 유효성 검사

- Shell로 확인하기

  ```python 
  form
  form.as_p()
  dorm.get_user()
  form.is_valid()
  ```

  

<br><br>



## 3. Login

> Django에서 로그인하는 것은 session을 CREATE하는 것과 같다.
>
> - Django는 session에 대한 매커니즘을 생각하지 않아도 쉽게 사용할 수 있다. 
> - sessoion 사용자가 로그인을 하면, 사용자가 로그아웃을 하거나 정해진 일정한 시간이 지나기 전까지는 계속 유지된다. 
>
> User를 인증하는 ModelForm : **AuthenticationForm**
>
> - `AuthenticationForm(request, request.FORM)`
>   - Login은 session이라는 정보가 추가되기 때문에 request를 첫번째 인자로 넘겨 request session 정보를 주어야 한다.
>   - request.FORM : 사용자로 부터 로그인 정보를 가져온다.

<br>

### 3.1 로그인 하기

- django에 내장된 login view 함수를 사용하기 위해 import한다.

  - 원래 이름은 login / 별칭으로 auth_login

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

        ![1573129555042](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573129555042.png)

        <br>

      - 로그인 실패

        ![1573129594610](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573129594610.png)

        <br>

  - articles/ index

    - 로그인이 성공한 경우, article의 index 페이지로 이동한다.

      ![1573129637708](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573129637708.png)

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



#### 유효성 검사

- Shell로 확인하기

  ```python 
  form
  form.as_p()
  dorm.get_user()
  form.is_valid()
  form.get_user().username
  ```

  

<br><br>



### 3.3 login_required 데코레이터

> 로그인을 하지 않은 사용자는 삭제, 수정, 댓글 등의 기능을 이용하기 위해서는 로그인이 필요하다. 그래서 로그인 페이지로 이동한 뒤, 로그인이 성공적으로 완료되면 이전에 있었던 페이지로 이동한다.
>
> - 비회원인 상태로 [new]를 하면 로그인 페이지로 이동
>   - 로그인을 하면 [new] 를 할 수 있는 form 페이지로 다시 이동
> - 비회원인 상태로 [delete]를 하면 로그인 페이지로 이동
>   - 로그인을 하면 [delete] 를 수행
>
> <br>
>
> 로그인을 하지 않은 사용자의 경우, `settings.LOGIN_URL`에 설정된 절대 경로로 redirect 된다. 
>
> - LOGIN_URL의 기본 경로는 `acounts/login` 이다.
> - Application의 이름을 accounts로 했을 경우
> -  Application의 이름을 accounts가 아닌 경우, 경로를 커스터마이징 해야한다.
>
> <br>
>
> `@login_required`를 사용했을 경우, 주소창에 특이한 Query String이 붙는다.
>
> - `next` 라는 Query String Parameter
>
>   - `@login_required`는 기본적으로 성공한 뒤에 사용자를 어디로 보낼지 (redirect )에 대한 경로를 next 라는 Parameter에 저장한다.
>
>   - 사용자가 접근했던 페이지가 반드시 로그인에 필요한 페이지였기 때문에, 일단 로그인 페이지로 강제로 보낸 다음 로그인을 끝낸 뒤 **원래 요청했던 주소로 보내주기 위해 경로를 KEEP 해둔다.**
>
>   - 우리가 따로  설정해주지 않으면, view에 설정해둔 redirect 경로로 이동한다. next에 담긴 경로로 이동시키기 위해 코드를 바꾸어야 한다.
>
>     ```python 
>     return redirect(request.GET.get('next') or 'articles:index')
>     ```

<br>

#### [ articles Application ]

```python 
from django.contrib.auth.decorators import login_required
```

- views.py

  ```python 
  @login_required
  def create(request):
      if request.method=="POST":
          form = ArticleForm(request.POST)
          
          # 유효성 검증
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
      
      else :
          form = ArticleForm()
      context = {
          'form' : form
      }
      return render(request, 'articles/form.html', context)
  
  ```

  <br>

  <br>



#### [ acounts Application ]

> **커스터마이징이** 필요한 경우!

<br>

**문제 발생!!**

- Application의 이름이 accounts가 아닌 acounts 이기 때문에 위의 코드를 그대로 수행하면 에러가 발생한다.

  ![1573437286157](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573437286157.png)

  <br>

- settings.py에 `LOGIN_URL = '/acounts/login/'`를 추가한다.

  ```python 
  # login_required 요청 경로 커스터마이징
  # 기본 : /accounts/login/
  LOGIN_URL = '/acounts/login/'
  ```

  - URL이 `http://127.0.0.1:8000/acounts/login/?next=/articles/create/`

    ![1573437646307](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573437646307.png)

<br>



**문제 발생!!**

- `@login_required` 과 `@require_POST`를 동시에 사용하면, delete를 GET 요청으로 수행하게 된다. 

  - `http://127.0.0.1:8000/acounts/login/?next=/articles/1/delete` -> GET 요청

    ```python 
    # 문제 발생 코드
    @login_required
    @require_POST
    def delete(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return redirect('articles:index')
    ```

    <br>



**해결** 

- **@login_required**를 내부에서 사용한다.

  - `if request.user.is_authenticated:`를 추가하여 로그인 여부를 확인한다. 

    ```python 
    @require_POST
    def delete(request, article_pk):
        if request.user.is_authenticated:
            article = get_object_or_404(Article, pk=article_pk)
            article.delete()
        return redirect('articles:index')
    ```

    <br>

- **@require_POST**를 내부에서 사용한다.

  - `if request.method == 'POST':`를 추가하여 로그인 여부를 확인한다. 

    ```ㅍ
    @login_required
    def delete(request, article_pk):
        if request.method == 'POST':
            article = get_object_or_404(Article, pk=article_pk)
            article.delete()
        return redirect('articles:index')
    ```

    <br><br>



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

      <br>

  - User 모델 Class

    - username : 사용자의 ID

      ```django
      <h2>어서오세요, {{user.username}}</h2>
      ```

    - password : 비밀번호 

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

  - `auth_logout(request)` : 현재 유지하고 있는 session을 DELETE하는 로직

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

      ![1573130825142](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573130825142.png)

      <br>

    - 로그아웃 한 사용자의 index 페이지에 회원가입 과 로그인 버튼이 보여진다.

      ![1573130872598](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573130872598.png)

<br>

<br>



## 5. Sign Out (회원 탈퇴)

> CRUD 로직에서 User 테이블에서 User 레코드 하나를 삭제 시키는 DELETE 로직과 흡사하다.
>
> - 로그인 된 상태에서만 회원탈퇴 링크를 만들어서 접근할 수 있도록 한다.

<br>

- 이미 로그인이 되어 있기 때문에 request에 이미 로그인하고 있는 사람의 session, user 정보가 들어가 있다.

  - `delete()` 만 해주면 끝!
    - 지금 접속하고 있는 user 삭제

  ```python 
  @require_POST
  def delete(request):
      request.user.delete()
      return redirect('articles:index')
  ```



<br><br>

## 6. 회원 정보 수정

- Django에서 제공하는 회원 정보 수정 폼 (UserChangeForm) 을 가져다 사용한다. 

```python 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
```

<br>

- 회원정보 폼에는 user의 정보가 들어가 있어야 한다.

  - instance로 request.user를 통해 사용자의 정보를 가져온다.

    ```python 
    # 회원정보 수정
    def update(request):
        if request.method == "POST":
            pass
        else:
            # 회원정보 폼에는 user의 정보가 들어가 있어야 한다.
            # instance로 request.user를 통해 사용자의 정보를 가져온다.
            form = UserChangeForm(instance=request.user)
        
        context = {
            'form' : form
        }
    
        return render(request, 'acounts/update.html', context)
    ```

    <br>



<br>

**문제 발생**

- 너무 많은 수정 권한을 부여하게 된다.

  ![1573460527170](C:/Users/student/AppData/Roaming/Typora/typora-user-images/1573460527170.png)

  <br>



### 6.1 회원정보수정 Form Customizing

> 회원정보수정 Form을 커스터 마이징하여 사용자가 제한적으로 회원 정보를 수정하도록 한다.
>
> - [django 깃허브](https://github.com/django/django)에 들어가서 사용자로 하여금 수정이 가능하도록 할 회원정보에 대한 field를 설정할 수 있다. 

<br>

- acounts/ forms.py 생성

  ![1573460738269](C:%5CUsers%5Cstudent%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5C1573460738269.png)

  <br>

- 







- 새롭게 커스텀한 폼을 사용한다. 

```
from .forms import CustomUserChangeForm
```

UserChangeForm import한 것 제거 



비회원은 수정 페이지에 들어가지 못하게 막아준다. `@login_required`







##  7. 비밀번호 변경

### 7.1 비밀번호 변경하기

```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
```



```
# 비밀번호 수정
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        pass

    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form' : form
    }

    return render(request, 'acounts/change_password.html', context)
```

- 실행 화면
  - 비밀번호 변경
  - 자동 로그아웃 되어 index.html로 이동한다. 



<br>

### 7.2 자동 로그아웃 해제

update_session_auth_hash

> 비밀번호 변경은 성공적으로 반영이 되지만, 변경이 끝나면 로그인이 풀려 자동으로 로그아웃을 수행한다.
>
> - 비밀번호가 변경되면서 기존 session과 회원 인증 정보가 불일치하기 때문
> - **`update_session_auth_hash(request, user)`로 해결!!!**





```
from django.contrib.auth import update_session_auth_hash
```

- q비밀번호를 수정한 뒤, 수정한 값을 바로 session에 update하기 때문에 로그인이 풀리지 않는다. 







## 8. Auth Form 통합

Form을 하나의 html에서 사용 

-> 재사용성을 높여보자!



- acount_form.html

  ```django
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  {% block body %}
  
  {% if request.resolver_match.url_name == 'signup' %}
  <h1>회원가입</h1>
  {% elif request.resolver_match.url_name == 'login' %}
  <h1>로그인</h1>
  {% elif request.resolver_match.url_name == 'update' %}
  <h1>회원정보 수정</h1>
  {% else %}
  <h1>비밀번호 변경</h1>
  {% endif %}
  
  <hr>
  
  <form action="" method="post">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% buttons submit='수정' reset='초기화' %}
  {% endbuttons %}
  </form>
  
  {% endblock  %}
  ```

  



<br>



### 9. Gravatar - 프로필 이미지 만들기

> 이메일을 활용해서 프로필 사진을 만들어주는 서비스이다. 한번 등록하면, 이를 지원하는 사이트에서는 모두 해당 프로필 이미지를 사용할 수 있다. 
>
> <br>





이메일 체크

- `https://ko.gravatar.com/site/check/`
- 이메일 주소를 해시 (MD5)로 바꾼 뒤, URL을 통해 접속하면 등록된 이미지가 본인다.
  - s Query String으로 사이즈를 조절한다.
  - `?s=80`





base.html

```
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
    <h2> <img src="https://s.gravatar.com/avatar/f87913b9277844f3c095a7aa64f5fd9e?s=80" alt=""> 어서오세요, {{user.username}}</h2>
    <a href="{% url 'acounts:logout' %}" class="btn btn-warning">로그아웃</a>
    <a href="{% url 'acounts:update' %}" class="btn btn-warning">회원정보 수정</a>
    <a href="{% url 'acounts:change_password' %}" class="btn btn-warning">비밀번호 변경</a>

    <form action="{% url 'acounts:delete' %}" method="post" style="display : inline">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴" class="btn btn-danger">

    </form>

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



https://s.gravatar.com/avatar/f87913b9277844f3c095a7aa64f5fd9e?s=800





Python으로 Hash 만들기

- MD5 Hash 생성
  - import hashlib
- 혹시 모를 공백, 대문자 등을 방지하기 위한 파이썬 문법들
  - .strip(), lower()



```python 
>>> import hashlib
>>> hashlib.md5('glglthssla@gmail.com'.encode('utf-8').lower().strip()).hexdigest()
'f87913b9277844f3c095a7aa64f5fd9e'
>>> img_url = hashlib.md5('glglthssla@gmail.com'.encode('utf-8').lower().strip()).hexdigest()
```



- 프로필 이미지를 받기 위해 회원가입 폼을 커스터 마이징한다.
  - 회원가입 폼에 email 정보를 받는다.



[acounts]

```
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email',)
```



```
from .forms import CustomUserChangeForm, CustomUserCreationForm

def signup(request):
    
    if request.user.is_authenticated:
        return redirect('articles:index')

    # 사용자를 만드는 로직
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # 회원가입 후 바로 로그인 되어 메인페이지로 이동
            auth_login(request, user)

            return redirect('articles:index')


    # 회원가입 Form을 던지는 로직
    else:
        form = CustomUserCreationForm
    
    context = {
        'form' : form,
    }

    return render(request, 'acounts/acount_form.html', context)
```





[articles]



```python 
import hashlib

# Create your views here.
def index(request):
    # embed()
    if request.user.is_authenticated:
        gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
    else : 
        gravatar_url = None

    articles = Article.objects.all()
    context = {
        'articles' : articles,
        'gravatar_url' : gravatar_url,
    }
    return render(request, 'articles/index.html', context)
```



```
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
    <h2> <img src="https://s.gravatar.com/avatar/{{img_url}}?s=80" alt=""> 어서오세요, {{user.username}}</h2>
    <a href="{% url 'acounts:logout' %}" class="btn btn-warning">로그아웃</a>
    <a href="{% url 'acounts:update' %}" class="btn btn-warning">회원정보 수정</a>
    <a href="{% url 'acounts:change_password' %}" class="btn btn-warning">비밀번호 변경</a>

    <form action="{% url 'acounts:delete' %}" method="post" style="display : inline">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴" class="btn btn-danger">

    </form>

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









커스텀



templatetags



base.html

```
{% load bootstrap4 %}
{% load gravatar %}
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
    <h2> <img src="https://s.gravatar.com/avatar/{{user.email|makemd5}}?s=80" alt=""> 어서오세요, {{user.username}}</h2>
    <a href="{% url 'acounts:logout' %}" class="btn btn-warning">로그아웃</a>
    <a href="{% url 'acounts:update' %}" class="btn btn-warning">회원정보 수정</a>
    <a href="{% url 'acounts:change_password' %}" class="btn btn-warning">비밀번호 변경</a>

    <form action="{% url 'acounts:delete' %}" method="post" style="display : inline">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴" class="btn btn-danger">

    </form>

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

