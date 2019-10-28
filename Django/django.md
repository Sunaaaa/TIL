# django

- 2005년 7월
- 보안이 우수하고 유지보수가 편리한 웹사이트를 신속하게 개발하는 하도록 도움을 주는 파이썬 웹 프레임워크



##### Versatile (**다용도**)

##### Secure (**안전한**)

##### Scalable (**확장성** )

##### Complete (**완결성** )

##### Maintainable (**유지보수가 쉬운**)

##### Portable (**포터블한**)







### 성격

- Opinionate : 독선적
- UnOpinionate : 관용적, Customizing 가능
- 다소 Opinionate 이지만, 일부 Customizing 할 수 있는 부분이 있다. 





- Static Web (html 문서의 집합) 과 Dynamic Web 모두 가능





## MTV 패턴

#### MVC 

- Model
- View
- Controller

![1572230693722](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572230693722.png)

- Model
  - 데이터를 정의 (Data)
  - 데이터를 관리, 데이터베이스의 모양, 형태를 정의

- Template : 사용자가 보는 화면을 정의

- View

  - 중간 관리자
  - 사용자가 보고 있는 데이터를 가공
  - Model에 있는 데이터 베이스의 데이터를 꺼내서 가공한다.

  - @app.route() 안에 정의된 함수와 같은 역할



3 Kings Of Django

- models.py
  - 데이터 베이스 관리
- views.py
  - 여러 가지 함수들이 들어감
  - 각각  view 함수 하나에 하나의 페이지를 관리한다.
- urls.py
  - 사용자가 들어오면 어떤 view함수로 가는지 관리 



T & V

T와 V를 통해 request와 response



사용자의 요청이 들어온다.

urls라는 파일 (url.py) 을 따로 두어 사용자가 들어올 수 있는 url을 따로 보관한다.

- 적절한 

view가 model에서 데이터를 가져옴 

view.py







## Django 설치하기

> 생성한 venv 폴더를 임의로 드래그 앤 드롭으로 폴더의 위치를 옮기면 가상환경이 제대로 동작하지 않는다.

<br>

- python 이 기본적으로 가지고 있는venv 모듈을 통해 venv라는 이름의 가상환경을 만든다.

  ![1572225623605](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572225623605.png)



- Ctrl + Shift + P를 눌러 'interpreter'를 작성하여 

  ![1572225809684](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572225809684.png)



- interpreter를 좀전에 생성한 가상환경 venv로 설정

  ![1572225895783](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572225895783.png)

  - 결과 

    - setting.json 파일이 생성된다. 

      ![1572226428223](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572226428223.png)

      - setting.json

        ![1572226297875](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572226297875.png)



- bash를 새로 추가하면 바로 가상환경에 접근할 수 있다. 

  ![1572226024533](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572226024533.png)

  - vnev를 설정안하도 자동으로 가상환경에 접근 가능!



- .gitignore 파일 추가

  - github에 올라가자 않도록 등록한다.

    - Django, venv, Visual Studio Code

      ![1572226168727](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572226168727.png)





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

  

- Django 설치

  - `pip list`  :  설치된 프로그램 확인 

    -  아무것도 설치되어 있지 않아야 한다.

    ![1572227433604](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572227433604.png)

  - `pip install django`

    ![1572227659826](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572227659826.png)

  - `pip list` : django 설치 확인

  - `python -m django --version`

    ![1572227722348](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572227722348.png)





## 프로젝트 생성

- `django-admin startproject config .`

  : django를 통해 project를 시작하겠다.

  . : 현재 위치를 django 프로젝트로 사용하겠다.

  ![1572228328924](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572228328924.png)

  - config, manage.py 가 생성

    ![1572228387795](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572228387795.png)

  - 기본적으로 manage,py라는 파일에서 서버를 수행해야한다.

    - python manage.py

      ![1572228528362](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572228528362.png)

    - 결과 - 성공적으로 서버가 실행된다.

      ![1572228501867](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572228501867.png)

### Project 폴더 구조 

![1572229151395](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572229151395.png)

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





## Application

- 하나의 프로젝트에 여러가지 Application
  - 사용자 인증을 관리하는 Admin  Application
  - 게시판을 관리하는 Post Application



Pages Application 생성

- $ python manage.py startapp pages

![1572229225707](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572229225707.png)

- Pages라는 Application 생성

  ![1572229259188](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572229259188.png)



### Pages Application 구조

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





### 프로젝트에 Pages Applicatoin 설정

- Application을 생성하면 만들었다고 알려야 한다.
  - Like 전입신고

- config 폴더 아래, settings.py 파일에 생성한 Appcation의 이름을 작성한다.

  ![1572229600813](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572229600813.png)

  - 가급적 아래의 규칙 및 구성으로 

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

    



- language와 time-zone 설정

  - 한국어 / 서울 시간으로 변경

    ```python 
    LANGUAGE_CODE = 'ko-kr'
    
    TIME_ZONE = 'Asia/Seoul'
    
    USE_I18N = True
    
    USE_L10N = True
    
    USE_TZ = True
    ```

    

  - 한글로 된 서버 확인

    ![1572229764280](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572229764280.png)







Django 확장 프로그램 설치

