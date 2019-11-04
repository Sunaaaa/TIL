# 19-10-30(수)_19-10-31(목) Django CRUD 구현

 

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

  ![1572438050236](https://user-images.githubusercontent.com/39547788/67859530-37508700-fb5f-11e9-905b-7e4cf903e61e.png)

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

  - 실행 화면

    - index 페이지

      ![1572519859519](https://user-images.githubusercontent.com/39547788/67947869-e9ec1c80-fc27-11e9-8243-8f547bf3dc67.png)

      <br>

      

    - 게시글 Form 작성

      ![1572519933740](https://user-images.githubusercontent.com/39547788/67947871-e9ec1c80-fc27-11e9-8f38-865f416eb5bf.png)

      <br>

    - 작성 완료 시, create 페이지로 이동

      ![1572520602723](https://user-images.githubusercontent.com/39547788/67947877-eb1d4980-fc27-11e9-9cf3-a67431c8d920.png)

      

      <br>

    - 작성한 글 확인

      - index 페이지

        ![1572520066271](https://user-images.githubusercontent.com/39547788/67947874-ea84b300-fc27-11e9-86f3-5e6fce48fe0f.png)

        <br>

      - admin 페이지

        ![1572520109965](https://user-images.githubusercontent.com/39547788/67947875-ea84b300-fc27-11e9-8cf8-658a4c162185.png)

<br>





### 1.3 POST 요청

> 지금은 GET 요청으로 보내고 있어서 쿼리 스트링에 데이터가 노출되고 있다. 이는 우리 서버의 데이터 구조가 노출될 위험도 있고, URL 경로로만 게시글 작성이 가능하면 서버 폭파의 위험성이 증가한다.
>
> - POST 요청으로 바꾸어 HTTP body에 내용을 숨기고 작성자의 신원을 확인하는 절차를 거치도록 하자.
> - **CSRF** 를 이용해 신원을 확인한다.

<br>

- form을 통해 title과 content를 입력받는다. 입력 받은 title과 content를 실제 데이터 베이스에 저장한다.

  - new.html

    - **{% csrf_token %}**을 반.드.시. 작성하여 신원 확인을 수행하도록 한다.

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

    - `request.GET.get('title')` -> `request.POST.get('title')`

      : POST 방식의 데이터를 가져온다.

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

  <br>

  - 실행 화면

    - index 페이지

      ![1572519859519](https://user-images.githubusercontent.com/39547788/67947870-e9ec1c80-fc27-11e9-9c65-8fb1fca6379d.png)

      <br>

      

    - 게시글 Form 작성

      ![1572519933740](https://user-images.githubusercontent.com/39547788/67947871-e9ec1c80-fc27-11e9-8f38-865f416eb5bf.png)

      <br>

    - 작성 완료 시, detail 페이지로 이동

      - **URL에 게시글 정보가 보이지 않는다.**
        - HTTP body에 숨겨져 보낸다.

      ![1572519997785](https://user-images.githubusercontent.com/39547788/67947873-ea84b300-fc27-11e9-83a5-62c6bfa72ec9.png)

      <br>

    - 작성한 글 확인

      - index 페이지

        ![1572520066271](https://user-images.githubusercontent.com/39547788/67947874-ea84b300-fc27-11e9-86f3-5e6fce48fe0f.png)

        <br>

      - admin 페이지

        ![1572520109965](https://user-images.githubusercontent.com/39547788/67947875-ea84b300-fc27-11e9-8cf8-658a4c162185.png)

  <br>

  

### 1.4 redirect

> 지금은 게시글 작성 완료 후, create.html 페이지로 이동해 다소 어색한 로직이 구현되어 있다. 새 게시물 작성 후, 해당 게시글의 상세 내용을 보여주는 페이지로 이동하도록 수정해보자. 
>
> - **sqlite에 게시글 작성이 완료되면 메인 페이지로 redirect **

<br>

#### 1.4.1 pk값을 가져오는 방법

```python 
In [3]: article = Article.objects.get(pk=1)

In [4]: article
Out[4]: <Article: [1] : 첫 번째 제목 >

In [5]: article.pk
Out[5]: 1
```

<br>

- views.py

  - `article.pk`로 방금 저장한 게시글의 pk 값을 가져온다.

    ```python 
    # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
    def create(request):
        title = request.POST.get('title')
        content = request.POST.get('content')
    
        article = Article(title=title, content=content)
        article.save()
     
        article_pk = article.pk
    
        return redirect(f'/articles/{article_pk}')
    ```

  <br>

  - 실행 화면

    - 초기 index 페이지에서 게시글을 작성하는 new 페이지로 이동한 후, 새로운 게시글을 작성한다. 

      - index 페이지

        ![1572482855148](https://user-images.githubusercontent.com/39547788/67947850-e789c280-fc27-11e9-9978-4281aa72b694.png)

        <br>

      - new 페이지

        ![1572482989719](https://user-images.githubusercontent.com/39547788/67947851-e789c280-fc27-11e9-8166-95a6535d5c52.png)

        <br>

    - 작성이 완료된 후 제출 버튼을 누르면, 방금 작성한 게시글의 상세 내용을 볼 수 있는 detail 페이지로 이동한다.

      - detail 페이지

        ![1572483038927](https://user-images.githubusercontent.com/39547788/67947853-e8225900-fc27-11e9-8994-e029a334844d.png)

    

<br><br>

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

  - 실행 화면

    - index 페이지

      ![1572524178093](https://user-images.githubusercontent.com/39547788/67947929-fbcdbf80-fc27-11e9-954e-f195de346f51.png)

      <br>



### 2.2 게시글 목록 제목/상세내용 구분

> 지금은 index 페이지에서 게시글의 제목 뿐만 아니라 상세 내용까지 모두 보인다. 이제는 index 페이지 목록에는 게시글 번호와 제목만 보이고, 사용자가 링크를 클릭했을 때 게시글 상세 내용 페이지로 이동하도록 구현해보자!

<br>

- index 페이지에서 각 게시글 별 [DETAIL] 링크를 클릭하면, 해당 게시글의 상세 내용을 보여준다.

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

    <br>

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

  - 실행 화면

    - index 페이지

      ![1572520981250](../AppData/Roaming/Typora/typora-user-images/1572520981250.png)

      <br>

    - detail 페이지

      ![1572521030678](https://user-images.githubusercontent.com/39547788/67947881-eb1d4980-fc27-11e9-8f74-eaf29a111246.png)

  

<br>

<br>

## 3. UPDATE

> 사용자가 수정을 요청하면 수정하는 폼을 제공한다. 그리고 수정이 완료 되면 sqlite3에 수정된 내용을 반영한다.
>
> - 작성한 게시글을 수정
>
> <br>
>
> 게시글 수정 폼은 게시글 작성 폼과 다른 점이 있다. 
>
> - 게시글 작성 폼 
>   - 새로운 정보를 받는다. 
>   - 모든 데이터를 작성하고 수정할 수 있다.
>
>  <br>
>
> - 게시글 수정 폼 
>   - 데이터 베이스에 저장된 정보를 받는다.
>   - 몇몇 데이터만 작성하고 수정이 가능하다. 가령 게시글 작성 시간, 게시글 번호 등은 수정할 수 없다. 

<br>

- detail 페이지에서 [EDIT] 링크를 클릭하여 나타나는 게시글 수정 폼 (edit) 에서 게시글 제목과 게시글 내용을 수정한다.

  - edit 페이지에서 POST 방식으로 전달한 Form 데이터와 게시글의 pk로 게시글을 수정한다.

    - 각 인스턴스의 값을 지정한 뒤, sqlite3에 반영한다.

      - `article.save()`

    - views.py

      ```python 
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
          return redirect(f'/articles/{article_pk}') 
      ```

      <br>

    - urls.py

      ```python 
      urlpatterns = [
          path('<int:article_pk>/update/', views.update), # UPDATE Logic - 폼 전달
          path('<int:article_pk>/edit/', views.edit), # UPDATE Logic - 폼 전달
          path('<int:article_pk>/', views.detail), # READ Logic - Detail
          path('new/', views.new), # CREATE Logic - 데이터 베이스에 저장
          path('create/', views.create), # CREATE Logic - 사용자에게 폼 전달
          path('', views.index), # READ Logic - Index
      ]
      ```

      <br>

    - edit.html

      - textarea는 value가 없으므로 태그 안에 내용을 채워준다.

        ```django
        {% extends 'base.html' %}
        
        {% block body %}
          <h1 class="text-center">EDIT</h1>
        
          <form action="{% url 'articles:update' article.pk %}", method="POST">
          {% csrf_token %}
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

      <br>

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
        <a href="/articles/{{article.pk}}/edit">[EDIT]</a>
      {% endblock  %}
      ```

      <br>

  - 실행 화면

    - detail.html

      ![1572524814294](https://user-images.githubusercontent.com/39547788/67947930-fc665600-fc27-11e9-84b6-8bda8b4e1eb6.png)

      <br>

    - edit.html

      - 수정 전

        ![1572524864906](https://user-images.githubusercontent.com/39547788/67947931-fc665600-fc27-11e9-9590-094ee93e870a.png)

        <br>

      - 수정 후

        ![1572524894662](https://user-images.githubusercontent.com/39547788/67947932-fc665600-fc27-11e9-930f-cd55e9207193.png)

        <br>

    - 수정 완료 확인

      - detail.html

        ![1572525162944](https://user-images.githubusercontent.com/39547788/67947933-fc665600-fc27-11e9-8688-036dd641255f.png)

        <br>

      - sqlite3

        ![1572525216453](https://user-images.githubusercontent.com/39547788/67947934-fcfeec80-fc27-11e9-837c-a96cec6c7c29.png)

        <br>

      - 관리자 페이지

        ![1572525279791](https://user-images.githubusercontent.com/39547788/67947935-fcfeec80-fc27-11e9-9ad7-5fdb705073f3.png)

      <br>

  

<br>

<br>

## 4. DELETE

> 상세 내용을 보여주는 페이지에서 해당 게시글을 삭제 할 수 있는 기능을 추가해보자
>
> - 게시글을 삭제

<br>

- 게시글의 pk 값으로 삭제한다.

  - delete() 는 별도의 save() 를 호출하지 않아도 자동으로 sqlite에 반영이 된다. 

    - views.py

      ```python 
      # 게시글 삭제
      def delete(request, article_pk):
          article = Article.objects.get(pk=article_pk)
          article.delete()
          return redirect('/articles/')
      ```

      

    <br>

    - urls.py

      ```python 
      urlpatterns = [
          path('<int:article_pk>/delete', views.delete), # DELETE Logic 
          path('<int:article_pk>/update/', views.update), # UPDATE Logic - 폼 전달
          path('<int:article_pk>/edit/', views.edit), # UPDATE Logic - 폼 전달
          path('<int:article_pk>/', views.detail), # READ Logic - Detail
          path('new/', views.new), # CREATE Logic - 데이터 베이스에 저장
          path('create/', views.create), # CREATE Logic - 사용자에게 폼 전달
          path('', views.index), # READ Logic - Index
      
      ]
      ```

      <br>

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
        <a href="/articles/{{article.pk}}/delete/">[DELETE]</a>
      
      {% endblock  %}
      ```

      <br>

- 실행 화면

  - 14번 게시글을 삭제한다.

    - index.html

      ![1572483382866](https://user-images.githubusercontent.com/39547788/67947854-e8225900-fc27-11e9-92a3-b0e7e6a69bf7.png)

      <br>

    - detail.html

      ![1572483448406](https://user-images.githubusercontent.com/39547788/67947855-e8225900-fc27-11e9-8f82-bea0104c7c33.png)

      <br>

    - index.html

      ![1572483516728](https://user-images.githubusercontent.com/39547788/67947857-e8225900-fc27-11e9-93c8-5a48bdb7d71d.png)

      <br>



<br>

<br>

<br>

# [실습] students Application 구현하기

- students 앱을 만들어준다.
- Student 모델 클래스를 만들어준다. -> 이름,나이
  - Django Shell 으로 Student 데이터를 만들고, 관리자 페이지에서 데이터가 잘 만들어졌는지 확인해보기
  - READ 로직 1 : Index 페이지 (학생들 목록)
  - CREATE 로직 : new , create (새로운 학생 등록)
  - READ 로직 2 : Detail 페이지(학생 상세정보)
  - DELETE 로직 (학생 삭제)
  - UPDATE 로직 (학생 정보 수정)



- 실행 화면

  

## Student Model

- 학생 데이터 확인

  - sqlite3

    ![1572521396379](https://user-images.githubusercontent.com/39547788/67947884-ebb5e000-fc27-11e9-926a-0f2ea628624e.png)

    <br>

  - 관리자 페이지

    ![1572521452786](https://user-images.githubusercontent.com/39547788/67947885-ebb5e000-fc27-11e9-997c-cf8c85119c13.png)

    

<br>

## READ 

- index 페이지 (학생들 목록)

  ![1572521366955](https://user-images.githubusercontent.com/39547788/67947883-eb1d4980-fc27-11e9-84fb-b06ad1f56808.png)

  <br>





## CREATE 

- new 페이지 (학생 등록)

  ![1572521598030](https://user-images.githubusercontent.com/39547788/67947887-ebb5e000-fc27-11e9-982d-fd43e4315cfc.png)

  <br>

- 학생 등록 확인

  - sqlite3

    ![1572521703141](https://user-images.githubusercontent.com/39547788/67947890-ec4e7680-fc27-11e9-827c-abe4c5893f87.png)

    <br>

  - 관리자 페이지

    ![1572521683843](https://user-images.githubusercontent.com/39547788/67947889-ec4e7680-fc27-11e9-99c6-9cafecdc4660.png)

    <br>

  - index 페이지 (학생들 목록)

    ![1572521636179](https://user-images.githubusercontent.com/39547788/67947888-ec4e7680-fc27-11e9-948f-13ed91592a72.png)

    

    <br>



## READ 

- Detail 페이지 (학생 상세정보)

  - index 페이지

    ![1572521807282](https://user-images.githubusercontent.com/39547788/67947891-ec4e7680-fc27-11e9-9725-cd3a5a7321cb.png)

    <br>

  - detail 페이지

    ![1572521833627](https://user-images.githubusercontent.com/39547788/67947892-ece70d00-fc27-11e9-8451-49c0ce182664.png)

  <br>



## UPDATE 

- 학생 정보 수정

  - detail 페이지

    ![1572521932141](https://user-images.githubusercontent.com/39547788/67947893-ece70d00-fc27-11e9-8010-ce5b82fad5ce.png)

    <br>

  - edit 페이지

    ![1572522042533](https://user-images.githubusercontent.com/39547788/67947894-ece70d00-fc27-11e9-99db-a133cfbd2d36.png)

- 정보 수정 확인

  - detail 페이지

    ![1572522114075](https://user-images.githubusercontent.com/39547788/67947895-ed7fa380-fc27-11e9-97c5-14f5b3d554e0.png)

    <br>

  - sqlite3

    ![1572522203554](https://user-images.githubusercontent.com/39547788/67947898-ed7fa380-fc27-11e9-9b81-f2e4ff00fffe.png)

    <br>

  - 관리자 페이지

    ![1572522175543](https://user-images.githubusercontent.com/39547788/67947897-ed7fa380-fc27-11e9-9a67-2493880474ed.png)

    <br>

  - index 페이지 (학생들 목록)

    ![1572522273434](https://user-images.githubusercontent.com/39547788/67947899-ed7fa380-fc27-11e9-9b17-cc570ea3f036.png)

    <br>





## DELETE 

- 학생 (용식이) 삭제 

  - detail 페이지

    ![1572522448092](https://user-images.githubusercontent.com/39547788/67947849-e789c280-fc27-11e9-8074-a08df27b65d7.png)

    <br>

- 학생 (용식이) 삭제 확인

  - index 페이지

    ![1572522782834](https://user-images.githubusercontent.com/39547788/67947936-fcfeec80-fc27-11e9-83ef-80018d8f1a42.png)

    <br>

  - sqlite3

    ![1572522907311](https://user-images.githubusercontent.com/39547788/67947927-fbcdbf80-fc27-11e9-81fc-069d011668d3.png)

    <br>

  - 관리자 페이지

    ![1572522820484](https://user-images.githubusercontent.com/39547788/67947926-fb352900-fc27-11e9-8f0b-59374dbf6110.png)

    <br>

## 소스 코드

- models.py

  ```python 
  from django.db import models
  
  # Create your models here.
  class Student(models.Model):
      name = models.CharField(max_length=20)
      age = models.CharField(max_length=4)
  
      created_at = models.DateTimeField(auto_now_add=True)
  
      # 객체를 표시하는 형식 Customizing
      def __str__(self):
          return f'[{self.pk}] : {self.name} | {self.age}'
  ```

  <br>

- admin.py

  ```python 
  from django.contrib import admin
  
  # Register your models here.
  from .models import Student
  
  class StudentAdmin(admin.ModelAdmin):
      list_display = ('pk', 'name', 'age',)
  
  admin.site.register(Student, StudentAdmin)
  ```

  <br>

- views.py

  ```python 
  from django.shortcuts import render, redirect
  from .models import Student
  
  # Create your views here.
  def index(request):
      students = Student.objects.all()
      content = {
          'students' : students
      }
  
      return render(request, 'students/index.html', content)
  
  def new(request):
      return render(request, 'students/new.html')
  
  def create(request):
      
      name = request.POST.get('name')
      age = request.POST.get('age')
      student = Student(name=name, age=age)
      student.save()
  
      return redirect('students:index')
  
  
  def detail(request, student_pk):
      student = Student.objects.get(pk=student_pk)
      content = {
          'student' : student
      }
  
      return render(request, 'students/detail.html', content)
  
  def edit(request, student_pk):
      student = Student.objects.get(pk=student_pk)
      content = {
          'student' : student
      }
      return render(request, 'students/edit.html', content)
  
  def update(request, student_pk):
  
      student = Student.objects.get(pk=student_pk)
      student.name = request.POST.get('name')
      student.age = request.POST.get('age')
      student.save()
  
      return redirect('students:detail', student_pk)
      
  
  def delete(request, student_pk):
      student = Student.objects.get(pk=student_pk)
      student.delete()
  
      return redirect('students:index')
  ```

  <br>

- urls.py

  ```python 
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
  
  ```

  <br>

- detail.html

  ```django
  {% extends 'base.html' %}
  
  {% block body %}
    <h1 class="text-center">DETAIL</h1>
  
    <p>이름 : {{student.name}}</p>
    <p>나이 : {{student.age}}</p>
    <hr>
  
    <a href="{% url 'students:index' %}">[INDEX]</a>
    <a href="{% url 'students:edit' student.pk %}">[EDIT]</a>
    <a href="{% url 'students:delete' student.pk %}">[DELETE]</a>
  
  {% endblock  %}
  ```

  <br>

- edit.html

  ```django
  {% extends 'base.html' %}
  
  {% block body %}
    <h1 class="text-center">EDIT STUDENT</h1>
  
    <form action="{% url 'students:update' student.pk%}", method="POST">
    {% csrf_token %}
      <label for="name">NAME </label>
      <input type="text" id="name" name="name" value="{{student.name}}"> <br>
  
      <label for="age">AGE </label>
      <input type="text" id="age" name="age" value={{student.age}} > <br>
  
      <input type="submit">
    </form>
  
    <hr>
    <a href="{% url 'students:index' %}">[BACK]</a>
  
  {% endblock  %}
  ```

  <br>

- index.html

  ```django
  {% extends 'base.html' %}
  
  {% block body %}
  <h1>Students</h1>
  <a href="{% url 'students:new' %}">[NEW]</a>
  <br>
  <hr>
  {% for student in  students %}
   <p>[{{student.pk}}] : {{student.name}} 
   <a href="{% url 'students:detail' student.pk%}">[상세보기]</a> 
   </p>
    <hr>
  
  {% endfor %}
  
  {% endblock  %}
  ```

  <br>

- new.html

  ```django
  {% extends 'base.html' %}
  
  {% block body %}
    <h1 class="text-center">NEW STUDENT</h1>
  
    <form action="{% url 'students:create' %}", method="POST">
    {% csrf_token %}
      {% comment %} NAME : <input type="text" name="name" > <br> {% endcomment %}
      <label for="name">NAME </label>
      <input type="text" id="name" name="name" > <br>
      <label for="age">AGE </label>
      <input type="text" id="age" name="age" > <br>
  
      <input type="submit">
    </form>
  
    <hr>
    <a href="{% url 'students:index' %}">[BACK]</a>
  
  {% endblock  %}
  ```