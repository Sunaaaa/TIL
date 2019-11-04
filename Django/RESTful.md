# RESTful API

> HTML 에서 공식적인 지원은 GET / POST
>
> - 일부 프레임워크를 제외하고는 대부분 위의 두가지로 수행해야한다.
>
> HTTP URI 를 통해 자원()을 명시하고 , HTTP Method () 를 통해 해당 자원에 대한 CRUD 로직을 적용하는 것
>
> - 혼자 개발해서 혼자 사용할 용도라면, articles/1/butterfly/show/magic 처럼 그냥 마구잡이로 개발하고 작동만 하면 된다. 
> - 하지만 다른 사람이 사용하는 것을 염두해 둔다면, [GET]articles/1과 같이 전 세계 개발자들이 사용하는 REST 아키텍처를 염두에 두고 개발해야 한다.



<br>

## 1. REST 핵심 구성요소

- URI (자원)
- HTTP Method (행위)
- Reoresentations (표현)

<br>

## 2. REST API 디자인 가이드

- **URI는 정보의 자원을 표현해야 한다.**

  ```bash
  # URI는 자원을 표현하는데 중점을 둔다. 따라서, show, read와 같은 행위에 대한 표현이 들어가서는 안된다.
  GET /articles/show/1 (X)
  GET /articles/1 (O)
  ```

  <br>

- 자원에 대한 행위는 HTTP Method로 표현한다.

  ```bash
  # GET Method는 리소스 생성/삭제 등의 행위에는 어울리지 않는다.
  GET /articles/1/update (X)
  PUT /articles/1 (O)
  ```

  <br>

- **BUT!** Django 에서는 PUT, DELETE와 같은 비공식적 요청을 default로 지원하지 않고 있기 때문에 어느 정도의 절충안이 필요하다.

  ```bash
  GET /articles/1/update/ # 사용자에게 수정 페이지를 보여준다.
  POST /articles/1/update/ # 수정 작업 수행한다.
  ```

  <br>



