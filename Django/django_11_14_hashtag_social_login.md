# 1. Hashtag

> **해시태그**(영어: hashtag)는 소셜 네트워크 서비스(SNS) 등에서 사용되는 기호로, **해시** 기호(#) 뒤에 특정 단어를 쓰면 그 단어에 대한 글을 모아 분류해서 볼 수 있다.

<br>

### 1.1 Model 생성

#### [ articles Application ]

- models.py

  - `unique = True`

    - True 인 경우, 필드는 테이블 전체에서 고유한 값이어야 한다.
    - 유효성 검사 단계에서 실행되면, 중복 값이 있는 모델을 저장하려고 하면, `.save()`메서드로 인해서 에러가 발생한다.

  - `hashtags = models.ManyToManyField(Hashtag, blank=True)` 필드 추가

    ```python 
    class Hashtag(models.Model):
        # 해쉬태그가 없어도 게시글이 작성될 수 있도록 blank=True 옵션 
        content = models.TextField(blank=True)
        
    class Article(models.Model):
        title = models.CharField(max_length=40)
        content = models.TextField()
    
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
        hashtags = models.ManyToManyField(Hashtag, blank=True)
    
        # 객체 표시 형식 수정
        def __str__(self):
            return f'[{self.title}] {self.content}'
    ```

- migrate

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  - sqlite3로 테이블 생성 확인

    ![1573698921703](Hashtag.assets/1573698921703.png)

<br>

### 1.2 해쉬 태그 처리 

> 사용자가 작성한 게시글 (title / content)에서 `#`로 시작하는 단어 (해쉬태그)만 뽑아서 해쉬태그로 저장해야 한다. 
>
> 리스트 반복문을 돌려서 앞자리가 '#'으로 시작하는 단어를 해시태그 테이블에 등록한다. 또 동시에 해당 게시글 해시태그 목록에 추가한다.
>
> - content = "폴킴 #짱 #명곡 #감성"
>
>   - `.split(' ')`
>
>     `content_list = ['폴킴', '#짱', '#명곡', '#감성']`
>
>     `article.hashtags.add(word)`
>
> - content = "폴킴 #짱 #짱 #명곡 #감성"
>
>   - content_list = ['폴킴', '#짱', '#짱', '#명곡', '#감성']
>
>     **문제 발생!!** `unique=True`이기 때문에, `#짱`이 이미 존재 -> 에러 발생
>
>     **해결!!** `get_or_create()`
>
>     - word와 같은 해시태그를 찾고 있으면 기존 객체를 `hashtag`반환한다.
>
>       만약, 없는 경우 새로운 객체를 생성한다.
>
>     - `hashtag, created = Hashtag.objects.get_or_create(content=word)`
>
>       - 기존 객체가 반환 되면 `created = True`
>       - 새로운 객체가 생성되면 `created = False`

<br>

- views.py

  - create 로직 수정

    - `article.content.split()` : 게시글 내용을 잘라서 리스트로 만든다.

    - `word.startswith('#')` : word가 '#'으로 시작하는지 확인한다.

      - '#'로 시작하면 해시태그 등록!

        - 만약, 기존에 있던 해시태그면 기존의 객체를 `hashtag`로 반환한다.

        - 새로운 해시태그면 새로운 객체를 생성하여 해당 게시글의 해시태그 목록에 추가한다.

          ```python 
          @login_required
          def create(request):
              if request.method=="POST":
                  form = ArticleForm(request.POST)
                  
                  # 유효성 검증
                  if form.is_valid():
                      article = form.save(commit=False)
                      article.user = request.user
                      article.save()
          
                      # hashtag
                      for word in article.content.split():
                          if word.startswith('#'):
                              hashtag, created = Hashtag.objects.get_or_create(content=word)
                              article.hashtags.add(hashtag)
          
                      return redirect('articles:detail', article.pk)
              
              else :
                  form = ArticleForm()
              context = {
                  'form' : form
              }
              return render(request, 'articles/form.html', context)
          
          ```

  <br>

  - update 로직 수정

    - `article.hashtags.clear()` : 해당 게시글의 해시태그 목록을 비운다.

      ```python 
      @login_required
      def update(request, article_pk):
          article = get_object_or_404(Article, pk=article_pk)
          if request.user == article.user:
      
              if request.method == 'POST':
                  form = ArticleForm(request.POST, instance=article)
      
                  if form.is_valid():
                      article = form.save()
      
                      # hashtag
                      article.hashtags.clear()
                      for word in article.content.split():
                          if word.startswith('#'):
                              hashtag, created = Hashtag.objects.get_or_create(content=word)
                              article.hashtags.add(hashtag)
      
      
                              return redirect('articles:detail', article_pk)
      
                          else :
                              form = ArticleForm(instance=article)
      
                              else:
                                  return redirect('articles:detail' , article_pk)
                              context = {
                                  'form' : form,
                                  'article' : article,
                              }
                              return render(request, 'articles/form.html', context)
      
      ```

    - 실행 화면

      - '#빵'을 추가하여 게시글을 수정한다.

        ![1573696306678](Hashtag.assets/1573696306678.png)

        <br>

      - sqlite3를 통해 해시태그가 등록된 것을 확인한다.

        ![1573696334981](Hashtag.assets/1573696334981.png)

        <br>

      - 만약, '#행복', '#감성'을 모두 지우면 게시글과 해시태그 관계를 나타내는 테이블에서 해당 데이터가 삭제되는 것을 확인할 수 있다. 

        - '#행복', '#감성' 지우기

          ![1573696428154](Hashtag.assets/1573696428154.png)

          <br>

        - sqlite3로 확인하기

          ![1573696448379](Hashtag.assets/1573696448379.png)

<br>



### 1.3 해시태그 글 모아보기

> 특정 해시태그 (예> '#빵')가 들어있는 게시글을 모아보자!

<br>

- views.py

  ```python 
  def hashtag(request, hash_pk):
      # 해시 태그 가져오기
      hashtag = get_object_or_404(Hashtag, pk=hash_pk)
  
      # 해당 해시태그를 참조하는 게시글을 가져오기
      articles = hashtag.article_set.order_by('-pk')
      context = {
          'hashtag' : hashtag,
          'articles' : articles,
      }
  
      return render(request, 'articles/hashtag.html', context)
  
  ```

  <br>

- hashtag.html

  - `{{article.comment_set.all|length}}` : 게시글에 등록된 댓글 수 

  - `{{article.like_users.all|length}}` : 게시글을 좋아하는 User의 수 

    ```django
    {% extends 'base.html' %}
    
    {% block body %}
    
    <h1> {{hashtag.content}} 글 모아보기 </h1>
    
    <h3> {{articles|length}} 개의 글이 있습니다. </h3>
    {% for article in articles %}
    <div class="container">
      <p>글 제목 : {{article.title}} </p>
      <p>글 내용 : {{article.content}} </p>
      <p> {{article.comment_set.all|length}} 개의 댓글이 있습니다.  </p>
      <p> {{article.like_users.all|length}}명이 이 글을 좋아합니다. </p>
    </div>
      <hr>
      
    {% endfor %}
    
    {% endblock  %}
    ```

<br>

- urls.py

  ```python 
  from django.urls import path
  from . import views
  
  app_name="articles"
  urlpatterns = [
      .
      .
      .
      path('<int:hash_pk>/hashtag/', views.hashtag, name="hashtag"),
  ]
  
  ```

<br>

- 실행 화면

  ![1573697453466](Hashtag.assets/1573697453466.png)





### 1.4 해시태그에 a태그 붙이기

- templatetags 폴더 / make_link.py 생성

  - 링크를 만들어 주는 사용자 정의 템플릿태그를 만들어준다.

    **서버를 껐다 켜야 반영됨!**

<br>

- make_link.py

  - ` f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a> '` : </a> 뒤에 띄어쓰기를 추가해줘야 한다.

  - `content = article.content + ' '`

    - 만약 게시글의 끝이 '#빵 '이 아닌 '#빵'으로 해시태그가 되어있는 경우를 대비하여 ' '를 붙여준다.

      ```python 
      from django import template
      
      register = template.Library()
      
      @register.filter
      def hashtag_link(article):
          content = article.content + ' '
          hashtags = article.hashtags.all()
      
          for hashtag in hashtags:
              content = content.replace(
                  hashtag.content + ' ', f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a> '
              )
      
          return content
      ```

<br>

- detail.html

  - `{% load make_link %}`과  `{{article|hashtag_link}}` 를 통해 게시글의 내용 중 해시태그를 찾아 a 태그를 적용한다.

  ```django
  {% extends 'base.html' %}
  
  {% load make_link %}
  
  {% block body %}
  {% include 'articles/_follow.html' %}
  {% load bootstrap4 %}
  <div class="container">
    <h2>{{article.title}}</h2>
    <div class="text-align mt-4">
      <p>내용  :  {{article|hashtag_link}}</p>
      <p>최초 업로드 날짜  :  {{article.created_at}}</p>
      <p>최종 수정 날짜  :  {{article.updated_at}}</p>
    </div>
  
  ```

- 실행 화면

  ![1573698218224](Hashtag.assets/1573698218224.png)

  <br>

### 1.5 Django Template Filter : safe

> [Django Template Filter](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/)를 사용하자!

<br>

- `safe`를 추가

  - 내장 필터인 safe 필터를 사용하여, **tag escape를 방지**할 수 있다.

  - 실행 화면

    - a 태그가 잘 적용되어 나오는 것을 확인할 수 있다. 

      ![1573698288150](Hashtag.assets/1573698288150.png)

  <br>





# 2. Social Login

> 인증, 계정, 등록 등을 다루는 여러가지 방법이 존재하는데, 우리는 **`django-allauth` 라는 라이브러리를 사용해서 손쉽게 Social Login을 구현할 수 있다.**
>
> [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) 따라가자

<br>

[config]

### 2.1 사전 준비

[django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) 따라가자

```bash
$ pip install django-allauth
```

- settings.py

  - 아래의 코드로 작성

    ```python 
    AUTHENTICATION_BACKENDS = (
    
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',
    
    )
    
    INSTALLED_APPS = (
        ...
        # The following apps are required:
        'django.contrib.auth',
        'django.contrib.messages',
        'django.contrib.sites',
    
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        
        'allauth.socialaccount.providers.kakao',
    )
    
    SITE_ID = 1
    ```

  <br>

- config/ urls.py

  - `path('acounts/', include('allauth.urls')),`

    ```python 
    urlpatterns = [
        path('acounts/', include('acounts.urls')),
        path('acounts/', include('allauth.urls')),
        path('articles/', include('articles.urls')),
        path('admin/', admin.site.urls),
    ]
    ```

  <br>

- migrate

  ```bash
  $ python manage.py makemigrations
  No changes detected
  
  $ python manage.py migrate
  ```

  

<br>



### 2.2 Kakao Developers OAuth 등록

#### 2.2.1 KaKao Developers

- 새로운 App 등록

- 플랫폼 [웹] 추가

  ![1573714222436](../../../Documents/Hashtag.assets/1573714222436.png)

  <br>

- 사이트 도메인 작성 

  ```python 
  http://127.0.0.1:8000
  https://127.0.0.1:8000
  ```

  ![1573714283650](../../../Documents/Hashtag.assets/1573714283650.png)

  <br>

  ![1573714304733](../../../Documents/Hashtag.assets/1573714304733.png)

  <br>

- 로그인 동의항목 설정

  ![1573714373954](../../../Documents/Hashtag.assets/1573714373954.png)

  <br>

- 사용자 관리 활성화 

  - 카카오 계정으로 로그인 및 API 사용을 위해 사용자 관리를 활성화 한다.

    ![1573714474220](../../../Documents/Hashtag.assets/1573714474220.png)

    <br>

- Client Secret 비밀키 발급

  - REST API로 토큰 발급 시 보안을 강화하기 위해 Client Secret을 사용할 수 있다. 

  - [고급 설정] -> 코드 발급

    ![1573714558574](../../../Documents/Hashtag.assets/1573714558574.png)

    <br>

  - Client Secret 활성화

    ![1573714583253](../../../Documents/Hashtag.assets/1573714583253.png)

    <br>

#### 2.2.2 admin 페이지

- 소셜 어플리케이션 추가

  ![1573714638508](../../../Documents/Hashtag.assets/1573714638508.png)

  <br>

- 소셜 어플리케이션 추가 폼 작성 후 저장

  ![1573714665529](../../../Documents/Hashtag.assets/1573714665529.png)

  <br>

- 소셜 계정 등록 완료

  ![1573714758367](../../../Documents/Hashtag.assets/1573714758367.png)

  <br>



### 2.3 카카오 로그인 연결

- social_login.html

  - acount_form.html 대신 '카카오 로그인' 버튼이 있는 템플릿을 생성한다. 

    ```django
    {% extends 'base.html' %}
    {% load bootstrap4 %}
    {% load socialaccount %}
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
        <a href="{% provider_login_url 'kakao' %} ">카카오 로그인</a>
    </form>
    
    {% endblock  %}
    ```

    <br>

- views.py

  - 템플릿을 acounts/acount_form.html에서 acounts/social_login.html으로 변경한다.

    ```python 
    def login(request):
    
        if request.user.is_authenticated:
            return redirect('articles:index')
    
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect(request.GET.get('next') or 'articles:index')
        else : 
            form = AuthenticationForm()
    
        context = {
            'form' : form,
        } 
    
        return render(request, 'acounts/social_login.html', context)
    ```

  <br>

- 실행 화면

  - 로그인 버튼

    ![1573709346262](../../../Documents/Hashtag.assets/1573709346262.png)

    <br>

  - 카카오 로그인 버튼 클릭

    - 카카오에 로그인이 되어 있는 경우

      ![1573709373302](../../../Documents/Hashtag.assets/1573709373302.png)

      <br>

    - 카카오에 로그인이 되어있지 않은 경우

      ![1573713647897](../../../Documents/Hashtag.assets/1573713647897.png)

      

<br>

**문제 발생!!**

- 로그인을 하면 에러 발생 

  ![1573709431232](../../../Documents/Hashtag.assets/1573709431232.png)

<br>

**해결!!**

- 로그인 후 redirect 경로를 커스터마이징 한다.

  - settings.py

    ```python 
    # 로그인 후 리다이렉트 경로
    LOGIN_REDIRECT_URL = 'articles:index'
    ```

    <br>

- 실행 화면

  - 카카오 계정으로 로그인 성공!!!

    ![1573714841723](../../../Documents/Hashtag.assets/1573714841723.png)

    <br>

  - 나의 카카오 계정 이메일 주소 확인!

    ![1573714927069](../../../Documents/Hashtag.assets/1573714927069.png)

    <br>


  

