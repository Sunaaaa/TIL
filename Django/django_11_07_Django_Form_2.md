# Django Form Final

<br>

## 1. URL Resolver

> CREATE 로직과 UPDATE 로직이 같은 form.html을 공유하고 둘다 동일한 헤더가 출력되어 있다. 또 CREATE로직과 UPDATE 로직때에는 [BACK]이 index 페이지로 이동해야한다.
>
> - `URL Resolver`을 적용해 이를 해결해보자!

<br>

- 사용자가 요청한 URL과 django 내부로 들어오는 URL 사이에서 번역해주는 통역사 역할을 해준다.

  - `request.resolver_match.url_name == 'create'` : request로 들어오는 url의 이름이 'create'인지 확인

    **- *urls.py에 등록된 url의 이름을 작성한다.**

    ```django
    {% if request.resolver_match.url_name == 'create' %}
    <h1 class="text-center">CREATE</h1>
    {% else %}
    <h1 class="text-center">UPDATE</h1>
    {% endif %}
    
    {% if request.resolver_match.url_name == 'create' %}
    <a href="{% url 'articles:index' %}">[BACK : INDEX]</a>
    {% else %}
    <a href="{% url 'articles:detail' article.pk %}">[BACK : DETAIL]</a>
    {% endif %}
    ```

    <br>

  - form.html

    ```django
    {% extends 'base.html' %}
    {% load bootstrap4 %}
    {% block body %}
    
    {% if request.resolver_match.url_name == 'create' %}
    <h1 class="text-center">CREATE</h1>
    {% else %}
    <h1 class="text-center">UPDATE</h1>
    {% endif %}
    
    <hr>
    <div class="container mx-auto">
      <form action="" method="POST" class="mx-auto" style="max-width:500px;">
        {% csrf_token %}
        <div class="text-center">
          {% bootstrap_form form layout="inline" %}
          {% buttons submit='제출' reset='초기화' %}
          {% endbuttons %}
          {% comment %} <input type="submit" value="작성"> <br> {% endcomment %}
        </div>
      </form>
    </div>
    
    {% if request.resolver_match.url_name == 'create' %}
    <a href="{% url 'articles:index' %}">[BACK : INDEX]</a>
    {% else %}
    <a href="{% url 'articles:detail' article.pk %}">[BACK : DETAIL]</a>
    {% endif %}
    
    {% endblock  %}
    ```

<br>

