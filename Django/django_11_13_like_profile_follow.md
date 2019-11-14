# Like / Profile / Follow

## 1. Like

> User는 여러 개의 게시글에 '좋아요' 표시를 할 수 있고, 게시글을 여러 명의 User에게 '좋아요' 를 받을 수 있다. 

<br>

### 1.1 모델 설정

#### [ articles Application ]

- models.py

  - `article.like_users`으로 User가 '좋아요' 누른 게시글을 알 수 있다. 

  - `related_name = 'like_articles'`

    - 현재 상황에서 `related_name` 옵션 설정은 필수
      - 만약, like_users 필드에 related_name을 쓰지 않으면, User 입장에서 article_set을 사용할 때 `user` 필드를 가져올지 `like_users`필드를 가져올지 인식하지 못한다.
      - related_name 설정과 함께 해당 필드는 article_set과 같은 방식으로 호출하지 못하고, `like_users` 방식으로 호출해야 된다.

  - `blank = True`

    - 최초 작성되는 글에는 좋아요가 없고, 글이 작성되더라도 좋아요를 받지 못할 수 있다.

    - `blank` 옵션을 부여해서 유효성 검사를 통과한다.

    - 실제 데이터베이스는 null이 들어가는게 아니라 빈 스트링(`' '`) 형태로 들어간다.

    ```python
    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=40)
        content = models.TextField()
    
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        # article.like_users
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
    
        # 객체 표시 형식 수정
        def __str__(self):
            return f'[{self.title}] {self.content}'
    ```

    

<br>

- migrate를 수행하고 sqlite3 를 확인한다.

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  - 임의의 테이블 'article_like_user'가 생성되었다. 

    ![1573641799654](django_11_13_like_profile_follow.assets/1573641799654.png)



<br>

#### [ 사용가능한 ORM 기능 (명령어) ]

##### User

- `user.article_set.all()` : User 가 작성한 게시글 전부 가져오기 [ 1 : N ]

- `user.like_articles.all()` : User 가 좋아요 누른 게시글 전부 가져오기 [ M : N ]

##### Article

- `article.user ` : 게시글을 작성한 User 가져오기 [ 1 : N ]

- `article.like_users ` : 유저가 작성한 게시글 전부 가져오기 [ M  : N ]

<br>

### 1.2 View & URL

#### [ articles Application ]

##### exists() & filter()

- `exists()` : 최소한 하나의 레코드가 존재하는지의 여부만 말해준다.
- `filter()` : 특정한 조건에 맞는 레코드들을 가져온다.

<br>

##### get() vs filter()

- 데이터가 없는 경우 에러 여부
  - get은 <u>에러발생</u>, 중복되는 데이터가 없을때 사용 가능하다.
  - filter는 에러가 발생하지 않는다.

<br>

- views.py

  - : 로그인한 사용자만 '좋아요'를 누를 수 있도록 한다.

  - `user in article.like_users.all()`: 현재 게시글에 '좋아요'를 누른 사람의 목록

    - 현재 접속한 User가 있는 경우 
      - 좋아요 취소
      - User를 현재 게시글에 '좋아요'를 누른 사람의 목록에서 삭제한다.
    - 현재 접속한 User가 없는 경우 
      - 좋아요 
      - User를 현재 게시글에 '좋아요'를 누른 사람의 목록에 추가한다.

    ```python 
    # 좋아요 기능
    @login_required
    def like(request, article_pk):
        # 좋아요 누른 게시글 가져오기
        article = get_object_or_404(Article, pk=article_pk)
        # 현재 접속하고 있는 User
        user = request.user
        # 현재 게시글에 좋아요를 누른 사람의 목록에서
        # 현재 접속한 User가 있는 경우 -> 좋아요 취소
        # 현재 접속한 User가 없는 경우 -> 좋아요 
        if user in article.like_users.all():
            article.like_users.remove(user)
        else : 
            # article.like_users.add(user)
            article.like_users.add(user)
    
        return redirect('articles:index')
    ```

  <br>

