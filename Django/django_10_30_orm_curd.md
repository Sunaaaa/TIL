# 19-10-30(수) Django CRUD 구현

## 0. 사전 작업

- 프로젝트 생성
- Application 생성
- URL 분리 (위임)
- 템플릿 경로 커스터 마이징 + base.html 만들기
- 데이터 베이스 모델링

<br>

## 1. CREATE

> 기본적으로 두 개의 뷰 함수로 구성된다.
>
> 1. 사용자에게 HTML Form을 던져줄 함수
> 2. HTML Form에서 데이터를 전달받아서 실제 DB에 저장하는 함수
>
> **GET 요청과 POST 요청을 통해 구현해보자!**



### 1.1 admin 설정

> 데이터가 정상적으로 저장됐는지 확인하기 위해 admin 페이지로 들어간다.

<br>



#### 1.1.1 admin 폼 생성

- admin 계정 생성 

  ```bash
  $ python manage.py createsuperuser
  ```

  <br>

- admin 폼 Customizing

  - admin.py

    ```python 
    from django.contrib import admin
    from .models import Article
    
    # Register your models here.
    
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    
    admin.site.register(Article, ArticleAdmin)
    ```

    <br>

- 게시글을 작성하면 admin의 게시글 목록에 추가되는 것을 확인할 수 있다.

  ![1572438050236](../AppData/Roaming/Typora/typora-user-images/1572438050236.png)

<br>



### 1.2 GET 요청

- form을 통해 title과 content를 입력받는다. 입력 받은 title과 content를 실제 데이터 베이스에 저장한다.

  - views.py

    ```python 
    from django.shortcuts import render, redirect
    from .models import Article
    
    # 사용자에게 게시글 작성 폼을 보여주는 함수
    def new(request):
        return render(request, 'articles/new.html')
    
    # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
    def create(request):
        title = request.GET.get('title')
        content = request.GET.get('content')
    
        article = Article(title=title, content=content)
        article.save()
    
        return redirect('/articles/create.html')
    ```

    <br>

  - new.html

    ```django
    {% extends 'base.html' %}
    
    {% block body %}
      <h1 class="text-center">NEW</h1>
    
      <form action="/articles/create/", method="GET">
        TITLE : <input type="text" name="title" > <br>
        CONTENT : <textarea type="text" name="content" cols="30" rows="10"> </textarea> <br>
    
        <input type="submit">
      </form>
    
      <hr>
      <a href="/articles/">[BACK]</a>
    
    {% endblock  %}
    ```

  <br>

  - create.html

    ```django
    {% extends 'base.html' %}
    
    {% block body %}
      <h1 class="text-center">글 작성이 완료 되었습니다. </h1>
    
      <hr>
      <a href="/articles/new/">[NEW]</a>
      <a href="/articles/">[INDEX]</a>
    {% endblock  %}
    
    ```

    

<br>





### 1.3 POST 요청

> 지금은 GET 요청으로 보내고 있어서 쿼리 스트링에 데이터가 노출되고 있다. 이는 우리 서버의 데이터 구조가 노출될 위험도 있고, URL 경로로만 게시글 작성이 가능하면 서버 폭파의 위험성이 증가한다.
>
> - POST 요청으로 바꾸어 HTTP body에 내용을 숨기고 작성자의 신원을 확인하는 절차를 거치도록 하자.
> - CSRF 를 이용해 신원을 확인한다.

<br>