- 실행 화면 

  - CREATE 로직

    ![1573122560306](https://user-images.githubusercontent.com/39547788/68387295-5bd0e280-01a1-11ea-93b2-3c73122cf6d7.png)

    <br>

  - UPDATE 로직

    ![1573122512214](https://user-images.githubusercontent.com/39547788/68387294-5b384c00-01a1-11ea-9434-45e5fe8b789e.png)

<br>

<br>

## 2. Django BootStrap

> [Django BootStrap](https://django-bootstrap4.readthedocs.io/en/latest/quickstart.html)

<br>

- django-bootstrap4 설치

  ```bash
  $ pip install django-bootstrap4
  ```

<br>

- INSTALLED_APPS 에 등록하기

  - settings.py 

    ```python
    INSTALLED_APPS = [
        .
        .
        
        'articles',
        'imagekit',
        'bootstrap4',
        
        .
        .
    ]
    ```

  <br>

- bootstrap을 적용할 템플릿에 반드시  `{% load bootstrap4 %}`를 적용해야한다.

  ```django
  {% bootstrap_form form layout="inline" %}
  {% buttons submit='제출' reset='초기화' %}
  {% endbuttons %}
  ```

  <br>

  <br>





## 3. Comment-ModelForm

### 3.1 Comment Model 생성

```python 
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 메타데이터 옵션 설정
    # 정렬
    class Meta:
        ordering = ['-pk',]

    # 객체 표현 방식 Customizing
    def __str__(self):
        return self.content
```



<br>

### 3.2 Comment Model Form 생성

```python 
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="댓글",
        widget=forms.Textarea(
            attrs={
                "class" : "comment",
                "placeholder" : "댓글을 달아보세요~",
                'rows' : 1,
                'cols' : 30,

            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)
```

<br>

- Comment Form 실행 화면

  ![1573127312497](https://user-images.githubusercontent.com/39547788/68387296-5bd0e280-01a1-11ea-9f5e-731508613073.png)



<br>

### 3.3 admin.py  등록

```python 
from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display=('pk', 'article', 'content', 'created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)
```



<br>

<br>

## 4. View Decorators

> Django가 제공하는 decorator 활용하기

<br>

### 4.1 require_POST

- view 함수가 POST 메서드 요청만 승인하도록 하는 Decorator
- 일치하지 않는 요청이면 405 Method Not Allowed 에러 발생시킴

- require_POST import 하기

  ```python 
  from django.views.decorators.http import require_POST
  ```

<br>

### 4.2 require_POST 사용하기

- delete view 함수로 들어올 때 `@require_POST`가 붙는다.

  - 만약 GET 방식으로 들어오는 경우, 에러를 발생시킨다!

    - articles

      ```python 
      from django.views.decorators.http import require_POST
      
      @require_POST
      def delete(request, article_pk):
          article = get_object_or_404(Article, pk=article_pk)
          article.delete()
          return redirect('articles:index')
      ```

    - comment

      ```python 
      @require_POST
      def comments_create(request, article_pk):
          article = get_object_or_404(Article, pk=article_pk)
          
          comment_form = CommentForm(request.POST)
      
          if comment_form.is_valid():
              # save 메서드 -> 선택 인자 : (기본 값) commit=True : DB에 바로 저장
              # commit=False : DB에 바로 저장되는 것을 막아준다.
              # 객체 저장 
              comment = comment_form.save(commit=False)
              comment.article = article
              comment.save()
      
          return redirect('articles:detail', article.pk)
      
      @require_POST
      def comments_delete(request, article_pk, comment_pk):
          article = get_object_or_404(Article, pk=article_pk)
          
          comment = get_object_or_404(Comment, pk=comment_pk)
          comment.delete()    
          return redirect('articles:detail', article.pk)
      ```

      <br>

  

- 실행 화면

  - 사용자가 URL을 통해 직접 delete를 수행하려고 하면 405 에러를 발생시킨다.

    `http://127.0.0.1:8000/articles/3/delete`

    ![1573104174392](https://user-images.githubusercontent.com/39547788/68387290-5b384c00-01a1-11ea-9691-31f2f4c0a8c9.png)

    <br>

  - 사용자가 URL을 통해 직접 comments를 수행하려고 하면 405 에러를 발생시킨다.

    `http://127.0.0.1:8000/articles/2/comments`

    ![1573104714238](https://user-images.githubusercontent.com/39547788/68387292-5b384c00-01a1-11ea-9174-d854059202b0.png)





<br>

<br>

## [Beautify]

- 여러가지 언어들 Formatting 또는 코드를 정리해준다.

  ![1573087883243](../AppData/Roaming/Typora/typora-user-images/1573087883243.png)



<br>

- settings.json

  - 현재 프로젝트의 settings.json

    ![1573100072738](../AppData/Roaming/Typora/typora-user-images/1573100072738.png)
    <br>

    - settings.json 하단에 아래의 코드 추가!

      ```json
      "beautify.language": {
              "js": {
                  "type": ["javascript", "json"],
                  "filename": [".jshintrc", ".jsbeautifyrc"]
                  // "ext": ["js", "json"]
                  // ^^ to set extensions to be beautified using the javascript beautifier
              },
              "css": ["css", "scss"],
              "html": ["htm", "html", "django-html"]
          },
      ```

      <br>

      ![1573088016298](../AppData/Roaming/Typora/typora-user-images/1573088016298.png)

      <br>