- urls.py

  ```python 
  from django.urls import path
  from . import views
  
  app_name="articles"
  urlpatterns = [
      path('', views.index, name="index"),
      path('create/', views.create, name="create"),
      path('<int:article_pk>/',views.detail, name="detail"),
      path('<int:article_pk>/delete',views.delete, name="delete"),
      path('<int:article_pk>/update',views.update, name="update"),
      path('<int:article_pk>/comments',views.comments_create, name="comments_create"),
      path('<int:article_pk>/comments/<int:comment_pk>/delete',views.comments_delete, name="comments_delete"),
      path('<int:article_pk>/like/', views.like, name="like"),
  ]
  
  ```

<br>

### 1.3 Template

#### 1.3.1 Templat 분리 (_article.html)

- <u>모듈화한 템플릿</u>은 제목 앞에 **언더스코어(_)** 붙여주는것이 **코딩 컨벤션**!

  ![1573643093584](django_11_13_like_profile_follow.assets/1573643093584.png)

  <br>

- _article.html

  - Bootstrap Card 컴포넌트를 사용해서 예쁘게 꾸며보자!!!
    - Bootstrap 공식 홈페이지 -> Documentation -> [Cards](https://getbootstrap.com/docs/4.3/components/card/)

      ```django
      <div class="col-12 col-md-6 mb-3">
          <div class="card">
              <div class="card-body">
                  <h5 class="card-title">
                      글 제목: {{ article.title }}
                  </h5>
                  <p class="card-text">
                      <a href="{% url 'articles:like' article.pk %}">좋아요</a><br>
                      {{ article.like_users.all|length }}명이 이 글을 좋아합니다. <br>
                      생성시각: {{ article.created_at }}
                  </p>
                  <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">상세보기</a>
              </div>
          </div>
      </div> 
      ```

<br>

- index.html

  - `{% include 'articles/_article.html' %}` : 모듈화 시켜둔 article 템플릿 가져오기

    ```django
    {% extends 'base.html' %}
    {% block body %}
      <h1>Articles</h1>
      <hr>
      <a href="{% url 'articles:create' %}">[NEW]</a>
      <hr>
      <div class="row">
        {% for article in articles %}
          <!-- 모듈화 시켜둔 article 템플릿 가져오기 -->
          {% include 'articles/_article.html' %}
        {% endfor %}  
      </div>
    
    
    {% endblock  %}
    
    ```

    <br>

- 실행 화면

  ![1573644084644](django_11_13_like_profile_follow.assets/1573644084644.png)

  <br>

#### 1.3.2 Font- Awesome 아이콘 적용 및 분기

> [Font- Awesome 홈페이지](https://fontawesome.com/) 들어가서 가입 후, 

<br>

- Kits로 들어가서 script 코드를 복사하여 base.html에 넣어준다.

  ```html
  <script src="https://kit.fontawesome.com/[kits코드번호].js" crossorigin="anonymous"></script>
  ```

  ![1573644453001](django_11_13_like_profile_follow.assets/1573644453001.png)

  - base.html

    ```django
    {% load bootstrap4 %}
    {% load gravatar %}
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        .
        .
        .
      <!-- FontAwesome -->
      <script src="https://kit.fontawesome.com/[kits코드번호].js" crossorigin="anonymous"></script>
    </head>
    
    ```

    <br>

- 원하는 아이콘을 선택한뒤, 코드를 복사하여 사용한다.

  ```python 
  # 하트 모양 아이콘
  <i class="fas fa-heart"></i>
  ```

  - _articles.html

    ```django
    <div class="col-12 col-md-6 mb-3">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">
            글 제목: {{ article.title }}
          </h5>
          <p class="card-text">
            <a href="{% url 'articles:like' article.pk %}">
              <!-- 사용자가 좋아요 누른 상태 -> 꽉찬 하트 -->
              {% if request.user in article.like_users.all %}
                <i class="fas fa-heart"></i>
              <!-- 안 누른 상태 -> 빈 하트 -->
              {% else %}
                <i class="far fa-heart"></i>
              {% endif %}
            </a><br>
            {{ article.like_users.all|length }}명이 이 글을 좋아합니다. <br>
            생성시각: {{ article.created_at }}
          </p>
          <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">상세보기</a>
        </div>
      </div>
    </div> 
    ```

- 실행 화면

  - '좋아요' 누르기 전

    ![1573645112498](django_11_13_like_profile_follow.assets/1573645112498.png)

    <br>

  - '좋아요' 누른 후 

    ![1573645131558](django_11_13_like_profile_follow.assets/1573645131558.png)

    <br>



## 2. Profile

> 로그인한 User는 '마이페이지' 버튼을 이용해 자신이 작성한 게시글과 댓글을 한눈에 볼 수 있다. 각 User 마다 프로필 페이지를 만들어주자.
>
> - User의 CRUD 로직 중 Read 로직에 해당한다.

<br>

### 2.1 View & URL

#### [ acounts Application ]

> User에 대한 CRUD 로직의 대부분을 acounts Application에서 구현했기 때문에, Profile 페이지 역시 acounts Application에 구현해보자.

<br>

- views.py

  - request로 들어오는 `username`으로 User에 대한 정보를 가져온다.

    ```python 
    from django.shortcuts import render, redirect, get_object_or_404
    from django.contrib.auth import get_user_model
    
    def profile(request, username):
        person = get_object_or_404(get_user_model(), username=username)
        context = {
            'person' : person,
        }
        return render(request, 'acounts/profile.html', context)
    ```

- urls.py

  - url 패턴에서 `str`을 사용하면 맨아래에 위치해서 마지막에 탐색되게 해야한다. 

    - 조건을 붙일경우에는 위치 상관 없다.

      ```python 
      from django.urls import path
      from . import views
      
      app_name="acounts"
      urlpatterns = [
          path('signup/', views.signup, name="signup"),
          path('login/', views.login, name="login"),
          path('logout/', views.logout, name="logout"),
          path('delete/', views.delete, name="delete"),
          path('update/', views.update, name="update"),
          path('password/', views.change_password, name="change_password"),
          path('<str:username>/', views.profile, name='profile'),
      ]
      
      ```



<br>

### 2.2 Template

> User가 작성한 게시글, 댓글을 볼 수 있는 profile.html을 만들어보자!

<br>

- base.html

  - 마이페이지로 이동하는 링크 생성

    ```django
    <a href="{% url 'acounts:profile' user.username %}" class="btn btn-warning">마이페이지</a>
    ```

    ```django
    <body>
      <div class="container">
        {% if user.is_authenticated  %}
          .
          .
          .
        <a href="{% url 'acounts:profile' user.username %}" class="btn btn-warning">마이페이지</a>
    
    ```

  <br>

- profile.html

  - `article.like_users.all|length` : 게시글에 '좋아요'를 누른 사람들의 수

  - `person.article_set.all` : User가 작성한 게시글 모두를 가져온다.

  - `person.comment_set.all` : User가 작성한 댓글 모두를 가져온다.

  - `coment.created_at|date:"SHORT_DATETIME_FORMAT"` : 날짜 표시 형식을 변형할 수 있다.

    ```django
    {% extends 'articles/base.html' %}
    
    {% block body %}
    <h1 class="text-center mt-3">{{ person.username }}님의 Profile</h1>
    <hr>
    <h3 class="text-center mb-3">{{ person.username }}님이 작성한 게시글</h3>
    <div class="row">
      {% for article in person.article_set.all %}
      <div class="col-12 col-md-6 mb-3">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">
              글 제목: {{ article.title }}
            </h5>
            <p class="card-text">
              {{ article.like_users.all|length }}명이 이 글을 좋아합니다. <br>
              생성시각: {{ article.created_at }}
            </p>
            <a href="{% url 'articles:detail' article.pk %}" class="btn btn-primary">상세보기</a>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
    </div>
    <hr>
    <h3 class="text-center mb-3">{{ person.username }}님이 작성한 댓글</h3>
    <div class="container">
      <div class="row">
        {% for coment in person.comment_set.all %}
        <div class="col-12 col-md-6 mb-3">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">
                {{ coment.content }}
              </h5>
              <p class="card-text">
                작성시각: {{ coment.created_at|date:"SHORT_DATETIME_FORMAT" }}
              </p>
              <a href="{% url 'articles:detail' coment.article.pk %}" class="btn btn-primary">게시글 확인</a>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
    {% endblock %} 
    ```

  <br>

- 실행 화면

  - 로그인하면 '마이페이지' 버튼이 보인다. 

    ![1573647175560](django_11_13_like_profile_follow.assets/1573647175560.png)

    <br>

  - 마이페이지

    - [1공선아]가 작성한 게시글과 댓글을 볼 수 있다.
      -  '상세보기' 또는 '게시글 확인' 버튼을 누르면, 해당 게시글의 상세정보를 볼 수 있다. 

    ![1573647090131](django_11_13_like_profile_follow.assets/1573647090131.png)

    <br>

### 2.3 Navigation Bar

> 상단에 메뉴 버튼들을 위해 Nav Bar를 만들어보자!

<br>

- nav bar 또한 모듈화한 템플릿으로 생성한다.

  ![1573647679188](django_11_13_like_profile_follow.assets/1573647679188.png)

  <br>

- _nav.html 

  - base.html의 상단 메뉴 버튼을 생성한 코드들을 _nav.html에 작성하고 bootstrap으로 꾸며보자

    ```django
    {% load gravatar %}
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="{% url 'articles:index' %}">
        <img class="rounded-circle mr-2" src="https://s.gravatar.com/avatar/{{ user.email|makemd5 }}?s=80&d=mp" alt="">
        Hello, {{ user.username }}
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          {% if user.is_authenticated %}
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'articles:index' %}">메인화면</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'acounts:logout' %}">로그아웃</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'acounts:profile' user.username %}">마이페이지</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'acounts:update' %}">정보수정</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'acounts:change_password' %}">암호변경</a>
            </li>
            <form action="{% url 'acounts:delete' %}" method="POST" style="display: inline;">
              {% csrf_token %}
              <input type="submit" value="회원탈퇴" class="btn btn-danger">
            </form>
          {% else %}
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'acounts:login' %}">로그인</a>
            </li>
            <li class="nav-item active">
              <a class="nav-link" href="{% url 'acounts:signup' %}">회원가입</span></a>
            </li>
          {% endif %}
        </ul>
      </div>
    </nav> 
    ```

  <br>

- base.html

  - `{% include 'articles/_nav.html' %}`를 `<div class="container">`안으로 넣으면 nav bar가 화면 전체를 차지하지 않게 된다. 

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
            <!-- FontAwesome -->
            <script src="https://kit.fontawesome.com/d3ba2beacb.js" crossorigin="anonymous"></script>
        </head>
    
        <body>
    
            {% include 'articles/_nav.html' %}
            <div class="container">
                {% block body %}
                {% endblock  %}    
            </div>
    
            {% bootstrap_javascript jquery='full' %}
        </body>
    
    </html>
    ```

<br>

- 실행 화면

  - 메인화면 nav bar

    ![1573648288591](django_11_13_like_profile_follow.assets/1573648288591.png)

  <br>

  - 반응형으로 페이지의 크기를 작게하면 nav bar 의 모습이 바뀐다.

    ![1573648341016](django_11_13_like_profile_follow.assets/1573648341016.png) 

<br>





## 3. Follow

> Follow는 User와 User의 M:N 관계이다.
>
> Django가 제공하는 User 모델을 대체해서 반복한다. 처음부터 User 모델을 만드는게 아니라, Django가 개발자들이 자신만의 User 모델을 만들 수 있도록 제공해준다.
>
> - **AbstractUser**

<br>

### 3.1 User 모델 대체하기

#### [ acounts Application ]

- models.py

  - `ManyToManyField`를 사용하면 자동으로 테이블을 만들어준다

    - 양방향 접근 가능

      ```python 
      from django.db import models
      from django.conf import settings
      from django.contrib.auth.models import AbstractUser
      
      # Create your models here.
      class User(AbstractUser):
          followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
      ```

  <br>

- settings.py

  ```python 
  # 기본값 : auth.User
  AUTH_USER_MODEL = 'acounts.User'
  ```

  <br>

- migrate

  - 기존에 있던 articles/migrations에 있는 파일들 중 `000숫자`가 붙은 파일들을 삭제

  - `db.sqlite3` 파일도 삭제

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

  -  sqlite3 로 확인하기

    ![1573649421149](django_11_13_like_profile_follow.assets/1573649421149.png)

  

#### 3.1.1 admin 추가

- admin 생성

  ```bash
  $ python manage.py createsuperuser
  사용자 이름: admin
  이메일 주소:
  Password:
  Password (again):
  비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
  비밀번호가 너무 일상적인 단어입니다.
  비밀번호가 전부 숫자로 되어 있습니다.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.
  ```

<br>

- admin.py

  ```python 
  from django.contrib import admin
  from django.contrib.auth.admin import UserAdmin
  from .models import User
  
  # Register your models here.
  admin.site.register(User, UserAdmin)
  ```

  <br>

- 실행 화면

  ![1573649672808](django_11_13_like_profile_follow.assets/1573649672808.png)

  <br>





### 3.2 View & URL

#### [ articles Application ]

- views.py

  ```python 
  from django.contrib.auth import get_user_model
  
  from django.views.decorators.http import require_POST
  from django.contrib.auth.decorators import login_required
  from django.shortcuts import render, redirect, get_object_or_404
  from django.contrib.auth import get_user_model
  from .models import Article, Comment
  from .forms import ArticleForm, CommentForm
  from IPython import embed
  import hashlib
  
  # Create your views here.
  def index(request):
      # embed()
      # if request.user.is_authenticated:
      #     gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
      # else : 
      #     gravatar_url = None
  
      articles = Article.objects.all()
      context = {
          'articles' : articles,
          # 'gravatar_url' : gravatar_url,
      }
      return render(request, 'articles/index.html', context)
  
  @login_required
  def create(request):
      if request.method=="POST":
          # embed()
  
          # Binding  과정
          # Form 인스턴스를 생성하고, 전달받은 데이터를 채운다.
          # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다.
          form = ArticleForm(request.POST)
          
          # 유효성 검증
          if form.is_valid():
              article = form.save(commit=False)
              article.user = request.user
              # 유효성 검증이 끝난 form은 dict 형태로 뽑혀 나온다.
              # cleaned_data 를 통해 dict 안의 데이터를 검증한다.
              # title = form.cleaned_data.get('title')
              # content = form.cleaned_data.get('content')
              # article = Article.objects.create(title=title, content=content)
              article.save()
  
              return redirect('articles:detail', article.pk)
      
      else :
          form = ArticleForm()
      # Form으로 전달 받는 형태가 2가지
      # 1. GET 요청 -> 비어있는 Form 전달
      # 2. 유효성 검증 실패 -> 에러 메시지도 담겨서 Form 전달        
      context = {
          'form' : form
      }
      return render(request, 'articles/form.html', context)
  
  def detail(request, article_pk):
      # article = Article.objects.get(pk=article_pk)
                                  # Class    / PK 값
      article = get_object_or_404(Article, pk=article_pk)
      comments = article.comment_set.all()
  
      comment_form = CommentForm()
  
      context = {
          'article' : article,
          'comment_form' : comment_form,
          'comments' : comments,
      }
      return render(request, 'articles/detail.html', context)
  
  @require_POST
  def delete(request, article_pk):
      # 삭제할 게시글 가져오기
      article = get_object_or_404(Article, pk=article_pk)
  
      # 지금 사용자가 로그인이 되어있는지 확인
      if request.user.is_authenticated:
  
          # 로그인한 사용자와 게시글 작성자 비교 
          # 같은 경우
          if request.user == article.user:
              article.delete()
  
          # 다른 경우
          else : 
              return redirect('articles:detail', article_pk)
      return redirect('articles:index')
  
  @login_required
  def update(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
      if request.user == article.user:
  
          if request.method == 'POST':
              form = ArticleForm(request.POST, instance=article)
  
              if form.is_valid():
                  article = form.save()
                  return redirect('articles:detail', article_pk)
  
          else :
              # 빈 값이 아닌 Form의 데이터를 넣어 주는 부분
              form = ArticleForm(instance=article)
  
      # 2가지 Form 형식
      # 1. GET 요청 -> 초기값을 Form에 넣어서 사용자에게 던져줌
      # 2. POST -> is_valid가 False 가 리턴되었을때, 
      #            오류 메시지를 포함해서 사용자에게 던져줌
      else:
          return redirect('articles:detail' , article_pk)
      context = {
          'form' : form,
          'article' : article,
      }
      # update와 create 로직에서 동일한 form을 던져주기 때문에 create.html을 랜더링한다.
      return render(request, 'articles/form.html', context)
  
  @require_POST
  def comments_create(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
      if request.user.is_authenticated:
          
          comment_form = CommentForm(request.POST)
  
          if comment_form.is_valid():
              # save 메서드 -> 선택 인자 : (기본 값) commit=True : DB에 바로 저장
              # commit=False : DB에 바로 저장되는 것을 막아준다.
              # 객체 저장 
              comment = comment_form.save(commit=False)
              # 인스턴스 그대로 넣기
              comment.article = article
              # 데이터 베이스에 저장되어 있는 형식에 맞춰서 넣기 -> article 인스턴스를 불러오지 않아도 된다.
              # comment.article_id = article_pk
              comment.user = request.user
              comment.save()
  
      return redirect('articles:detail', article_pk)
  
  @require_POST
  def comments_delete(request, article_pk, comment_pk):
      # 1. 로그인 여부 확인
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=article_pk)        
          comment = get_object_or_404(Comment, pk=comment_pk)
  
          # 2. 로그인한 사용자와 댓글 작성자가 같을 경우 삭제를 수행한다.
          if request.user == comment.user:
              comment.delete()    
      return redirect('articles:detail', article.pk)
  
  # 좋아요 기능
  @login_required
  def like(request, article_pk):
      # 좋아요 누른 게시글 가져오기
      article = get_object_or_404(Article, pk=article_pk)
      # 현재 접속하고 있는 User
      user = request.user
      # 현재 게시글에 좋아요를 누른 사람의 목록에서
      # 현재 접속한 User가 있는 경우 -> 좋아요 취소
      if user in article.like_users.all():
          article.like_users.remove(user)
      # 현재 접속한 User가 없는 경우 -> 좋아요 
      # User를 현재 게시글에 좋아요를 누른 사람의 목록에 추가한다. 
      else : 
          # article.like_users.add(user)
          article.like_users.add(user)
  
      return redirect('articles:index')
  
  def follow(request, article_pk, user_pk):
      # 게시글 작성한 User
      person = get_object_or_404(get_user_model(), pk=user_pk)
  
      # 지금 접속하고 있는 User
      user = request.user
  
      # 게시글을 작성한 User와 팔로우 버튼을 누르는 User가 
      # 다른 경우에만 팔로우를 할 수 있다.
      if person != user:
          # 게시글을 작성한 User의 팔로워 명단에 지금 접속하고 있는 User가 있을 경우
          # -> UnFollow
          if user in person.followers.all():
              person.followers.remove(user)
          # 없을 경우
          # -> Follow 
          else : 
              person.followers.add(user)
  
      # 게시글 상세 정보로 redirect
      return redirect('articles:detail', article_pk)
          
  
  
  ```

  







