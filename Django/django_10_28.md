# 10.10.28(월) : Start Django

- 보안이 우수하고 유지보수가 편리한 웹사이트를 신속하게 개발하는 하도록 도움을 주는 파이썬 웹 프레임워크
- Static Web (html 문서의 집합) 과 Dynamic Web 모두 가능
- 특징
  - Versatile (**다용도**)
  - Secure (**안전한**)
  - Scalable (**확장성** )
  - Complete (**완결성** )
  - Maintainable (**유지보수가 쉬운**)
  - Portable (**포터블한**)
- 성격
  - Opinionate : 독선적
  - UnOpinionate : 관용적, Customizing 가능
  - 다소 Opinionate 이지만, 일부 Customizing 할 수 있는 부분이 있다. 



<br><br>

## MTV 패턴

![1572230693722](https://user-images.githubusercontent.com/39547788/67676146-38997c80-f9c4-11e9-88b2-5e01c46bddbd.png)

- django에서는 MTV 패턴이라고 부르지만, 실제로는 MVC 패턴과 동일하다.
- Model
  - 데이터 베이스를 정의 (Data)
  - 데이터를 관리, 데이터베이스의 모양, 형태를 정의
- Template : 사용자가 보는 화면을 정의
- View
  - 중간 관리자
  - 사용자가 보고 있는 데이터를 가공
  - Model에 있는 데이터 베이스의 데이터를 꺼내서 가공한다.
  - @app.route() 안에 정의된 함수와 같은 역할



<br><br>

## 3 Kings Of Django

- models.py
  - 데이터 베이스 관리
- views.py
  - 여러 가지 함수들이 들어감
  - 각각  view 함수 하나에 하나의 페이지를 관리한다.
- urls.py
  - 사용자가 들어오면 어떤 view함수로 가는지 관리 



<br><br>

## 가상환경 설정

> - why? 가상환경
>   - 글로벌 환경에서 개발을 진행하다 보면, 실제 해당 프로젝트에는 필요없는 라이브러리들이 설치될 수 있다. 내 컴퓨터에서는 정상적으로 돌아가지만, 다른 컴퓨터에서 실행했을 때 그 사람이 가지고 있는 라이브러리와 만나게 되면 돌아가지 않을 수 있다. 
>   - 파이썬 버전도 마찬가지로 특정한 버전에서만 실행되는 경우가 있다.
>   - 따라서, 지금 이 프로젝트에서만 필요한 패키지들이 설치된 가상환경에 진입해서 개발을 진행한다.
> - 생성한 venv 폴더를 임의로 드래그 앤 드롭으로 폴더의 위치를 옮기면 가상환경이 제대로 동작하지 않는다.

<br>

- Visual Studio Code에서 기본 가상환경 설정하기

  > - Visual Studio Code에서 기본 가상환경 설정하기
  >   - Shift + Ctrl + P 혹은 좌측 하단의 파이썬 버전 클릭해서 우리가 생성한 venv를 기본 값으로 선택해 준다.
  >   - 그 다움 VSCode 내장 터미널을 새로 실행하면, 자동으로 source ~activate 까지의 명령어가 실행되면서 가상환경으로 진입한다.
  > - VSCode 환경 설정이 꼬이는 경우, 그냥 터미널에서 가상환경 진입 명령어를 실행하자!
  >   - source  venv/Scripts/activate (for Window)

  - python 이 기본적으로 가지고 있는venv 모듈을 통해 venv라는 이름의 가상환경을 만든다.

  ![1572225623605](https://user-images.githubusercontent.com/39547788/67676121-359e8c00-f9c4-11e9-8f7f-4843dcdde9c2.png)

  <br>

  - Ctrl + Shift + P를 눌러 'interpreter'를 작성한다.

    ![1572225809684](https://user-images.githubusercontent.com/39547788/67676123-359e8c00-f9c4-11e9-9647-73f672d850f0.png)

    <br>

  - interpreter를 좀전에 생성한 가상환경 venv로 설정

    ![1572225895783](https://user-images.githubusercontent.com/39547788/67676124-359e8c00-f9c4-11e9-8a89-6eed8c210113.png)

  <br>

  - 결과 

    - setting.json 파일이 생성된다. 

      ![1572226428223](https://user-images.githubusercontent.com/39547788/67676129-36372280-f9c4-11e9-96d8-e88117bf46ee.png)

      <br>

    - setting.json

      ![1572226297875](https://user-images.githubusercontent.com/39547788/67676128-36372280-f9c4-11e9-8b30-bb89dcd02265.png)

<br>

- bash를 새로 추가하면 바로 가상환경에 접근할 수 있다. 

  ![1572226024533](https://user-images.githubusercontent.com/39547788/67676126-36372280-f9c4-11e9-97c7-b8049a64e0ac.png)

  <br>

  - vnev를 설정안하도 자동으로 가상환경에 접근 가능!

<br>

- .gitignore 파일 추가

  - github에 올라가자 않도록 등록한다.

    - Django, venv, Visual Studio Code

      ![1572226168727](https://user-images.githubusercontent.com/39547788/67676127-36372280-f9c4-11e9-9c6b-60567c635e5b.png)



<br>

- setting.json 파일의 아래의 내용 추가

  ```json
  {
  
      "python.pythonPath": "venv\\Scripts\\python.exe",
      "files.associations": {
          "**/*.html": "html",
          "**/templates/**/*.html": "django-html",
          "**/templates/**/*": "django-txt",
          "**/requirements{/**,*}.{txt,in}": "pip-requirements"
      },
     
      "emmet.includeLanguages": {
  	    "django-html": "html"
  	},
      "[django-html]": {
          "editor.tabSize": 2
      },
  }
  ```

  <br><br>



## Django 설치

- `pip list`  :  설치된 프로그램 확인 

  - 아무것도 설치되어 있지 않아야 한다.

  ![1572227433604](https://user-images.githubusercontent.com/39547788/67676130-36cfb900-f9c4-11e9-9391-3e4b436326ac.png)

  <br>

- `pip install django`

  ```bash
  (venv)
  $pip install django # 최신버전 설치		
  $pip install django==2.1.8 # 원하는 버전 설치
  ```

  ![1572227659826](https://user-images.githubusercontent.com/39547788/67676131-36cfb900-f9c4-11e9-8ef8-b088c18f1db8.png)

  <br>

- `pip list` 

  ```bash
  $pip list # django 설치 및 버전 확인
  ```

  

- `python -m django --version`

  ![1572227722348](https://user-images.githubusercontent.com/39547788/67676132-37684f80-f9c4-11e9-9c57-617a5bbae40f.png)



<br><br>

## django 프로젝트 시작

```bash
# django 프로젝트를 담을 폴더 생성
$mkdir 00_django_intro

# 폴더로 이동
$cd 00_django_intro

# 현재 폴더를 프로젝트 폴더로 설정
$django-admin startproject config .
```

<br>

- `django-admin startproject config .`

  - django를 통해 project를 시작하겠다.
  - .  :  현재 위치를 django 프로젝트로 사용하겠다.

  ![1572228328924](https://user-images.githubusercontent.com/39547788/67676133-37684f80-f9c4-11e9-9d0b-b441ced19e30.png)

  <br>

  - config, manage.py 가 생성

    ![1572228387795](https://user-images.githubusercontent.com/39547788/67676135-37684f80-f9c4-11e9-8b6e-222f2a5cdd3f.png)

    <br>

  - 반.드.시! manage,py라는 파일에서 서버를 수행해야한다.

    - python manage.py

      - django 프로젝트와 의사소통하는  상호작용 Command Line Utility

        ```bash
        $python manage.py runserver
        ```

        

        ![1572228528362](https://user-images.githubusercontent.com/39547788/67676137-3800e600-f9c4-11e9-88ec-93b962ee7198.png)

      <br>

    - 터미널에 출력되는 로컬 호스트 주소로 들어가서 로켓 확인!

      - 이 서버는 django가 제공하는 경량 개발용 서버이므로, 배포할 때는 절대 이용해서는 안된다.

        배포할 때는 heroku, pythonanywhere 를 이용한다.

      - 결과 - 성공적으로 서버가 실행된다.

        ![1572228501867](https://user-images.githubusercontent.com/39547788/67676136-3800e600-f9c4-11e9-8015-b5c524eaeb63.png)

      <br><br>

### Project 폴더 구조 

![1572229151395](https://user-images.githubusercontent.com/39547788/67676138-3800e600-f9c4-11e9-904d-ea5e2b00c373.png)

<br>

#### config/

- 프로젝트의 각종 환경 설정이 담기는 폴더

- __ init__.py

  - 빈 파일, 우리가 다룰 일이 없다.
  - python에게 config 디렉토리를 하나의 python  package로 관리하도록 지시한다.

- settings.py

  - 우리가 만드는 웹 서비스의 
  - static파일, 데이터 베이스, 어플리케이션 등록 등의 각종 환경 설정들이 담겨 있다. 
  - 즉, Django Project 

- urls.py

  - 사용자 들의 경로와 우리의 view 함수를 Mapping시킨다.

  - url.py

    ```python 
    @app.route([request])
    ```

- wsgi.py

  - Web Server Gateway Interface
  - python django 프로젝트 베포할 때 확인한다.
  - 파이썬 웹 프레임워크에서 사용하는 웹 서버 규칙

#### dbsqlite3

- 데이터 베이스 정보들이 담김

#### manage,py

- django 프로젝트와 의사소통할 때 쓰이는 Command Line Utility

- 명령을 내릴 때 이곳을 통해서 명령을 내린다.

  



<br>

<br>

## Application

- 하나의 프로젝트에 여러가지 Application

  - 사용자 인증을 관리하는 Admin  Application
  - 게시판을 관리하는 Post Application

- Project VS Application 

  - Project는 여러 개의 Application을 담는 그릇의 역할을 한다.

    - 커다란 django 프로젝트의 각종 환경 설정들이 담긴다.
    - 하나의 프로젝트는 여러 개의 Application을 가질 수 있다.

  - Application은 실제 웹 서비스에서 어떠한 역할을 수행하는 것을 담당한다.

    - 예를 들어 게시글을 조회하고 수정, 삭제하거나 사용자의 로그인, 로그아웃, 회원가입을 하는 등 모든 행위는 Application이라는 친구가 수행한다.

    - 기본적으로 Application은 하나의 역할 및 기능 단위로 쪼개는 것이 원칙!

      그러나, 장고 개발진에서 어떤 식으로 나누라는 기준을 제공하는 것은 아니다. 

    - 프로젝트를 수행하면서 프로젝트 사정에 맞게 알아서 쪼개면 된다.

    - Application 이름은 가능한 복수형 (예 > pages, posts, boards, ...) 으로 짓는다.



<br>

### Pages Application 생성

- Pages라는 Application 생성 

  - $ python manage.py startapp pages

    ![1572229225707](https://user-images.githubusercontent.com/39547788/67676140-3800e600-f9c4-11e9-80b3-5c29cb7e9fbe.png)

<br><br>

### Pages Application 구조

![1572229259188](https://user-images.githubusercontent.com/39547788/67676141-38997c80-f9c4-11e9-9d7b-c3c8b35795dd.png)

- migrations
  - 데이터 베이스의 추가, 수정, 삭제 등의 기록이 담기는 곳
- __ init__.py
  - pages라는 디렉토리를 python 패키지로 관리해줘
- admin.py
  - django에서 제공하는 관리자용 페이지를 Customizing 할 수 있는 곳
- apps.py
  - pages라는 Application의 구성 정보가 담긴 파일
- models.py
  - model : 데이터 베이스의 형식 정의하는 곳
  - Application에서 사용하는 데이터베이스 정보가 담긴 파일
- test.py
  - test Code가 담긴 파일
  - 기능 테스트할 때 이곳에서 작성
- views.py
  - view 함수들이 여러 개 담기는 곳
  - 사용자에게 돌려줄 데이터를 가공하는 뷰 함수가 담긴 파일
  - Flask에서 app.py에 정의했던 함수가 담기는 장소



<br><br>

### 프로젝트에 Pages Applicatoin 설정

- Application을 생성하면 만들었다고 알려야 한다.

  - Like 전입신고

- config 폴더 아래, settings.py 파일에 생성한 Appcation의 이름을 작성한다.

  ![1572229600813](https://user-images.githubusercontent.com/39547788/67676142-38997c80-f9c4-11e9-8f1f-4fdd10db5b81.png)

  <br>

  - 가급적 아래의 규칙 및 구성으로 작성한다.

    ```python
    # Application definition
    
    INSTALLED_APPS = [
        # Local apps : 우리가 만들 apps
        'pages',
    
        # Third Party apps : 라이브러리
    
        # Django apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

    <br>

- language와 time-zone 설정

  - 한국어 / 서울 시간으로 변경

    ```python 
    LANGUAGE_CODE = 'ko-kr'
    
    TIME_ZONE = 'Asia/Seoul'
    
    USE_I18N = True
    
    USE_L10N = True
    
    USE_TZ = True
    ```

    <br>

  - 한글로 된 서버 확인

    ![1572229764280](https://user-images.githubusercontent.com/39547788/67676144-38997c80-f9c4-11e9-9c56-b2f87df77c1b.png)



<br><br>



### Django 확장 프로그램 설치

![1572235823648](https://user-images.githubusercontent.com/39547788/67676148-39321300-f9c4-11e9-8dfc-0fe0be11cc40.png)



<br><br>

### 페이지 작성

#### index 페이지 작성

- 페이지 작성 

  - pages 폴더 밑 views.py 작성

    - view 함수는 중간 관리자

    - 사용자가 접속해서 볼 페이지를 작성한다.

    - 즉, 하나하나의 페이지를 'view'라고 부른다.

    - 'view' 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다.

    - views.py

      - 첫번째 인자는 반드시 request!

      - 첫번째 return 도 반드시 request

        ```python 
        from django.shortcuts import render
        
        # Create your views here.
        
        # 필수적으로 첫번째 인자는 반드시 request!
        def index(request):
            # 첫번째 return 도 반드시 request
            return render(request, 'index.html')
        
        ```

      <br>

  - pages 폴더 밑 templates 폴더 생성 & index.html 생성

    - templates 폴더 생성 

    - index.html

      ```html
      <h1>hello, Django</h1>
      
      ```

  <br>

  - Project 폴더 밑 urls.py 작성

    - path('index/', views.index)

      - 사용자가 index라는 페이지로 들어오면 index.hrml을 불러줘

    - from pages import views

      - pages Application에서 views 파일을 import 한다.

      

    - urls.py

      ```python
      from django.contrib import admin
      from django.urls import path
      # pages Application에서 views 파일 import
      from pages import views
      
      urlpatterns = [
          # index라는 페이지로 들어오면 index.hrml 호출
          path('index/', views.index),
          path('admin/', admin.site.urls),
      ]
      
      ```

      <br>

  - 실행화면

  ![1572236189779](https://user-images.githubusercontent.com/39547788/67676149-39321300-f9c4-11e9-8494-990bd93ef232.png)

<br><br>

#### introduce 페이지 작성

- 이름 소개 페이지를 작성한다.

  - views.py

    ```python 
    def introduce(request):
        return render(request, 'introduce.html')
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('index/', views.index),
        path('introduce/', views.introduce),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - introduce.html

    ```html
    <h1>안녕하세요, 공선아 입니다. </h1>
    
    ```

    <br>

  - 실행화면

    ![1572236659339](https://user-images.githubusercontent.com/39547788/67676150-39321300-f9c4-11e9-9147-fac16c8ccacf.png)



<br><br>

## Django Template

### 템플릿 변수 (Template Variable)

> 세번째 인자로 딕셔너리 형태 변수 넘겨주기
>
> ```python 
> return render(request, '___.html', {'key' : value})
> 
> ```

<br>

#### 이름 넘기기

- 하나 이름을 파라미터로 넘긴다.

  - views.py

    - 변수를 넘길 때는 딕셔너리 형태 ( 'Key' : Value )로 넘겨야 한다.

      ```python 
      def introduce(request):
          name = '폴킴'
      
          # render 메서드의 세번째 인자로 변수를 딕셔너리 형태로 넘길 수 있다. 
          return render(request, 'introduce.html', {'name' : name})
      
      ```

    <br>

  - introduce.html

    ```html
    <h1>안녕하세요, {{name}} 입니다. </h1>
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('index/', views.index),
        path('introduce/', views.introduce),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - 실행 화면

    ![1572237021316](https://user-images.githubusercontent.com/39547788/67676152-39321300-f9c4-11e9-8eb3-91be4745d107.png)

  <br>

  <br>

#### 저녁메뉴 

- 저녁 메뉴 하나를 랜덤으로 골라 return 

  - views.py

    - 넘겨야 할 데이터가 2개 이상이면 context라는 변수 명에 담아서 넘겨준다.

      ```python 
      from django.shortcuts import render
      import random
      
      # 메뉴 하나를 랜덤으로 골라 return 
      def dinner(request):
          menu = ['초밥', '삼겹살', '치즈돈까스', '살치살 스테이크']
          today_pick = random.choice(menu)
      
          # 넘겨야 할 데이터가 2개 이상이면 context라는 변수 명에 담아서 넘겨준다.
          context = {
              'pick' : today_pick
          }
      
          return render(request, 'dinner.html', context)
      
      ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('index/', views.index),
        path('introduce/', views.introduce),
        path('dinner/', views.dinner),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - dinner.html

    ```html
    <h1>오늘의 저녁 메뉴는 ... {{pick}}!!!! </h1>
    
    ```

    <br>

  - 실행 화면

    ![1572237394803](https://user-images.githubusercontent.com/39547788/67676153-39caa980-f9c4-11e9-8ef8-b109937c5453.png)



<br><br>

#### Lorem Picsum

- Lorem Picsum 사용해서 랜덤 이미지를 보여주는 페이지 만들기!

  - views.py

    ```python 
    # Lorem Picsum 사용해서 랜덤 이미지를 보여주는 페이지 만들기!
    def image(request):
        img = "https://picsum.photos/200/300"
        context = {
            'img' : img
        }
    
        return render(request, 'image.html', context)
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('index/', views.index),
        path('introduce/', views.introduce),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - image.html

    ```html
    <img src={{img}} alt={{img}}/>
    
    ```

    <br>

  - 실행 화면 1

    ![1572239073550](https://user-images.githubusercontent.com/39547788/67676155-39caa980-f9c4-11e9-9814-d817525c4694.png)

    <br>

  - 실행 화면 2

    ![1572239114846](https://user-images.githubusercontent.com/39547788/67676156-39caa980-f9c4-11e9-8d12-a3afac2b8ac7.png)



<br><br>

### 동적 라우팅 (Variable Routing)

> Why? greeting/도현 , greeting/경희 등의 대한 각각의 수백개의 페이지를 작성하는 수고를 덜 수 있다.  

<br>

- 함수의 인자로 변수 명을 순서대로 작성한다.

<br>

#### hello : 변수 1개 넘기기

- URL을 통해 주어지는 '이름'을 출력한다.

  - views.py

    ```python 
    def hello(request, name):
        context = {'name' : name }
        return render(request, 'hello.html', context)
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        # 동적 라우팅을 위한 변수 설정
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        path('introduce/', views.introduce),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - hello.html

    ```html
    <h1>Hello~~~~~~~~</h1>
    <h2>It's {{name}} .</h2>
    
    ```

    <br>

  - 실행 화면

    ![1572241441548](https://user-images.githubusercontent.com/39547788/67676158-3a634000-f9c4-11e9-9b62-c41d7e00f9a7.png)

    <br>

    <br>



#### hello : 템플릿 변수를 여러개 넘기기

- 동적 라우팅을 통해 이름과 저녁 메뉴 

  - views.py

    ```python 
    def hello(request, name):
        menu = ['초밥', '삼겹살', '치즈돈까스', '살치살 스테이크']
        today_pick = random.choice(menu)
    
        context = {
            'name' : name,
            'pick' : today_pick,
            }
        return render(request, 'hello.html', context)
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        # 동적 라우팅을 위한 변수 설정
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        path('introduce/', views.introduce),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
     
    
    ```

    <br>

  - hello.html

    ```html
    <h1>Hello~~~~~~~~</h1>
    <h2>It's {{name}} .</h2>
    <h2>오늘은 {{pick}} 먹어유.</h2>
    
    ```

  - 실행 화면

    ![1572239890773](https://user-images.githubusercontent.com/39547788/67676157-39caa980-f9c4-11e9-811c-933c00d249c9.png)

<br><br>



#### 나의 정보 

- 템플릿 변수를 2개 이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해보자

  - views.py

    ```python 
    def introduce(request, name, age, hobby, speciality):
        context = {
            'name' : name,
            'age' : age,
            'hobby' : hobby,
            'speciality' : speciality,
            }
        return render(request, 'introduce.html', context)
    
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        # 동적 라우팅을 위한 변수 설정
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
    
    	# 동적 라우팅을 위한 변수 설정
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
    
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - hello.html

    ```html
    <h1>Hello~~~~~~~~</h1>
    <h2>It's {{name}} .</h2>
    <h2>오늘은 {{pick}} 먹어유.</h2>
    
    ```

    <br>

  - 실행 화면

    ![1572242158312](https://user-images.githubusercontent.com/39547788/67676163-3afbd680-f9c4-11e9-8b90-0ee7292b15c6.png)



<br><br>

#### 두개의 숫자 곱하기

- 숫자 2개를 동적 라우팅으로 전달 받아서, 두 개의 숫자를 곱해주는 페이지를 만들자!

  - views.py

    ```python 
    def times(request, num1, num2):
        result = num1 * num2
        context = {
            'num1' : num1,
            'num2' : num2,
            'result' : result,
        }
        return render(request, 'times.html', context)
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        # 동적 라우팅을 위한 변수 설정
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
    
        # 동적 라우팅을 위한 변수 설정
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
    
        # 동적 라우팅을 위한 변수 설정
        path('times/<int:num1>/<int:num2>', views.times),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - times.html

    ```html
    <h1>{{num1}} X {{num2}} = {{result}}</h1>
    
    ```

    <br>

  - 실행 화면

    ![1572241677388](https://user-images.githubusercontent.com/39547788/67676159-3a634000-f9c4-11e9-8ba8-c855f2854fe0.png)

<br><br>

#### 원의 넓이 

- 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자

  - views.py

    ```python 
    def radius(request, rad):
        result = 3.14 * rad*rad
        context = {
            'rad' : rad,
            'result' : result,
            }
        return render(request, 'radius.html', context)
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        # 동적 라우팅을 위한 변수 설정
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
    
    	# 동적 라우팅을 위한 변수 설정
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
    
        # 동적 라우팅을 위한 변수 설정
        path('times/<int:num1>/<int:num2>', views.times),
    
        # 동적 라우팅을 위한 변수 설정
        path('radius/<int:rad>', views.radius),
    
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - radius.html

    ```html
    <h1>{{rad}} 인 원의 넓이는 {{result}} 입니다. </h1>
    
    ```

    <br>

  - 실행 화면

    ![1572241885886](https://user-images.githubusercontent.com/39547788/67676160-3a634000-f9c4-11e9-8f3a-eee81422bf32.png)

<br><br>





#### 랜덤 이미지 : 너비와 높이 지정

- 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자

  - views.py

    ```python 
    def imageSize(request, width, height):
        img = "https://picsum.photos/"+width + "/"+height
        context = {
            'img' : img,  
        }
    
        return render(request, 'imageSize.html', context)
    
    ```

    <br>

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        # 동적 라우팅을 위한 변수 설정
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
    
        # path('introduce/', views.introduce),
        # 동적 라우팅을 위한 변수 설정
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
    
        # 동적 라우팅을 위한 변수 설정
        path('times/<int:num1>/<int:num2>', views.times),
    
        # 동적 라우팅을 위한 변수 설정
        path('radius/<int:rad>', views.radius),
    
        # 동적 라우팅을 위한 변수 설정
        path('imageSize/<str:width>/<str:height>', views.imageSize),
    
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

    <br>

  - imageSize.html

    ```html
    <h1>랜덤 이미지 쨘</h1>
    <img src={{img}} alt={{img}}/>
    
    ```

    <br>

  - 실행 화면

    - 500 * 500

      ![1572241912994](https://user-images.githubusercontent.com/39547788/67676161-3a634000-f9c4-11e9-9842-965d63bb4797.png)

      <br>

    - 100 * 100

      ![1572241937263](https://user-images.githubusercontent.com/39547788/67676162-3afbd680-f9c4-11e9-9c09-b82a09fc2df4.png)

<br>





## DTL (Django Template Language)

- Django에서 사용하는 템플릿 엔진으로, DTL이 기본적으로 내장되어 있다.
  - Flask에서 사용하던 Jinja2 템플릿 엔진과 비슷하다.
- Jinja2와 마찬가지로 조건문, 반복문, 변수 치환, 필터 등의 기능을 제공한다.
- 사용자에게 보여줄 데이터를 가공하는 작업이 필요한 경우, DTL에 내장된 연산 방식을 사용하지 말고, 되도록이면 view 함수 내부에서 데이터를 가공할 뒤 템플렛에게 넘겨주자.



### 기본 코드

- views.py

  ```python 
  from datetime import datetime
  def template_language(request):
      menus = ['짜장면', '탕수육', '짬뽕', '양장피']
      my_sentence = 'Life is short, you need python'
      messages = ['apple', 'banana', 'cucumber', 'mango']
      datetimenow = datetime.now()
      empty_list = []
      context = {
          'menus': menus,
          'my_sentence': my_sentence,
          'messages': messages,
          'empty_list': empty_list,
          'datetimenow': datetimenow,
      }
      return render(request, 'template_language.html', context)
  
  ```

- urls.py

  ```python 
  from django.contrib import admin
  from django.urls import path
  from pages import views
  
  urlpatterns = [
  
      path('template_language/', views.template_language),
      path('hello/<str:name>/', views.hello),
      path('index/', views.index),
      # path('introduce/', views.introduce),
      path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
      path('times/<int:num1>/<int:num2>', views.times),
      path('radius/<int:rad>', views.radius),
      path('imageSize/<str:width>/<str:height>', views.imageSize),
      path('dinner/', views.dinner),
      path('image/', views.image),
      path('admin/', admin.site.urls),
  ]
  
  ```

  



#### 주석

- 주석 형식

  ```django
  {% comment %} 주석입니다.  {% endcomment %}
  
  ```

  <br>

#### 반복문

- 반복문 형식

  ```django
  {% for menu in menus %}
   
  {% endfor %}
  
  ```

  <br>

- template_language.html

  ```django
  <h1>반복문</h1>
  <h4>메뉴판</h4>
  
  <ul>
  {% for menu in menus %}
    <li>{{menu}}</li>
  {% endfor %}
  </ul>
  
  ```

  - 반복문 실행화면

    ![1572244097631](https://user-images.githubusercontent.com/39547788/67676164-3afbd680-f9c4-11e9-864c-8a8b465dcda6.png)

    <br>







#### 조건문

- 조건문 형식

  ```django
  {% if 'a'  in 'apple' %}
  
  {% endif %}
  
  
  
  {% if menu == '짜장면' %}
  
  {% else %}
  
  {% endif %}
  
  ```

  

- template_language.html

  ```django
  <h1>조건문</h1>
  <h4>메뉴판</h4>
  {% if '짜장면' in menus %}
    <p>짜장면에는 정성이 가득</p>
  {% endif %}
  
  <hr>
  
  <ul>
  {% for menu in menus %}
    {% if menu == '짜장면' %}
      <li>{{menu}} : 짜장면에는 정성이 가득</li>
    {% else %}
      <li>{{menu}}</li>
    {% endif %}
  {% endfor %}
  </ul>
  
  ```

  

  - 조건문 실행 화면

    ![1572252166016](https://user-images.githubusercontent.com/39547788/67676170-3c2d0380-f9c4-11e9-8960-2ac178084533.png)







#### Length Filter

- Length Filter 형식

  - `|length`

    ```django
    {% if message|length > 5 %}
    
    {% else %}
    
    {% endif %}
    
    ```

- template_language.html

  ```django
  <h1>Length Filter</h1>
  {% for message in messages %}
    {% if message|length > 5 %}
      <P>{{message}} ... 너무 길어요. 줄여주세요!</p>
    {% else %}
      <P>{{message}} 의 길이는 {{message|length}} 글자!</p>
    {% endif %}
  {% endfor %}
  
  ```

  - Length Filter 실행 화면

    ![1572244612438](https://user-images.githubusercontent.com/39547788/67676167-3b946d00-f9c4-11e9-9a4c-98b41b93870b.png)

<br>

#### Lorem

- Lorem 형식

  - w : word

  - p : <p></p>

  - random : 무작위

    ```django
    {% lorem %}
    
    ```

    

- template_language.html

  ```django
  <h1>Lorem Text</h1>
  {% lorem %}
  
  <hr>
  
  {% lorem 3 w%}
  
  <hr>
   {% comment %} 랜덤으로 단어  {% endcomment %}
  {% lorem 4 w random%}
  
  <hr>
  
  {% lorem 4 p %}
  
  ```

  - Lorem 실행 화면

    ![1572252193281](https://user-images.githubusercontent.com/39547788/67676171-3c2d0380-f9c4-11e9-924c-0e6e40a16a9a.png)

<br>



#### 글자수 제한 (Truncate - 자르기)

- Truncate 형식

  ```django
  {{my_sentence|truncatewords:3}}
  {{my_sentence|truncatechars:3}}
  
  ```

  

- template_language.html

  ```django
  <!-- 단어 단위로 자른다. -->
  <p>{{my_sentence|truncatewords:3}}</p>
  
  <!-- 문자 단위로 자른다. / 3번째 포함 X -->
  <p>{{my_sentence|truncatechars:3}}</p>
  
  <!-- 문자 단위로 자른다. / 10번째 포함 X -->
  <p>{{my_sentence|truncatechars:10}}</p>
  
  ```

  - Truncate 실행화면

    ![1572252207204](https://user-images.githubusercontent.com/39547788/67676172-3c2d0380-f9c4-11e9-9499-f7b28cc17f87.png)

<br>

#### 연산

> 자세한 내용은 [django mathfilters](https://pypi.org/project/django-mathfilters/) 참고

- 기본적으로, 사용자에게 보여줄 데이터를 가공하는 것은 뷰 함수에서 처리하자

  반드시 필요한 경우에만 연상 필터를 사용한다.

- 연산 형식

  ```django
  {{ 4|add:6}}
  
  ```

  

- template_language.html

  ```django
  <h1>연산</h1>
  <!-- 
      기본적으로, 사용자에게 보여줄 데이터를 가공하는 것은 뷰 함수에서 처리하자
      반드시 필요한 경우에만 연상 필터를 사용한다.
  
      django mathfilters
   -->
  <p>{{ 4|add:6}}</p>
  
  <hr>
  
  ```

  - 연산 실행 화면

    ![1572252215789](https://user-images.githubusercontent.com/39547788/67676173-3cc59a00-f9c4-11e9-8899-c8405ff89157.png)

<br>

#### 날짜

- 날짜 형식

  - 파이썬 내장 라이브러리 datetimenow

    ```django
    {{datetimenow}}
    
    ```

    

  - DTL 내장  now (기본)

    ```django
    {% now "DATETIME_FORMAT"%}
    
    ```

    

- template_language.html 

  - DTL 내장 now를 활용해 다양한 형태의 날짜 형식을 출력할 수 있다.

    ```django
    <h1>날짜</h1>
    {% comment %} DTL에 {% now %}가 기본적으로 내장되어 있다. {% endcomment %}
    
    <!-- 7.1 파이썬 내장 라이브러리인 datetimenow 로 날짜를 출력 -->
    {{datetimenow}} <br>
    
    <!-- 7.2 DTL에 내장된  now 를 사용해보자 -->
    {% now "DATETIME_FORMAT"%} <br>
    {% now "SHORT_DATETIME_FORMAT"%} <br>
    {% now "DATETIME_FORMAT"%} <br>
    {% now "DATE_FORMAT"%} <br>
    {% now "SHORT_DATE_FORMAT"%} <br>
    
    <hr>
    
    {% now "Y년 m월 d일 D h:i"%}
    
    ```

  - 날짜 실행 화면

    ![1572252245696](https://user-images.githubusercontent.com/39547788/67676174-3cc59a00-f9c4-11e9-96e8-806e1c4424ca.png)

<br>

#### 기타

- 특정 str를 url로 변환

  - urlize

  - template_language.html 

    ```django
    {{'google.com'|urlize}}
    ```

  - 기타 실행 화면

    ![1572252259077](https://user-images.githubusercontent.com/39547788/67676175-3cc59a00-f9c4-11e9-8097-737b923d1153.png)



<br>

### 로또 번호 추첨

- 임으로 출력한 로또 번호와 가장 최근에 추첨한 로또 번호 비교해서 당첨여부 확인

  - views.py

    ```python 
    def lotto(request, lottonum, bonus):
    
        # [18,34,39,43,44,45]
        real_lotto = list(map(int, lottonum.strip().split(',')))
        # s_lotto = sorted(real_lotto)
    
        num_list = [i for i in range(1, 47)]
        lotto_list = random.sample(num_list, 6)
        my_bnum = random.choice(num_list)
        # s_lotto_list = sorted(lotto_list)
       
        count = 0
        for i in real_lotto:
            for j in lotto_list:
                if i == j:
                    count += 1
                else : 
                    pass
    
        if count == 6:
            rank = "1"
        elif count == 5 and bonus == my_bnum: 
            rank = "2"
        elif count == 5 and bonus != my_bnum: 
            rank = "3"
        elif count == 4: 
            rank = "4"
        elif count == 3: 
            rank = "5"
        else :
            rank = "꽝"
    
        context = {
            'real_lotto': real_lotto,
            'lotto_list': lotto_list,
            'count': count,
            'rank': rank,
            'bonus': bonus,
            'my_bonus': my_bnum,
        }
        return render(request, 'lotto.html',context)
    ```

    

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('lotto/<str:lottonum>/<int:bonus>', views.lotto),
        path('template_language/', views.template_language),
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        # path('introduce/', views.introduce),
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
        path('times/<int:num1>/<int:num2>', views.times),
        path('radius/<int:rad>', views.radius),
        path('imageSize/<str:width>/<str:height>', views.imageSize),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    ```

    

  - lotto.html

    ```django
    <h1>인생 역전 가능할까요?</h1>
    <h3>당신이 뽑은 로또 번호는... </h3>
    <p>{{lotto_list}}</p>
    
    <h3>실제 로또 번호는... </h3>
    <p>{{real_lotto}}</p>
    
    <h3>실제 보너스 번호는  </h3>
    <p>{{bonus}}</p>
    
    <h3>나의 보너스 번호는  </h3>
    <p>{{my_bonus}}</p>
    
    <h3>맞은 개수 </h3>
    <p>{{count}}</p>
    
    <h3>순위 </h3>
    {% if rank == '꽝' %}
      <p>꽝! 다음 기회에...</p>
    {% else %}
      <p>{{rank}} 등 입니다!</p>
    {% endif %}
    
    ```

    - 로또 추첨 실행 화면

      ![1572262106883](https://user-images.githubusercontent.com/39547788/67676894-ee18ff80-f9c5-11e9-9df2-1dc5e56b98db.png)

<br>

### Is it your birthday?

- 오늘 날짜와 본인 실제 생일 비교해서 , 맞으면 예! 아니면 아니오!

- 날짜 라이브러리 활용

  - views.py

    ```python 
    def isbirth(request):
        days = datetime.now()
        if days.month == 10 and days.day == 28:
            result = True
        else : 
            result = False
    
        context = {
            'result': result,
        }
        return render(request, 'isbirth.html',context)
    
    ```

    

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('isbirth/', views.isbirth),
        path('lotto/<str:lottonum>', views.lotto),
        path('template_language/', views.template_language),
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        # path('introduce/', views.introduce),
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
        path('times/<int:num1>/<int:num2>', views.times),
        path('radius/<int:rad>', views.radius),
        path('imageSize/<str:width>/<str:height>', views.imageSize),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

    

  - isbirth.html

    ```django
    <h1>Is it your birthday?</h1>
    {% if result %}
      <h2>생일 축하해~</h2>
      {% else %}
      <h2>너의 생일이 아니야</h2>
    {% endif %}
    
    ```

    - Is it your birthday? 실행 화면

      - 생일이 오늘인 경우

        ![1572262138967](https://user-images.githubusercontent.com/39547788/67676178-3d5e3080-f9c4-11e9-805a-3f4bccbd3b8c.png)

        <br>

      - 생일이 오늘이 아닌 경우

        ![1572262161055](https://user-images.githubusercontent.com/39547788/67676117-3505f580-f9c4-11e9-8513-399e880bc057.png)





<br><br>



### 회문 판별

- 오디오는 거꾸로 해도 오디오 -> 회문

- (팰린드롬 / 문자열 슬라이싱 파트 활용 )

  - views.py

    ```python 
    def ispal(request, word):
        # 검색 키워드 : 파이썬 문자열 슬라이스
        if word == word[::-1]:
            result = True
        else :
            result = False
        context = {
            'word': word,
            'result': result,
        }
        return render(request, 'ispal.html',context)
    
    ```

    

  - urls.py

    ```python 
    from django.contrib import admin
    from django.urls import path
    from pages import views
    
    urlpatterns = [
        path('lotto/<str:lottonum>', views.lotto),
        path('ispal/<str:word>', views.ispal),
        path('isbirth/', views.isbirth),
        path('template_language/', views.template_language),
        path('hello/<str:name>/', views.hello),
        path('index/', views.index),
        # path('introduce/', views.introduce),
        path('introduce/<str:name>/<str:age>/<str:hobby>/<str:speciality>/', views.introduce),
        path('times/<int:num1>/<int:num2>', views.times),
        path('radius/<int:rad>', views.radius),
        path('imageSize/<str:width>/<str:height>', views.imageSize),
        path('dinner/', views.dinner),
        path('image/', views.image),
        path('admin/', admin.site.urls),
    ]
    
    ```

    

  - ispal.html

    ```django
    {% if result %}
     <p> {{word}}는 거꾸고 말해도 {{word}}이므로, 회문이다.  </p>
    {% else %}
     <p> {{word}}는 회문이 아니다.  </p>
    {% endif %}
    
    ```

    - 회문 판별 실행 화면

      - 회문인 경우

        ![1572262182951](https://user-images.githubusercontent.com/39547788/67676119-3505f580-f9c4-11e9-91ab-a065aff4ffba.png)

        <br>

      - 회문이 아닌 경우

        ![1572262197614](https://user-images.githubusercontent.com/39547788/67676120-359e8c00-f9c4-11e9-998e-413c7bbc04b9.png)



<br><br>



## 코드 작성 순서 (권장)

> 대출창구 (views.py)를 만들지 않았는데 손님을 대출창구로 모시면 (urls.py), 컴플레인을 받는다. (에러를 뿜는다.)

1. views.py (view 작성)

   - 보여주고자 하는 페이지의 view 함수를 작성한다.
   - 기능 구현 우선

   

2. templates

   - 사용자에게 보여줄 Template 페이지를 작성한다.

   

3. urls.py (view 등록)

   - 사용자가 해당 경로로 들어왔을 때 view 함수를 실행한다.

