# Django Form Class

## [ 사전 준비 ]

> Django Form을 적용하기 전, 이때까지 우리가 학습했던 HTML Form으로 앱을 구현해보자.

<br>

- **프로젝트 생성**

  ```
  $ mkdir 04_django_form
  $ cd 04_django_form
  ```

  ```
  $ django-admin startproject config .
  ```

  <br>

- **앱 생성**

  ```
  $ python manage.py startapp articles
  ```

  <br>

- **Article Model**

  ```python 
  from django.db import models
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      # 객체 표시 형식 수정
      def __str__(self):
          return f'[{self.title}] {self.content}'
  ```

  <br>

- **URL 설정**

  ```python 
  # config/urls.py
  
  from django.urls import path
  from . import views
  
  app_name="articles"
  urlpatterns = [
      path('', views.index, name="index"),
      path('create/', views.create, name="create"),
      path('<int:article_pk>/detail/',views.detail, name="detail")
  
  ]
  ```

  <br>

  ```python 
  # articles/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  from articles import views
  
  urlpatterns = [
      path('articles/', include('articles.urls')),
      path('admin/', admin.site.urls),
  ]
  
  ```

  <br>

- **base.html 생성** (부트스트랩 적용X)

  ```django
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Article</title>
  </head>
  <body>
    {% block body %}
    {% endblock  %}
  </body>
  </html>
  ```

  <br>

- **Index 페이지** (-> 모든 게시글 보여주기)

  ```python 
  from django.shortcuts import render, redirect
  from .models import Article
  
  # Create your views here.
  def index(request):
      articles = Article.objects.all()
      context = {
          'articles' : articles,
      }
      return render(request, 'articles/index.html', context)
  ```

  <br>

  ```django
  {% extends 'base.html' %}
  {% block body %}
    <h1>Articles</h1>
    <hr>
    <a href="{% url 'articles:create' %}">[NEW]</a>
    <hr>
    {% for article in articles %}
    <p>[{{article.title}}]  {{article.content}} </p>
    <a href="{% url 'articles:detail' article.pk %}">[MORE]</a>
    {% endfor %}
  
  
  {% endblock  %}
  ```

  <br>

- **Create 페이지**

  ```python 
  from django.shortcuts import render, redirect
  from .models import Article
  
  def create(request):
      if request.method=="POST":
          article = Article()
          article.title = request.POST.get('title')
          article.content = request.POST.get('content')
          article.save()
  
          return redirect('articles:detail', article.pk)
      
      else :
          return render(request, 'articles/create.html')
  ```

  <br>

  **잠깐!!**

  - RESTFul 하게 로직을 통합했기 때문에 
    form 에서 action을 비워두어도 자동으로 현재 경로의 POST 로 수행한다.
    action 값이 공백일 경우, 현재 위치하고 있는 주소로 요청을 보낸다. 
    폼을 던져주는 경로, DB에 저장하는 경로가 동일한 경로라면 공백으로 해도 정상적으로 작동한다. 

    <br>

  ```django
  {% block body %}
  
  <form action="" method="POST">
    {% csrf_token %}
    <label for="title" >TITLE</label>
    <input type="text" id="title" name="title"> <br>
  
    <label for="content">CONTENT </label>
    <textarea type="text" id="content" name="content" cols="30" rows="10"> </textarea> <br>
  
    <input type="submit" value="작성"> <br>
  </form>
  
  {% endblock  %}
  ```

  <br>

- **Detail 페이지**

  ```python 
  from django.shortcuts import render, redirect
  from .models import Article
  
  def detail(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      context = {
          'article' : article,
      }
      return render(request, 'articles/detail.html', context)
  
  ```

  <br>

  ```django
  {% block body %}
  <p>제목  :  {{article.title}}</p>
  <p>내용  :  {{article.content}}</p>
  <p>최초 업로드 날짜  :  {{article.created_at}}</p>
  <p>최종 수정 날짜  :  {{article.updated_at}}</p>
  
  {% endblock  %}
  ```

