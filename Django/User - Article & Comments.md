# User - Article & Comments

> django가 프로젝트를 실행 시키면, `INSTALLED_APPS` Application을 들고 오고, 각 Application에 해당하는 model들을 import한다. 그래서 import 한 뒤에 사용 할 수 있다. 
>
> - 만약, User를 사용해서 정의한다 했을 때 import 되지 않았을 때 사용해야하는 경우가 발생한다. 
>   - `get_user_model()` 
>     - 클래스의 모델이 먼저 import 될 수 있도록 해야 한다. 
>   - `settings.AUTH_USER_MODEL`
>     - 순서의 영향을 받지 않기 때문에 모델 정의할 때 사용하도록 한다. 

<br>

- User 클래스 가져오는 법

  - settings.AUTH_USER_MODEL

    - return str

    - models.py 에서 모델 정의할 때만 사용한다.

      ```python 
      from django.conf import settings
      settings.AUTH_USER_MODEL
      ```

  - get_user_model()

    - return Class

    - models.py 제외한 모든 곳

      ```
      
      ```



<br>

<br>



# User Article

## 게시글 작성자 정보 넣기 [ CREATE ]

#### [ articles Application ]

- 모델 정의

  - 게시글 작성자에 대한 정보를 넣기 위해 Article 클래스에 User 클래스를 외래키로 설정한다.

    ```python 
    from django.conf import settings
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ```

  - models.py

    ```python 
    from django.db import models
    from imagekit.models import ProcessedImageField
    from imagekit.processors import Thumbnail
    from django.conf import settings
    
    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=40)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
        # 객체 표시 형식 수정
        def __str__(self):
            return f'[{self.title}] {self.content}'
    ```

    <br>



- 마이그레이션

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  <br>

- user 외래키 설정 확인

  ![1573520368647](User%20-%20Article%20&%20Comments.assets/1573520368647.png)

  <br>

- 새로운 게시글을 작성할 때 작성자에 대한 정보를 넣는 로직을 추가한다.
  - views.py
    - article이 바로 저장되지 않도록 `article = form.save(commit=False)`를 설정한다.

    - `request.user`를 이용해 게시글 작성자를 설정한 뒤, `article.save()`를 통해 새로운 게시글을 등록한다. 

      ```python  
      @login_required
      def create(request):
          if request.method=="POST":
              form = ArticleForm(request.POST)
      
      		if form.is_valid():
                  article = form.save(commit=False)
                  article.user = request.user
                  article.save()
      
                  return redirect('articles:detail', article.pk)
          
          else :
              form = ArticleForm()
          context = {
              'form' : form
          }
          return render(request, 'articles/form.html', context)
      ```

      

- 실행 화면

  - index.html

    ![1573520089171](User%20-%20Article%20&%20Comments.assets/1573520089171.png)

  - sqlite3

    ![1573520358825](User%20-%20Article%20&%20Comments.assets/1573520358825.png)





## 게시글 수정 제한 [ UPDATE ]

> 게시글 작성자가 아니면 수정이 불가능하도록 로직을 변경해보자!

<br>

- 이렇게만 하면 URL을 통해 접근 가능 -> 아예 view함수에서 막아보자

```
{% extends 'base.html' %}
{% block body %}
{% load bootstrap4 %}

<div class="container">
  <h2>{{article.title}}</h2>
  <div class="text-align mt-4">
    <p>내용  :  {{article.content}}</p>
    <p>최초 업로드 날짜  :  {{article.created_at}}</p>
    <p>최종 수정 날짜  :  {{article.updated_at}}</p>
  </div>

    <a class="ml-auto btn btn-dark"  href="{% url 'articles:index' %}">[INDEX]</a>
  {% if request.user == article.user  %}
    <a class="ml-auto btn btn-dark"  href="{% url 'articles:update' article.pk %}">[EDIT]</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST" style="display : inline;" onclick="return confirm('진짜 삭제할까요...?')">
      {% csrf_token %}
      <input class="ml-auto btn btn-dark"  type="submit" value="DELETE">
    </form>  
  {% endif %}

</div>


<hr>

<form action="{% url 'articles:comments_create' article.pk %}" method="POST" style=" max-width:500px;">
  {% comment %} {{comment_form}} {% endcomment %}
  {% csrf_token %}
  {% bootstrap_form comment_form layout="horizontal" %}
  {% buttons submit='댓글 작성' layout="inline" %}
  {% endbuttons %}
</form>
<hr>
<p><b>댓글 목록({{comments|length}}개)</b></p>
<hr>
{% for comment in comments  %}
  <p ">[{{forloop.revcounter}} 번 댓글]  {{comment.content}}</p>
  <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" style="display:inline; max-width:500px;">
    {% csrf_token %}
    {% buttons submit='삭제' layout="inline" %}
    {% endbuttons %}
  </form>
{% endfor %}

{% endblock  %}
```





