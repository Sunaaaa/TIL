# Static File

- static files 기본 경로

  - 기본적으로 애플리케이션 안에 있는 `static` 디렉토리를 탐색해서 정적파일을 가져온다.

  <br>

- `{% load  static %}`

  - 해당 페이지에 정적 파일들을 불러와서 사용하겠다고 선언한다.

  - 일반적으로는 HTML 문서 상단에 위치한다.

  - 상속받는 {% extends ' [ ] ' %} 태그가 존재하면, 태그 밑에 위치한다.

    ```django
    {% extends 'base.html' %}
    {% load  static %}
    ```

    <br>

- `{% static %}`

  - 해당하는 경로에 있는 파일에 대해서 django가 접근할 수 있는 절대 URL 경로를 생성한다.

  - 실제 파일이 위치한 경로는 아니다!!!!

    - 127.0.0.0:8000**/static/**articles/images/love.jpg

      ​							[최상위 경로]

      - /static/ : 최상위 경로 

      ```python 
      # 웹 사이트에서 사용할 정적 파일의 최상위 URL 경로
      STATIC_URL = '/static/'
      ```



<br>

<br>

## 1. Static Files Customizing

> static 파일의 경로를 커스터 마이징하여 사용할 수 있다. 

<br>



### 1.1 Static 디렉토리 생성

- Application 아래에 static 폴더를 생성하여 이미지를 넣는다.

  ![1572930852904](https://user-images.githubusercontent.com/39547788/68205684-3cee1700-000e-11ea-8392-f2d55162452c.png)

- index.html에 해당 이미지를 띄운다.

  - index.html

    - `{% load  static %}`을 반드시 추가한다.

      ```django
      {% extends 'base.html' %}
      {% load  static %}
      {% block body %}
        <h1 class="text-center">Articles</h1>
        <hr>
      
        <img class="mx-auto" src="{% static 'articles/image/love.jpg' %}" alt="김선호님" style="display : block">
      
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

- 실행 화면

  - index.html

    ![1572937332629](https://user-images.githubusercontent.com/39547788/68205705-3f507100-000e-11ea-9ee3-090b1f4725e7.png)

  <br>

  - 이미지 경로 

    ![1572937701859](https://user-images.githubusercontent.com/39547788/68205707-3fe90780-000e-11ea-87fc-94cf0e11e33e.png)

    <br>



### 1.2 settings.py 수정

- 정적 파일이 위치한 경로를 설정한다.

  - 앞으로 static 파일을 찾을 때, 아래 설정한 경로에 찾아가서 탐색한다.

    - 개발 단계에서 사용 --> 실제 프로덕션 배포 단계에서는 다른 방식을 사용한다.

    - settings.py  

      ```python 
      # config/ assets 로 Application에서 사용하는 정적 파일들을 가져온다.
      STATICFILES_DIRS = [
          os.path.join(BASE_DIR, 'config', 'assets'),
      ]
      ```

    <br>



### 1.3 assets 디렉토리 생성

- config/ assets 폴더 생성한 뒤, 모든 application 의 static 디렉토리 하위 폴더 및 파일들을 가져온다. 

  ![1572937453590](https://user-images.githubusercontent.com/39547788/68205706-3f507100-000e-11ea-9299-5f5a4ff12f72.png)

  

  <br>



### 1.3 Article  Model 수정

> image 필드를 추가하기!

- 수정 전 

  ```python 
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      # 객체 표시 형식 수정
      def __str__(self):
          return f'[{self.pk}] : {self.title} '
  ```

  <br>

- **수정 후**

  - 원래 대로 라면, 새로운 필드를 추가하고 나면, makemigrations 할때, 어떤 값을 넣을 것인지 Django 가 물어본다. 기본적으로 blank = False이기 때문이다.

  - `blank=True`

    - '빈 문자열' 이 들어가도 된다. 

    - "기본값으로 어떤 것을 넣을 거냐?"라는 절차가 생략

    - 기본 값을 물어보는 절차가 생략되기 때문에, 바로 `migrate`r가 수행된다. 

      ```python 
      from django.db import models
      
      class Article(models.Model):
          title = models.CharField(max_length=40)
          content = models.TextField()
      
          # 원래 대로 라면, 새로운 필드를 추가하고 나면, makemigrations 할때, 
          # 어떤 값을 넣을 것인지 Django 가 물어본다. 기본적으로 blank = False이기 때문이다.
          # blank=True : '빈 문자열' 이 들어가도 된다.
          image = models.ImageField(blank=True)
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)
      
          # 객체 표시 형식 수정
          def __str__(self):
              return f'[{self.pk}] : {self.title} '
      ```

  <br>

- Model 수정

  - makemigrations

    ```bash
    $ python manage.py makemigrations
    ```

    ![1572932336996](https://user-images.githubusercontent.com/39547788/68205686-3cee1700-000e-11ea-8254-169b5e8a1678.png)

    <br>

  - Pillow 설치 

    ```bash
    $ pip install Pillow
    ```

    ![1572932374109](https://user-images.githubusercontent.com/39547788/68205687-3cee1700-000e-11ea-8712-155a643c336a.png)

    <br>

  - 다시 makemigrations

    ```bash
    $ python manage.py makemigrations
    ```

    ![1572932496882](https://user-images.githubusercontent.com/39547788/68205689-3d86ad80-000e-11ea-94ef-3bd6fa47bb89.png)

    <br>

  - show로 확인하기

    ```bash
    $ python manage.py showmigrations
    ```

    ![1572932564466](https://user-images.githubusercontent.com/39547788/68205690-3d86ad80-000e-11ea-9458-afc3072e1c78.png)

    <br>

  - migrate 실행

    ```bash
    $ python manage.py migrate
    ```

    ![1572932610835](https://user-images.githubusercontent.com/39547788/68205693-3d86ad80-000e-11ea-8233-c64f35154dc5.png)

    <br>

  - show로 확인하기

    ```bash
    $ python manage.py showmigrations
    ```

    ![1572932680592](https://user-images.githubusercontent.com/39547788/68205695-3e1f4400-000e-11ea-8222-188d84ef9e03.png)

    <br>

  - sqlite3로 확인

    ![1572932700428](https://user-images.githubusercontent.com/39547788/68205696-3e1f4400-000e-11ea-906d-9db2c514b47f.png)



<br>

<br>

## 2. 사용자 이미지 업로드

> 사용자로부터 이미지 업로드 받아서 데이터 베이스에 저장하기 

<br>

- views.py

  - request를 통해 Form으로 부터 이미지 파일을 받을 때 `enctype="multipart/form-data"`으로 설정한다.

    - POST로 전송되는 Text와 파일을 따로 전송한다.

      그래서 image는 POST가 아닌 **FILES** 로 찾는다.

      **`image = request.FILES.get('image')`를 통해 이미지를 저장한다.**

      ```python 
      # 사용자로부터 데이터를 받아서 DB에 저장하는 함수
      def create(request):
      
          # POST 요청 -> 게시글 생성 로직 수행
          if request.method == 'POST':
              title = request.POST.get('title')
              content = request.POST.get('content')        
              
              # POST로 전송되는 Text와 파일을 따로 전송한다.
              image = request.FILES.get('image')
              article = Article(title=title, content=content, image=image)
      
              article.save()    
              article_pk = article.pk
              return redirect('articles:detail', article_pk) # 2 URL Namespace
      
          # GET 요청 -> 사용자에게 폼 보여주기
          else :
              return render(request, 'articles/create.html')
      ```

  <br>

- create.html

  - **enctype**

    1. application/x-www-form-urlencoded
       - 기본 값
       - 모든 문자 인코딩

    2. multipart/form-data
       - 파일 형태 첨부 시 필수 사용 / 데이터를 나누어 전송한다.
       - POST로 전송되는 Text와 파일을 따로 전송한다.

    3. text/plain

       - 인코딩 X  -> 사실상 사용하지 않는다.

       <br>

       ```django
       {% extends 'base.html' %}
       
       {% block body %}
         <h1 class="text-center">NEW</h1>
         <form action="{% url 'articles:create' %}", method="POST" enctype="multipart/form-data">
         {% csrf_token %}
           <label for="title">TITLE </label>
           <input type="text" id="title" name="title" > <br>
           <label for="content">CONTENT </label>
           <textarea type="text" id="content" name="content" cols="30" rows="10"> </textarea> <br>
       
           <input for="image"></label>
           <input type="file" name="image" id="image" accept="image/*" ><br>
       
           <input type="submit">
         </form>
       
         <hr>
         <a href="{% url 'articles:index' %}">[BACK]</a>
       
       {% endblock  %}
       ```

       <br>

- admin 페이지에서 확인하기

  - admin.py

    ```python 
    from django.contrib import admin
    from .models import Article
    from .models import Comment
    
    # Register your models here.
    
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title', 'content', 'image', 'created_at', 'updated_at',)
    
    class CommentAdmin(admin.ModelAdmin):
        list_display = ('pk', 'content', 'created_at', 'updated_at',)
    
    admin.site.register(Article, ArticleAdmin)
    admin.site.register(Comment, CommentAdmin)
    
    ```

    <br>

    - 이미지 저장 확인!

      ![1572933897198](https://user-images.githubusercontent.com/39547788/68205698-3e1f4400-000e-11ea-80c7-8640bef440c8.png)

      <br>

  - 이미지 업로드 실행 화면

    - create.html

      ![1572935552536](https://user-images.githubusercontent.com/39547788/68205700-3eb7da80-000e-11ea-9da2-c7c7ffc15955.png)

      <br>

    - [**문제점**] 이미지가 제대로 나오지 않는다.

      ![1572934763557](https://user-images.githubusercontent.com/39547788/68205699-3eb7da80-000e-11ea-886a-9d8f4e1b4a77.png)

    - 이미지 저장되는 위치

      ![1572935696184](https://user-images.githubusercontent.com/39547788/68205701-3eb7da80-000e-11ea-9b0c-e4fefb5dae1f.png)

      <br>



<br>

## 3. 업로드 이미지 파일 저장 위치 Customizing

> 업로드된 이미지 파일이 저장되는 위치도 커스터마이징해서 사용할 수 있다. 

<br>

- settings.py 수정

  - `MEDIA_URL` : 업로드된 파일의 주소를 만들어 주는 역할

  - MEDIA_ROOT : 실제로 파일이 업로드 된 다음에 어디로 배치가 될지

    ```python 
    # Media Files
    MEDIA_URL = '/media'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

    <br>

- config/ urls.py

  - `static()`

    - 첫 번째 인자 : 어떤 URL을 정적으로 추가할 지 (Media file)

    - 두 번째 인자 : 실제 해당 미디어 파일은 어디에 있는지?

      ```python 
      # settings 불러오기
      from django.conf import settings
      # static() 불러오기
      from django.conf.urls.static import static
      
      urlpatterns = [
          path('jobs/', include('jobs.urls') ),
          path('articles/', include('articles.urls') ),
          path('students/', include('students.urls') ),
          path('admin/', admin.site.urls),
      ]
      
      # static()
      urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
      
      ```

      <br>

  - 이미지 업로드 실행 화면

    - create.html

      ![1572935972897](https://user-images.githubusercontent.com/39547788/68205703-3f507100-000e-11ea-8a43-a4d114952462.png)

      <br>

    - detail.html

      ![1572936104253](https://user-images.githubusercontent.com/39547788/68205704-3f507100-000e-11ea-8871-22f8918f45dd.png)

      <br>





<br>



## 4. 업로드 이미지 수정

> input type이 file 일 경우, value 값을 지정할 수 없다. 
>
> - 이미지 파일은 바이너리 데이터 (하나의 덩어리)로 들어가서, 텍스트를 수정하듯이 일부만 수정하는 것이 불가능하다. 
>
> 
>
> **당장의 해결 방법은?**
>
> - 새로운 사진을 덮어씌우는 방식을 사용한다.
>
>   똑같은 사진을 업로드 하도록 **유도**한다. (임시 방편)
>
>   - 사진 파일을 업데이트 페이지에 띄운다.
>
>     만약, 이미지가 없는 경우 'no_image.jpg'를 띄운다.
>
>     **이미지가 있는 경우 VS 이미지가 없는 경우**

<br>

### 4.1 이미지가 있는 경우 

> 부분 수정이 불가능하기 때문에 새로운 사진 업로드를 수행하도록 한다. 단, 기존에 사용자가 업로드 했던 이미지를 재 업로드하도록 유도하기 위해 기존의 이미지를 화면에 띄운다.

<br>

- 이미지 데이터가 있는 경우의 수정 화면

  ![1572951287441](https://user-images.githubusercontent.com/39547788/68205704-3f507100-000e-11ea-8871-22f8918f45dd.png)

  <br>

### 4.2 이미지가 없는 경우

> 샘플 이미지 (static/ image/ no_image.jpg) 를 넣어두고, 이미지 없는 게시글은 샘플 이미지가 나오도록 한다.

<br>

- no_image.jpg 이미지 파일의 아래와 같이 넣는다.

![1572950256322](https://user-images.githubusercontent.com/39547788/68205709-3fe90780-000e-11ea-9acb-e7841e59f6e6.png)

<br>

- 이미지 데이터가 없는 경우의 수정 화면

  ![1572951345393](https://user-images.githubusercontent.com/39547788/68205713-40819e00-000e-11ea-94d2-469d67bc0a62.png)

  <br>



### 4.3 이미지 수정 코드

> 이미지가 없는 게시글에 이미지를 추가해보자!

<br>

- 수정하는 Update 로직 변경

  - detail.html 내 이미지 여부 확인

    ```django
    {% if article.image %}
      <p class="mx-auto" >업로드 되어있는 사진</p>
      <img class="mx-auto" src="{{article.image.url}}" alt="{{article.image}}" style="display : block; width : 50%">
    
    {% else %}
      <p class="mx-auto" >사진이 없어요....</p>  
      <img class="mx-auto" src="{% static 'articles/image/no_image.png' %}" alt="no_image" style="display : block">
    {% endif %}
    ```

    <br>

  - update.html내 이미지 여부 확인

    ```django
    {% if article.image %}
      <p class="mx-auto" >업로드 되어있는 사진</p>
      <img class="mx-auto" src="{{article.image.url}}" alt="{{article.image}}" style="display : block;">
    
    {% else %}
      <p class="mx-auto" >사진이 없어요....</p>  
      <img class="mx-auto" src="{% static 'articles/image/no_image.png' %}" alt="no_image" style="display : block">
    {% endif %}
    ```

    <br>

  - form의 enctype 설정

    `enctype="multipart/form-data"` 설정!

    ```django
    <form action="{% url 'articles:update' article.pk %}", method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <label for="title">TITLE </label>
        <input type="text" id="title" name="title" value={{article.title}} > <br>
    
        <label for="content">CONTENT </label>
        <textarea type="text" id="content" name="content" cols="30" rows="10">{{article.content}} </textarea> <br>
    
        <input type="submit">
        <label for="image">IMAGE </label>
        <input type="file" id="image" name="image"  > <br>
    </form>
    ```

    <br>

  - views.py

    ```python 
    # 수정된 내용을 전달 받아서 DB에 저장 (반영)
    def update(request, article_pk):
    
        article = Article.objects.get(pk=article_pk)
    
        # POST 요청 -> DB 수정사항 반영
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            image = request.FILES.get('image')
    
            article.image = image
            article.title = title
            article.content = content
            article.save()
    
            return redirect('articles:detail', article_pk)
    
        # GET 요청 -> 사용자에게 수정 Form 전달
        else :
            context = {
                'article' : article,
            }
    
            return render(request, 'articles/update.html', context)
    ```

    <br>

- 실행 화면

  - 이미지가 없는 게시글

    ![1572952564897](https://user-images.githubusercontent.com/39547788/68205716-40819e00-000e-11ea-9324-b5c8b3f87eb4.png)

    <br>

  - 이미지 업로드

    - update.html

      ![1572952495626](https://user-images.githubusercontent.com/39547788/68205715-40819e00-000e-11ea-9fc0-2a55de582f40.png)

      <br>

  - 수정 완료 후 이미지 업로드 된 게시글

    - detail.html

      ![1572952675379](https://user-images.githubusercontent.com/39547788/68205717-411a3480-000e-11ea-8dee-f78f013139e1.png)

      <br>

    - sqlite3로 확인

      ![1572954741139](https://user-images.githubusercontent.com/39547788/68205683-3c558080-000e-11ea-8e3a-125b7d60c3c6.png)

      <br>

    - admin 페이지로 확인

      ![1572952965544](https://user-images.githubusercontent.com/39547788/68205718-411a3480-000e-11ea-9bd4-74a353bd5c10.png)



<br>