<br>

## 1. Django Form

> Django에서 제공하는 Form 클래스를 이용해서 편리하게 Form 정보를 관리하고, 유효성 검증을 진행하고, 비유효 field에 대한 에러 메시지를 결정한다.

<br>

### 1.1 Form 장점

**자동화**

- `blank=Ture`와 같은 옵션을 따로 지정해주지 않았다면, HTML 태그에 required 옵션을 자동으로 붙여준다.
- 기존에 `max_length`와 같은 조건을 어길 경우, 에러 메시지를 출력했는데, Django Form을 써서 에러 메시지를 출력해준다.

<br>

### 1.2 Django Form 실습

#### 1.2.1 forms.py

- forms.py를 생성한다.

  ![1573015566877](../AppData/Roaming/Typora/typora-user-images/1573015566877.png)

  <br>

  

- **Article Form Class** 정의

  - forms.py

    ```python 
    from django import forms
    
    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=40)
        content = forms.CharField()
    ```

    <br>



#### 1.2.2 views.py 로직 변경

- 바인딩 과정

  - Form 인스턴스를 생성하고, 전달받은 데이터를 채운다.

  - 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다.

    - **유효성 검증**

      - 유효성 검증이 끝난 form은 dict 형태로 뽑혀 나온다.
      - `cleaned_data` 를 통해 dict 안의 데이터를 검증한다.

    - Form으로 전달받는 형태 2가지

      1. GET 요청 -> 비어있는 Form 전달
      2. 유효성 검증 실패 -> 에러 메시지도 담겨서 Form 전달 

    - views.py

      ```python 
      def create(request):
          if request.method=="POST":
              form = ArticleForm(request.POST)
              
              embed()
              # 유효성 검증
              if form.is_valid():
                  title = form.cleaned_data.get('title')
                  content = form.cleaned_data.get('content')
                  article = Article.objects.create(title=title, content=content)
      
              return redirect('articles:detail', article.pk)
          
          else :
              form = ArticleForm()
          
          context = {
              'form' : form
          }
          return render(request, 'articles/create.html', context)
      ```

      <br>

    - create.html

      ```django
      {% block body %}
      
      <form action="" method="POST">
        {% csrf_token %}
        {% comment %} 
        {{form.as_p}}: 각각의 input 태그를 p 태그로 감싼다.
        {{form.as_table}}: 각각의 input 태그를 테이블 태그로 감싼다.
        {% endcomment %}
        {{form.as_p}}
        <input type="submit" value="작성"> <br>
      </form>
      
      {% endblock  %}
      ```

      <br>

- 실행 화면

  ![1573014238623](../AppData/Roaming/Typora/typora-user-images/1573014238623.png)



<br>



#### [ IPython ]

> 실행 도중 원하는 위치에 shell을 실행할 수 있다. 
>
> IPython을 이용해 Django Form 유효성 검증 전/후를 확인한다.

<br>

- IPython의 embed를 import 한다.

  ```python 
  from IPython import embed
  ```

  <br>

- Django Form 유효성 검증 전/후 확인

  ```python 
  In [1]: form
  Out[1]: <ArticleForm bound=True, valid=Unknown, fields=(title;content)>
  
  In [2]: type(form)
  Out[2]: articles.forms.ArticleForm
  
  In [3]: form.is_valid()
  Out[3]: True
  
  In [4]: form
  Out[4]: <ArticleForm bound=True, valid=True, fields=(title;content)>
  
  In [5]: form.cleaned_data
  Out[5]: {'title': '제목', 'content': '내용'}
  
  In [6]: type(form.cleaned_data)
  Out[6]: dict
      
  In [7]: form.cleaned_data.get('title')
  Out[7]: '제목'
  ```

  <br>