- 설정한 url 들을 볼 수 있다. 

  ```bash
  $ python manage.py show_urls
  ```

  <br>

  ![1572843023632](https://user-images.githubusercontent.com/39547788/68100456-725e0c00-ff0b-11e9-97d0-373f64b10a15.png)

<br>



## 3. URL을 RESTful하게 변경하기

### 3.1 urls.py

- 기존의 urls.py

  ```python 
  from django.urls import path
  from . import views
  
  app_name='articles'
  urlpatterns = [
      path('<int:article_pk>/update/', views.update, name='update'), # UODATE Logic - 폼 전달
      path('<int:article_pk>/edit/', views.edit, name='edit'), # UODATE Logic - 폼 전달
      path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic 
      path('<int:article_pk>/', views.detail, name='detail'), # READ Logic - Detail
      path('new/', views.new, name='new'), # CREATE Logic - 데이터 베이스에 저장
      path('create/', views.create, name='create'), # CREATE Logic - 사용자에게 폼 전달
      path('', views.index, name='index'), # READ Logic - Index
  
  ]
  
  ```

  <br>

- 변경

  ```python 
  from django.urls import path
  from . import views
  
  app_name='articles'
  urlpatterns = [
      path('<int:article_pk>/update/', views.update, name='update'), # GET (edit) / POST (update)
      path('<int:article_pk>/delete/', views.delete, name='delete'), # DELETE Logic 
      path('<int:article_pk>/', views.detail, name='detail'), # READ Logic - Detail
      path('create/', views.create, name='create'), # GET (new) / POST (create)
      path('', views.index, name='index'), # READ Logic - Index
  
  ]
  
  ```

<br>



### 3.2 views.py

#### 3.2.1 [create]

- create - GET / POST

  - 기존의 views.py

    ```python 
    from django.shortcuts import render, redirect
    from .models import Article
    
    # 사용자에게 게시글 작성 폼을 보여주는 함수
    def new(request):
        return render(request, 'articles/new.html')
    
    # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
    def create(request):
    
        # POST 방식으로 사용자가 입력한 데이터를 받는다.
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
       
        article_pk = article.pk
        return redirect('articles:detail', article_pk) # 2 URL Namespace
    ```

    <br>

  - RESTful 변경된 views.py

    ```python 
    # 사용자에게 게시글 작성 폼을 보여주는 함수
    # def new(request):
    #     return render(request, 'articles/new.html')
    
    # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
    def create(request):
    
        # POST 요청 -> 게시글 생성 로직 수행
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            article = Article(title=title, content=content)
            article.save()    
            article_pk = article.pk
            return redirect('articles:detail', article_pk) # 2 URL Namespace
    
        # GET 요청 -> 사용자에게 폼 보여주기
        else :
            return render(request, 'articles/new.html')
    ```

    <br>

- index.html

  - `new` -> `create` 

  ```django
  {% extends 'base.html' %}
  
  {% block body %}
    <h1 class="text-center">Articles</h1>
  
    <hr>
      <a href="{% url 'articles:create' %}">[NEW]</a>
    <hr>
  
    {% for article in articles %}
      <p>[{{article.pk}}] : {{article.title}}</p>
      <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
  
    <hr>
    
    {% endfor %}
    <hr>
  
  {% endblock  %}
  ```

  <br>

- 통일을 위해 new.html을 create.html로 Rename한다.

  - create.html

    `new` -> `create` 

    ```django
    {% extends 'base.html' %}
    
    {% block body %}
    <h1 class="text-center">NEW</h1>
    
    <form action="{% url 'articles:create' %}", method="POST">
        {% csrf_token %}
        <label for="title">TITLE </label>
        <input type="text" id="title" name="title" > <br>
        <label for="content">CONTENT </label>
        <textarea type="text" id="content" name="content" cols="30" rows="10"> </textarea> <br>
    
        <input type="submit">
    </form>
    
    <hr>
    <a href="{% url 'articles:index' %}">[BACK]</a>
    
    {% endblock  %}
    ```

    <br>



#### 3.2.2 [update]

- update- GET / POST

  - 기존의 views.py

    ```python 
    from django.shortcuts import render, redirect
    from .models import Article
    
    # 게시글 수정
    def edit(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        context = {
            'article' : article
        }
    
        return render(request, 'articles/edit.html', context)
    
    # 수정된 내용을 전달 받아서 DB에 저장 (반영)
    def update(request, article_pk):
    
        # 1. 수정할 게시글 인스턴스 가져오기
        article = Article.objects.get(pk=article_pk)
    
        # 2. 폼에서 전달받은 데이터 덮어쓰기
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        
        # 3. DB 저장
        article.save()
    
        # 3. DB 저장 완료 후 게시글 detail로 이동
        # return redirect(f'/articles/{article_pk}')
        return redirect('articles:detail', article_pk)
    ```

    <br>

  - RESTful 변경된 views.py

    ```python 
    # 수정된 내용을 전달 받아서 DB에 저장 (반영)
    def update(request, article_pk):
    
        article = Article.objects.get(pk=article_pk)
    
        # POST 요청 -> DB 수정사항 반영
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            article.title = title
            article.content = content
            article.save()
    
            return redirect('articles:detail', article_pk)
    
        # GET 요청 -> 사용자에게 수정 Form 전달
        else :
            context = {
                'article' : article
            }
    
            return render(request, 'articles/update.html', context)
    ```

    <br>

- detail.html

  - `edit` -> `update`

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
  
    <a href="{% url 'articles:index' %}">[INDEX]</a>
    <a href="{% url 'articles:update' article.pk %}">[EDIT]</a>
  
    <form action="{% url 'articles:delete' article.pk%}" method="POST" style="display : inline;" onclick="return confirm('진짜 삭제할까요...?')">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
  
  
  {% endblock  %}
  ```

  <br>

- 통일을 위해 edit.html을 update.html로 Rename한다.

  - update.html

    `edit` -> `update`

    ```django
    {% extends 'base.html' %}
    
    {% block body %}
      <h1 class="text-center">EDIT</h1>
    
      <form action="{% url 'articles:update' article.pk %}", method="POST">
      {% csrf_token %}
        <label for="title">TITLE </label>
        <input type="text" id="title" name="title" value={{article.title}} > <br>
    
        <label for="content">CONTENT </label>
        <textarea type="text" id="content" name="content" cols="30" rows="10">{{article.content}} </textarea> <br>
    
        <input type="submit">
      </form>
    
      <hr>
      <!-- 상세 정보로 보내기 -->
      <a href="{% url 'articles:detail' article.pk %}">[BACK]</a>
    
    {% endblock  %}
    ```

    

































































## [DELETE] 기존의 a 태그 -> 매우 위험 (GET)

- url을 통해 delete를 하지 못하도록 변경하자

  - detail.html

    - 변경 전

      ```django
      <a href="{% url 'articles:delete' article.pk %}">[DELETE]</a>
      ```

      <br>

    - 변경 후 

      - Form 태그를 통해 POST 방식으로 전달한다.

        ```django
        <form action="{% url 'articles:delete' article.pk%}" method="POST" style="display : inline;">
            {% csrf_token %}
            <input type="submit" value="DELETE">
        </form>
        ```

        <br>

- 삭제 전, 확인 요청을 받는 코드 추가

  ```django
  <form action="{% url 'articles:delete' article.pk%}" method="POST" style="display : inline;" onclick="return confirm('진짜 삭제할까요...?')">
      {% csrf_token %}
      <input type="submit" value="DELETE">
  </form>
  ```

  

<br>