- new.html

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
  <h1 class="text-center">NEW</h1>
  <form action="/articles/create/" method="POST">
    {% csrf_token %}
    TITLE: <input type="text" name="title"><br>
    CONTENT: <textarea name="content" cols="17" rows="4"></textarea><br>
    <input type="submit">
  </form>
  <hr>
  <a href="/articles/">[BACK]</a>
  {% endblock %}
  ```

  <br>

- views.py

  ```python 
  def new(request):
      return render(request, 'articles/new.html')
  
  def create(request):
      title = request.POST.get('title')
      content = request.POST.get('content')
      article = Article(title=title, content=content)
      article.save()
      return render(request, 'articles/create.html')
  ```



### 1.4 redirect

> 지금은 게시글 작성 완료 후, create.html 페이지로 이동해 다소 어색한 로직이 구현되어 있다. 
>
> - **sqlite에 게시글 작성이 완료되면 메인 페이지로 redirect 시켜버리자.**

<br>

- views.py

  ```python 
  from django.shortcuts import render, redirect
  
  def create(request):
      title = request.POST.get('title')
      content = request.POST.get('content')
      article = Article(title=title, content=content)
      article.save()
      return redirect('/articles/')
  ```

  <br>



## 2. READ

> sqlite 에서 가져온 게시글 목록을 가져와 페이지에 보여줄 수 있다.
>
> 게시글 목록이 출력되는 메인 페이지에서 글 내용, 수정 시각 등 모든 정보를 보여줄 필요는 없다. **메인 페이지에선 글 번호, 글 제목과 같은 기본적인 내용만 보여주고, 사용자가 클릭했을 때 게시글 상세정보 페이지로 이동**하도록 만들어보자.

<br>

### 2.1 게시글 목록 보여주기

- sqlite 에서 게시글 목록 전부를 가져와 index 페이지에서 보여준다.

  - views.py

    ```python 
    def index(request):
        articles = Article.objects.all()[::-1]
        context = {'articles': articles}
        return render(request, 'articles/index.html', context)
    ```

    <br>

  - index.html

    ```django
    {% extends 'base.html' %}
    
    {% block body %}
      <h1 class="text-center">Articles</h1>
    
      <hr>
      <a href="/articles/new/">[NEW]</a>
      <hr>
    
      {% for article in articles %}
      <p>[{{article.pk}}] : {{article.title}}</p>
      <a href="/articles/{{article.pk}}">[DETAIL]</a>
    
      <hr>
      
      {% endfor %}
      <hr>
    
    {% endblock  %}
    
    ```

    <br>



### 2.1 게시글 목록 제목/상세내용 구분

> 지금은 index 페이지에서 게시글의 제목 뿐만 아니라 상세 내용까지 모두 보인다. 이제는 index 페이지 목록에는 게시글 번호와 제목만 보이고, 사용자가 링크를 클릭했을 때 게시글 상세 정보 페이지로 이동하도록 구현해보자!

- views.py

  ```python 
  # 게시글 상세 정보를 가져오는 함수
  def detail(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      context = {
          'article' : article
      }
      return render(request, 'articles/detail.html', context)
  ```

  <br>

- urls.py

  ```python 
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('<int:article_pk>/', views.detail),
      path('new/', views.new),
      path('create/', views.create),
      path('', views.index),
  
  ]
  ```

- detail.html

  ```django
  {% extends 'base.html' %}
  
  {% block body %}
    <h1 class="text-center">DETAIL</h1>
  
    <p>글 번호 : {{article.pk}}</p>
    <p>글 제목 : {{article.title}}</p>
    <p>글 내용 : {{article.content}}</p>
    <p>생성 시간 : {{article.created_at}}</p>
    <p>수정 시간 : {{article.updated_at}}</p>
    <hr>
  
    <a href="/articles/">[INDEX]</a>
  
  {% endblock  %}
  ```

- index.html

  ```django
  {% extends 'base.html' %}
  
  {% block body %}
    <h1 class="text-center">Articles</h1>
  
    <hr>
    <a href="/articles/new/">[NEW]</a>
    <hr>
  
    {% for article in articles %}
    <p>[{{article.pk}}] : {{article.title}}</p>
    <a href="/articles/{{article.pk}}">[DETAIL]</a>
  
    <hr>
    
    {% endfor %}
    <hr>
  
  {% endblock  %}
  ```

  