- views.py

  ```python 
  from django.shortcuts import render, redirect, get_object_or_404
  from .models import Article
  from .forms import ArticleForm
  from IPython import embed
  
  def create(request):
      if request.method=="POST":
          # Binding  과정
          # Form 인스턴스를 생성하고, 전달받은 데이터를 채운다.
          # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다.
          form = ArticleForm(request.POST)
          
          # shell_plus 열기
          embed()
          # 유효성 검증
          if form.is_valid():
          
          .
          .
          .
         
  ```

  

<br><br>

### 1.3 Django Form Customizing

> forms.py를 Customizing하여 다양한 형태의 Django Form을 구성할 수 있다. 

<br>

- [ 1 ] forms.py

  ```python 
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(
          max_length=40, 
          # HTML TAG 와 동일
          label='제목',
      )
      content = forms.CharField()
  ```

  <br>

  - 실행 화면

    ![1573018859593](../AppData/Roaming/Typora/typora-user-images/1573018859593.png)

    <br>

- [ 2 ] forms.py

  ```python 
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(
          max_length=40, 
          # HTML TAG 와 동일
          label='제목',
          widget=forms.TextInput(
              attrs={
                  'class' : 'title',
                  'placeholder' : '제목을 입력해주세요~',
              }
          )
      )
      content = forms.CharField()
  ```

  <br>

  - 실행 화면

    ![1573018956832](../AppData/Roaming/Typora/typora-user-images/1573018956832.png)

  <br>

- [ 3 ] forms.py

  ```python 
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(
          max_length=40, 
          # HTML TAG 와 동일
          label='제목',
          widget=forms.TextInput(
              attrs={
                  'class' : 'title',
                  'placeholder' : '제목을 입력해주세요~',
              }
          )
      )
      content = forms.CharField(
          label='내용',
          widget=forms.Textarea(
              attrs={
                  'class' : 'content',
                  'placeholder' : '내용을 입력해주세욥',
                  'rows' : 5,
                  'cols' : 30,
              }
          )
      )
  ```

  <br>

  - 실행 화면

    ![1573019004026](../AppData/Roaming/Typora/typora-user-images/1573019004026.png)





<br><br>

### 1.4 NOT FOUND

- get_object_or_404를 불러온다.

  ```python 
  from django.shortcuts import render, redirect, get_object_or_404
  
  def detail(request, article_pk):
      # article = Article.objects.get(pk=article_pk)
                                  # Class    / PK 값
      article = get_object_or_404(Article, pk=article_pk)
      context = {
          'article' : article,
      }
      return render(request, 'articles/detail.html', context)
  ```

  <br>

  - 실행 화면

    ![1573015428905](../AppData/Roaming/Typora/typora-user-images/1573015428905.png)

<br>





#### 1.4.1 DELETE

- detail.html

  - form 태그를 이용해 DELETE 버튼 생성

    ```django
    {% block body %}
    
    <p>제목  :  {{article.title}}</p>
    <p>내용  :  {{article.content}}</p>
    <p>최초 업로드 날짜  :  {{article.created_at}}</p>
    <p>최종 수정 날짜  :  {{article.updated_at}}</p>
    
    <a href="{% url 'articles:index' %}">[INDEX]</a>
    <a href="{% url 'articles:update' article.pk %}">[EDIT]</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      {{form.as_p}}
      <input type="submit" value="[DELETE]"> <br>
    </form>
    
    
    {% endblock  %}
    ```

  <br>

- views.py

  ```python 
  def delete(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
  
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
      else :
          return redirect('articles:detail')
  ```

  <br>



#### 1.4.2 UPDATE

- create.html

  - a 태그를 이용해 UPDATE  버튼 생성

  - **update와 create 로직에서 동일한 form을 던져주기 때문에 create.html을 랜더링한다.**

    ```django
    
    ```

  <br>