- 수정 

  ```
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
  ```







## 게시글 삭제 제한 [ DELETE ]

> 게시글 작성자가 아니면 삭제가 불가능하도록 로직을 변경해보자!

삭제도 구현해보자

```
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
```





## User Comment

> comment 가 어떤 User의 것인지를 보이도록 로직을 변경해보자!
>
> Comment 는 Article 과 User 정보 2개를 갖는 **이중 1:N 관계 이다. **

<br>

## Comment 작성자 정보 넣기 [ CREATE ]

#### [ articles Application ]

- 모델 정의

  - 게시글 작성자에 대한 정보를 넣기 위해 Article 클래스에 User 클래스를 외래키로 설정한다.

    ```python 
    from django.conf import settings
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ```

  - models.py

    ```python 
    from django.db import models
    from imagekit.models import ProcessedImageField
    from imagekit.processors import Thumbnail
    from django.conf import settings
    
    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=40)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
        # 객체 표시 형식 수정
        def __str__(self):
            return f'[{self.title}] {self.content}'
    ```

    <br>



- 마이그레이션

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  <br>

- user 외래키 설정 확인

  ![1573522182970](User%20-%20Article%20&%20Comments.assets/1573522182970.png)

  <br>

  ![1573522241420](User%20-%20Article%20&%20Comments.assets/1573522241420.png)

  <br>

- 새로운 게시글을 작성할 때 작성자에 대한 정보를 넣는 로직 `comment.user = request.user` 을 추가한다.
  - views.py

    - comment가 바로 저장되지 않도록 `comment = form.save(commit=False)`를 설정한다.

    - `request.user`를 이용해 게시글 작성자를 설정한 뒤, `article.save()`를 통해 새로운 게시글을 등록한다. 

      ```python 
      @require_POST
      def comments_create(request, article_pk):
          article = get_object_or_404(Article, pk=article_pk)
          if request.user.is_authenticated:
              
              comment_form = CommentForm(request.POST)
      
              if comment_form.is_valid():
                  comment = comment_form.save(commit=False)
                  comment.article = article
                  comment.user = request.user
                  comment.save()
      
          return redirect('articles:detail', article_pk)
      
      ```



<br>

### [ comment user & article 저장 방법 ]

1. ##### 인스턴스 그대로 넣기

   ```python
   @require_POST
   def comments_create(request, article_pk):
       article = get_object_or_404(Article, pk=article_pk)
       if request.user.is_authenticated:
           
           comment_form = CommentForm(request.POST)
   
           if comment_form.is_valid():
               comment = comment_form.save(commit=False)
               comment.article = article
               comment.user = request.user
               comment.save()
   
       return redirect('articles:detail', article.pk)
   ```

   <br>

2. ##### 데이터 베이스에 저장되어 있는 형식에 맞춰넣기

   - 인스턴스를 가져오는 `article = get_object_or_404(Article, pk=article_pk)`를 작성하지 않아도 된다. 

     ```python 
     @require_POST
     def comments_create(request, article_pk):
         if request.user.is_authenticated:
             
             comment_form = CommentForm(request.POST)
     
             if comment_form.is_valid():
                 comment = comment_form.save(commit=False)
                 comment.article_id = article_pk
                 comment.user = request.user
                 comment.save()
     
         return redirect('articles:detail', article_pk)
     ```

     

<br><br>

## 게시글 수정 제한 [ UPDATE ]







<br><br>

## Comment 삭제 제한 [ DELETE ]

> 본인이 작성한 comment만 삭제할 수 있도록 로직을 변경해보자!

<br>

- views.py

  - 로그인한 사용자와 댓글 작성자가 같을 경우 삭제를 수행한다.

    - `request.user == comment.user:`

      ```python 
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
      ```

      <br>

- detail.html

  - `{% if coment.user == request.user %}`를 추가하여 comment 작성자인 경우에만 삭제 버튼을 보이도록 한다.

    ```django
    {% extends 'base.html' %}
    {% block body %}
    {% load bootstrap4 %}
    
    <hr>
    
    <p><b>댓글 목록({{comments|length}}개)</b></p>
    <hr>
    {% for coment in comments  %}
    
      <p>[{{forloop.revcounter}} 번 댓글]  {{coment.content}}</p>
      
      {% if coment.user == request.user %}
    
      <form action="{% url 'articles:comments_delete' article.pk coment.pk %}"  method="POST" style="display:inline; max-width:500px;">
        {% csrf_token %}
        {% buttons submit='삭제' layout="inline" %}
        {% endbuttons %}
      </form>
      {% endif %}
    {% endfor %}
    
    {% endblock  %}
    ```

  