![1572235823648](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572235823648.png)





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

      

  - pages 폴더 밑 templates 폴더 생성 & index.html 생성

    - templates 폴더 생성 

    - index.html

      ```html
      <h1>hello, Django</h1>
      ```

  

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

      

  -  실행화면

  ![1572236189779](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572236189779.png)



#### introduce 페이지 작성

- 이름 소개 페이지를 작성한다.

  - views.py

    ```python 
    def introduce(request):
        return render(request, 'introduce.html')
    ```

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

    

  - introduce.html

    ```
    <h1>안녕하세요, 공선아 입니다. </h1>
    ```

    

  - 실행화면

    ![1572236659339](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572236659339.png)





## 코드 작성 순서 (권장)

1. views.py (view 작성)

   - 보여주고자 하는 페이지의 view 함수를 작성한다.
   - 기능 구현 우선

   

2. templates

   - 사용자에게 보여줄 Template 페이지를 작성한다.

   

3. urls.py (view 등록)

   - 사용자가 해당 경로로 들어왔을 때 view 함수를 실행한다.





## Django Template

### 템플릿 변수 (Template Variable)

> 세번째 인자로 딕셔너리 형태 변수 넘겨주기
>
> ```python 
> return render(request, '___.html', {'key' : value})
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

    

  - introduce.html

    ```html
    <h1>안녕하세요, {{name}} 입니다. </h1>
    ```

    

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

    

  - 실행 화면

    ![1572237021316](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572237021316.png)

  

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

    

  - dinner.html

    ```
    <h1>오늘의 저녁 메뉴는 ... {{pick}}!!!! </h1>
    ```

    

  - 실행 화면

    ![1572237394803](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572237394803.png)





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

  - image.html

    ```html
    <img src={{img}} alt={{img}}/>
    ```

  - 실행 화면 1

    ![1572239073550](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572239073550.png)

  - 실행 화면 2

    ![1572239114846](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572239114846.png)





### 동적 라우팅 (Variable Routing)

> Why? 



- greeting/도현 , greeting/경희 등의 대한 각각의 수백개의 페이지를 작석하는 수고를 덜 수 있다. 

- 함수의 인자로 변수 명을 순서대로 작성한다.



#### hello : 변수 1개 넘기기

- URL을 통해 주어지는 '이름'을 출력한다.

  - views.py

    ```python 
    def hello(request, name):
        context = {'name' : name }
        return render(request, 'hello.html', context)
    ```

    

  - urls.py

    ```
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

    

  - hello.html

    ```html
    <h1>Hello~~~~~~~~</h1>
    <h2>It's {{name}} .</h2>
    ```

  - 실행 화면

    ![1572241441548](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572241441548.png)



#### hello : 템플릿 변수를 여러개 넘기기

- 동적 라우팅을 통해 이름과 저녁 메뉴 

  - views.py

    ```
    def hello(request, name):
        menu = ['초밥', '삼겹살', '치즈돈까스', '살치살 스테이크']
        today_pick = random.choice(menu)
    
        context = {
            'name' : name,
            'pick' : today_pick,
            }
        return render(request, 'hello.html', context)
    ```

    

  - urls.py

    ```
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

    

  - hello.html

    ```
    <h1>Hello~~~~~~~~</h1>
    <h2>It's {{name}} .</h2>
    <h2>오늘은 {{pick}} 먹어유.</h2>
    ```

  - 실행 화면

    ![1572239890773](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572239890773.png)





#### 나의 정보 

- 템플릿 변수를 2개 이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해보자

  - views.py

    ```
    # 실습 1
    # 템플릿 변수를 2개 이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해보자
    def introduce(request, name, age, hobby, speciality):
        context = {
            'name' : name,
            'age' : age,
            'hobby' : hobby,
            'speciality' : speciality,
            }
        return render(request, 'introduce.html', context)
    
    ```

    

  - urls.py

    ```
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

  - hello.html

    ```
    <h1>Hello~~~~~~~~</h1>
    <h2>It's {{name}} .</h2>
    <h2>오늘은 {{pick}} 먹어유.</h2>
    ```





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

    

  - urls.py

    ```
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

    

  - times.html

    ```html
    <h1>{{num1}} X {{num2}} = {{result}}</h1>
    ```

  - 실행 화면

    ![1572241677388](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572241677388.png)





#### 원의 넓이 

- 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자

  - views.py

    ```
    def radius(request, rad):
        result = 3.14 * rad*rad
        context = {
            'rad' : rad,
            'result' : result,
            }
        return render(request, 'radius.html', context)
    ```

    

  - urls.py

    ```
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

    

  - radius.html

    ```html
    <h1>{{rad}} 인 원의 넓이는 {{result}} 입니다. </h1>
    ```

  - 실행 화면

    ![1572241885886](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572241885886.png)







#### 랜덤 이미지 : 너비와 높이 지정

- 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자

  - views.py

    ```
    def imageSize(request, width, height):
        img = "https://picsum.photos/"+width + "/"+height
        context = {
            'img' : img,  
        }
    
        return render(request, 'imageSize.html', context)
    ```

    

  - urls.py

    ```
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

    

  - radius.html

    ```
    <h1>랜덤 이미지 쨘</h1>
    <img src={{img}} alt={{img}}/>
    ```

  - 실행 화면

    - 500 * 500

      ![1572241912994](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572241912994.png)

    - 100 * 100

      ![1572241937263](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572241937263.png)