- views.py

  - 2가지 Form 형식

    1. GET 요청 -> 초기값을 Form에 넣어서 사용자에게 던져줌

    2. POST -> is_valid가 False 가 리턴되었을때, 오류 메시지를 포함해서 사용자에게 던져줌

       ```python 
       def update(request, article_pk):
           article = get_object_or_404(Article, pk=article_pk)
       
           if request.method == 'POST':
               form = ArticleForm(request.POST)
       
               if form.is_valid():
                   article.title = form.cleaned_data.get('title')
                   article.content = form.cleaned_data.get('content')
                   article.save()
                   return redirect('articles:detail', article_pk)
       
           else :
       
               form = ArticleForm(initial={
                   'title' : article.title,
                   'content' : article. content
               })
           context = {
               'form' : form,
           }
           return render(request, 'articles/create.html', context)
       ```

  

<br>

<br>

## 2. Django Model Form

### 2.1 개념

- Django의 큰 특징 중 하나
- Model 클래스 정의와 비슷하게 Form 클래스를 선언할 수 있다.

<br>

### 2.2 역할

1. HTML 입력 Form 생성 : `as_p()`, `as_table()`
2. 유효성 검증 : `is_valid()`
3. 검증 통과한 값은 딕셔너리로 제공 : `cleaned_data`

<br>

### 2.3 Django Model Form 실습

> Django Model Form 
>
> 1. Model Form 클래스를 상속받아 사용한다.
>
> 2. 메타 데이터로 Model 정보를 건네주면, ModelForm이 자동으로 field에 맞춰 input을 생성해준다.
>
>    - 메타 데이터
>
>      - 데이터의 데이터
>
>        ex > 사진 한장 -> 촬영 장비 이름, 촬영 환경 등 사진 한장에 대한 데이터

<br>

- models.py

  - `model = Article` : model은 Article이야

  - `fields = '__all__'` : Article에 있는 것 다 

  - `fields = ('title', 'content')` : Article에 있는 것 중 title과 content 만

    ```python 
    from django import forms
    from .models import Article
    
    # Django Model Form 
    # Model Form 
    class ArticleForm(forms.ModelForm):
        title = forms.CharField(
            max_length=10, 
            label='제목',
            widget=forms.TextInput(
                attrs={
                    'class' : 'title',
                    'placeholder' : '제목을 입력해주세요~',
                }
            )
        )
        content = forms.CharField(
            label='내용',
            widget=forms.Textarea(
                attrs={
                    'class' : 'content',
                    'placeholder' : '내용을 입력해주세욥',
                    'rows' : 5,
                    'cols' : 30,
                }
            )
        )
        class Meta:
            model = Article
            # fields = '__all__'
            fields = ('title', 'content')
    ```

- views.py

  - CREATE

    ```python 
    def create(request):
        if request.method=="POST":
            form = ArticleForm(request.POST)
            
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

  - UPDATE

    ```python 
    def update(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
    
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
    
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article_pk)
    
        else :
            form = ArticleForm(instance=article)
    
        context = {
            'form' : form,
        }
        # update와 create 로직에서 동일한 form을 던져주기 때문에 form.html을 랜더링한다.
        return render(request, 'articles/form.html', context)
    ```

    <br>

- form.html

  - update와 create 시에 사용하는 템플릿이기 때문에 create.html을 form.html로 변경해준다.

    ```django
    {% block body %}
    
    <form action="" method="POST">
      {% csrf_token %}
      {% comment %} 
      {{form.as_p}}: 각각의 input 태그를 p 태그로 감싼다.
      {{form.as_table}}: 각각의 input 태그를 테이블 태그로 감싼다.
      {% endcomment %}
      {{form.as_p}}
      <input type="submit" value="작성"> <br>
    </form>
    <a href="{% url 'articles:index' %}">[BACK]</a>
    
    {% endblock  %}
    ```

  <br>





- Form VS Model Form

  ```
  
  ```