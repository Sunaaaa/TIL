# 19.10.29 : Start Django 2

## 1. HTML Form Tag

- Static Web VS Dynamic Web
  - Static Web 
    - 단순히 html 페이지 여러 개로 구성되어 있는 웹 서비스
  - Dynamic Web
    - 데이터 베이스에 변동을 주어서 데이터 베이스에 따라 웹 페이지의 내용이 바뀌는 웹 서비스

<br>

> Form을 통해 사용자로부터 정보를 받거나 받은 정보를 가공하는 등의 로직을 구현했다.
>
> Dynamic Web을 구현하기 위해서는 Form을 통해서 **정보를 요청하는 절차가 반드시 필요**하다.

<br>

- `<form></form>`
  - 사용자로부터 제공받은 데이터를 서버 측에 전송해주는 역할
  - 사용자가 여러 정보를 입력할 수 있는 수단을 제공 => input 태그를 통해!!!
    - `<form action="/new/">` 
      - 서버 측의 어디로 보낼 것인지
      - 서버 측의 경로를 지정한다.
    - `<form action="", method = "GET">`
      - 요청 방식을 무엇으로 할 것인지
      - POST 또는 GET
- `<input>`
  - Form 태그 안에서 가장 중요한 태그
  - 사용자로부터 어떠한 정보를 입력받는다.
    - `<input type="">` 
      - 사용자가 입력할 데이터의 종류 지정
    - `<input type="" name="">`
      - 서버 측에서 사용자가 입력한 값을 가져올 이름으로 사용

<br>

<br>



## [summary] GET VS POST

### GET 

- 서버 측에 데이터를 보낼 때 URL에 다 보임

  - 예 

    ![1572312993514](https://user-images.githubusercontent.com/39547788/67767014-22a6bd00-fa93-11e9-93ec-605436f70097.png)

  <br>

### POST

- 내부적으로 안쪽에 숨겨서 보낸다.

- HTTP BODY라는 곳에 숨겨서 보낸다.

  - 예

    ![1572322399735](https://user-images.githubusercontent.com/39547788/67767020-23d7ea00-fa93-11e9-93f2-74aee61d7d3a.png)

<br>

<br>



## 2. HTML Form - GET 요청

### 2.1 GET

> GET 요청은 서버로부터 정보를 조회하는데 사용한다. 데이터를 서버로 전송할 때 Query String을 통해 전송한다.
>
> - 서버의 데이터 (리소스) 를 변경 시키지 않는 요청이고, HTML 파일을 조회할 때 사용한다.
> - 서버에 GET 요청을 하면 HTML 문서 한 장을 받는다.



#### 2.1.1 throw & catch

- Form을 통해 정보를 throw 하고, throw된 정보를 catch하기

  - views.py

    ```python 
    # 정보를 던져줄 페이지
    def throw(request):
        return render(request, 'throw.html')
    
    # 사용자로부터 정보를 받아서 다시 던져줄 페이지
    # request를 통해서 정보가 들어온다.
    def catch(request):
        # GET으로 보내면 request를 통해서 GET 정보가 들어온다. JSON/딕셔너리
        print(request)
        print(request.GET)
        message = request.GET.get('message')
        message2 = request.GET.get('message2')
        context = {
            'message' : message
        }
        
        return render(request, 'myapp/catch.html', context)
    ```

    <br>

    - print(request) & print(request.GET)

      ![1572316199798](https://user-images.githubusercontent.com/39547788/67767018-233f5380-fa93-11e9-8623-bb861cb0766d.png)

      <br>

  - urls.py

    ```python 
    urlpatterns = [
        path('throw/', views.throw),
        path('catch', views.catch),
        .
        .
        .
    ]
    ```

    <br>

  - throw.html

    ```html
    <form action = "/catch/" method="GET">
      <input type="text" name="message">
      <input type="submit" value="던져!">
    </form>
    ```

    <br>

  - catch.html

    ```django
    <h1>니가 보낸 정보를 잘 받았다.</h1>
    <h1>그 정보의 내용을 <span style="color : red">{{message}}</span> 이란다!</h1>
    ```

  <br>

  - 실행 화면

    ![1572312832847](https://user-images.githubusercontent.com/39547788/67767012-22a6bd00-fa93-11e9-8107-e5f61dc82879.png)

    <br>

  - 실행 화면

    ![1572312993514](https://user-images.githubusercontent.com/39547788/67767014-22a6bd00-fa93-11e9-93ec-605436f70097.png)

    

  <br>

<br>

#### 2.1.2 ASCII ART

- 아스키 아트 API를 통한 요청-응답을 실습한다.

  - views.py

    ```python 
    # [실습] 아스키 아트 API를 통한 요청-응답 실습
    # 사용자로부터 텍스트를 입력받는 페이지
    def art(request):    
        return render(request, 'art.html')
    
    # 텍스트 받아서 아스키 아트로 보여주는 페이지
    def result(request):
        message = request.GET.get('text')
        art = "http://artii.herokuapp.com/make?text=" + message
        context = {
            'art' : art
        }
        
        return render(request, 'result.html', context)
    ```

    <br>

  - urls.py

    ```python 
    urlpatterns = [
        path('art/', views.art),
        path('result/', views.result),
        .
        .
        .
    ]
    ```

    <br>

  - art.html

    ```html
    <form action = "/result/" method="GET">
      <input type="text" name="text">
      <input type="submit" value="ASCII ART!">
    </form>
    ```

    <br>

  - result.html

    ```html
    <h2>ASCII ART</h2>
    
    <iframe width="500" height="500" src={{art}}></iframe>
    ```

    <br>

  - 실행 화면

    ![1572314573687](https://user-images.githubusercontent.com/39547788/67767016-233f5380-fa93-11e9-8484-1d97fc291a0d.png)

    <br>

  - 실행 화면

    ![1572314589073](https://user-images.githubusercontent.com/39547788/67767017-233f5380-fa93-11e9-9ae3-542c509faf45.png)

  

<br><br>

#### 2.1.3 ASCII ART_requests

- requests를 사용하여 ASCII API로 요청을 보내 여러 개의 font를 받아, 랜덤으로 하나의 font를 선택하여 ASCII ART를 만든다. 

  - requests 모듈 설치

    ![1572325467860](https://user-images.githubusercontent.com/39547788/67767025-24708080-fa93-11e9-8633-81754ae66a60.png)

    <br>

  - views.py

    ```python 
    import requests
    
    def art(request):    
        return render(request, 'art.html')
    
    def result(request)
    # 1. form 태그로 날린 데이터를 받는다. (GET 방식)
        word = request.GET.get('word')
    
        # 2. ARTII api로 요청을 보내 응답 결과를 text로 fonts에 저장한다.
        fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
        # fonts --> str
    
        # 3. fonts(str)를 fonts(list)로 바꾼다.
        fonts = fonts.split('\n')
    
        # 4. fonts(list)안에 들어있는 요소중 하나를 선택해서 font라는 변수에 저장한다.
        font = random.choice(fonts)
    
        # 5. 위에서 우리가 만든 word와 font를 가지고 다시 요청을 보내 응답 결과를 result에 저장
        result = requests.get(
            f'http://artii.herokuapp.com/make?text={word}&font={font}'
        ).text
    
        context = {'result': result}
        return render(request, 'result.html', context)
    ```

    <br>

  - urls.py

    ```python 
    urlpatterns = [
        path('art/', views.art),
        path('result/', views.result),
        .
        .
        .
    ]
    ```

    <br>

  - 실행 화면

    ![1572324392376](https://user-images.githubusercontent.com/39547788/67767024-24708080-fa93-11e9-8aa1-c4654070f146.png)

  <br><br>

## 3. HTML Form - POST 요청

> CRUD
>
> - Create : 생성
> - Read : 조회
> - Update : 수정
> - Delete : 삭제

<br>

### 3.1 POST

> POST 요청은 GET 요청처럼 Query String에 데이터가 노출되는 것이 아니라, HTTP BODY에 담겨서 전송된다. 
>
> - GET 요청
>   - Read
> - POST 요청
>   - Create, Update, Delete
>
> <br>
>
> POST 요청은 데이터 (리소스)를 수정/삭제시키는 로직이기 때문에, 똑같은 요청을 여러 번 시도하게 되면 서버에서 응답하는 결과를 다를 수 있다. 
>
> 원칙적으로 POST 요청을 보냈는데, HTML 파일을 그려주는 (render) 응답을 해서는 안된다. HTML 파일을 그려주는 응답은 GET 요청에서만 사용한다.
>
> - 사용자가 로그인을 하는 로직은 POST 요청을 통해서 이루어진다. 로직 마지막에 어떤 정보를 변수로 넘겨서 HTML 파일을 넘겨주는 로직을 구현하는게 아니라, 로그인이 끝나면 메인 페이지 ('/')  등으로 **redirect 시켜주는 로직**을 구현해야 한다.

<br>



#### 3.1.1 회원가입 

- (실제로는 이런 방식으로 구현하지 않는다. 이건 저세상 코드)

  사용자 인증이 끝나면, 메인 페이지로 이동시켜야 한다.

  - views.py

    ```python 
    # 회원가입 폼을 보여주는 페이지
    def user_new(request):
        return render(request, 'user_new.html')
    
    # 회원가입 요청을 처리하는 페이지 (로직)
    def user_create(request):
        user_id = request.POST.get('user_id')
        pw = request.POST.get('pw')
    
        context = {
            'user_id' : user_id,
            'pw' : pw,
        }
        return render(request, 'user_create.html', context)
    ```

    <br>

  - urls.py

    ```python 
    urlpatterns = [
        path('user_new/', views.user_new),
        path('user_create/', views.user_create),
        .
        .
        .
    ]
    
    ```

    <br>

  - user_new.html

    ```html
    <form action = "/user_create/" method="POST">
      아이디 : <input type="text" name="id"> <br>
      비밀번호 : <input type="password" name="pw"> <br>
      <input type="submit" value="ASCII 가입하기!">
    </form>
    ```

    <br>

  - 실행 화면

    - HTTP body에 숨어져있기 때문에 query String이 노출되지 않는다.

      ![1572322399735](https://user-images.githubusercontent.com/39547788/67767020-23d7ea00-fa93-11e9-93f2-74aee61d7d3a.png)

<br>

<br>

### 3.2 {% csrf token %}

- POST를 사용할 때는 `{% csrf token %}

- CSRF 공격을 막기 위한 최소한의 신원 확인 장치

- django 내부적으로 SCRF 공격을 막기 위한 미들웨어가 기본적으로 적용되어 있다.

  - settings.json 파일에 적용되어 있는 화면 

    ![1572323128300](https://user-images.githubusercontent.com/39547788/67767023-24708080-fa93-11e9-95f2-b18f022f1e7c.png)

    <br>

  - 얘가 존재하기 때문에, Form에서 POST 요청을 할 때  `{% csrf token %}`을 넣지 않으면 403 forbidden 에러를 뿜는다. 403 에러는 서버에는 정상적으로 접근을 하였으나, 권한이 없어서 접근하지 못하는 에러 이다.

  - GET 요청은 "야, HTML 파일 하나 줘!" 라고 하는 단순한 정보 조회 로직이지만, POST 요청은 서버측 DB(리소스) 에 변경을 요청하는 것이기 때문에 신원을 확인하는 절차가 없으면 임의의 공격을 통해 서버가 해킹당하게 된다.

  -  `{% csrf token %}`를 코드에 삽입하면, 실제 Form 태그를 개발자 도구로 찍어보면 hidden type 의 input 태그가 생기고 그 안에 암호화된 hash 값이 함께 전송되는 것을 확인할 수 있다. 

    - ![1572345402349](https://user-images.githubusercontent.com/39547788/67767051-28040780-fa93-11e9-84f0-e63c78057939.png)



<br>

<br>

## 4. 정적 파일 (Static Files)

> 정적 파일?
>
> - 별도의 가공 없이 사용자에게 그냥 전달만 해주면 되는 파일들
>
>   예 > `이미지, CSS, javaScript` 
>
> - 서버(프로그래머)가 미리 준비해주고, 사용자는 그냥 받아보기만 하면 된다.
>
> - 이미지의 경우 데이터 베이스를 통해 저장한 것이 아니라면, 일정한 주소를 통해 이미지를 불러와야 되는데 로컬에 저장했을 경우 그냥 경로만 적어서는 이미지를 불러 올 수 없다.
>
>   - django에서 제공하는 Static 파일 관리 방법을 준수해서 이미지를 불러와야 한다.

<br>

### 4.1 static 폴더 생성

- images 폴더와 stylesheets 폴더를 생성하고, 사진 파일과 .css 파일을 작성한다.

   ![1572335045454](https://user-images.githubusercontent.com/39547788/67767047-276b7100-fa93-11e9-8428-ef310277d832.png)  

  

  <br>

- Application 안에 있는 static 폴더를 알아서 찾는다.

  - 그 하위 폴더 경로부터 작성하면 된다.

    - 작성 요령

      ```python 
      <link rel="stylesheet" href="{% static 'stylesheets/sample.css' %}">
      <img src="{% static 'images/paul.jpg' %}" alt="paul" >
      ```

      

<br>

### 4.2 Static_sample

- local에 저장된 정적 파일을 사용할 떄는 `{% static '[경로]' %}`를 사용해야 한다.

  - views.py

    ```python 
    # 정적 파일
    def static_sample(request):
        return render(request, 'myapp/static_sample.html')
    ```

    <br>

  - urls.py

    ```python 
    urlpatterns = [
        path('static_sample/', views.static_sample),
        .
        .
        .
    ]
    ```

    <br>

  - static_sample.html

    ```html
    <!-- 폴더 안의 static 파일을 사용할 수 있도록 아래의 코드 반드시 삽입 -->
    {% load static %}
    
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Static 파일 실습</title>
            <link rel="stylesheet" href="{% static 'myapp/stylesheets/sample.css' %}">
        </head>
        <body>
            <h1>정적 파일 출력을 실습해봅시다.</h1>
            <img src="{% static 'myapp/images/paul.jpg' %}" alt="paul" >
        </body>
    </html>
    ```

    <br>

  - 실행 화면

    ![1572326349356](https://user-images.githubusercontent.com/39547788/67767027-25091700-fa93-11e9-826f-2c457d783206.png)

  <br>

- **static 이 아닌 실제 경로로 주어지면 정상적으로 동작하지 않는다.**

  - **반.드.시!** `{% static '[경로]' %}`로 경로를 작성하자

    - static_sample.html

      ```html
      <!-- 폴더 안의 static 파일을 사용할 수 있도록 아래의 코드 반드시 삽입 -->
      {% load static %}
      
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Static 파일 실습</title>
        <link rel="stylesheet" href="../static/stylesheets/sample.css">
      </head>
      <body>
        <h1>정적 파일 출력을 실습해봅시다.</h1>
        <img src="../static/images/paul.jpg" alt="" >
      </body>
      </html>
      ```



<br><br>

## 5. URL 로직 분리

> 지금까지 프로젝트 폴더 안에 있는 `urls.py` 에서 모든 URL 경로를 관리 했다. 그러나 Application 이 추가적으로 생기고, 관리해야할 경로 URL이 많아지면 매우 복잡해지는 것은 사실이다. 각자의 Application에 해당하는 URL은 Application이 직접 관리하도록 위임할 수 있다.
>
> - 각 Application 마다 urls.py 를 생성한다.
>
>   ![1572345887183](https://user-images.githubusercontent.com/39547788/67767053-28040780-fa93-11e9-9382-f82759e3db19.png)

<br>

### 5.1 Application 생성

- utilities Application 생성

  ```bash
  $python manage.py startapp utilities
  ```

  <br>

  ![1572326834067](https://user-images.githubusercontent.com/39547788/67767028-25091700-fa93-11e9-92ff-ac2096f6704c.png)

  <br>

  

  - 생성 결과 구조

    ![1572326848831](https://user-images.githubusercontent.com/39547788/67767030-25091700-fa93-11e9-922f-6b5519c28e0d.png)

    <br>

    

- utilities Application 등록

  - settings.py

    ![1572352497434](https://user-images.githubusercontent.com/39547788/67767031-25091700-fa93-11e9-9a02-cdbcc58cb8ca.png)

<br>

### 5.2 urls.py 분리

#### 5.2.1 프로젝트의 urls.py

```python 
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('static_sample/', views.static_sample),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('art/', views.art),
    path('result/', views.result),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('', views.index),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
```

<br>



#### 5.2.2 프로젝트의 urls.py 수정

> include 메서드를 사용해서 일정한 경로로 오는 요청들을 Application 의 urls.py에서 처리하도록 위임한다.
>
> ***** 반드시 모든 Application의urls.py에는 기본 코드가 있어야 한다.**
>
> ```python 
> from django.urls import path
> 
> urlpatterns = [
>     
> ]
> ```

<br>

- myapp/ 라고 시작하는 경로 (url)로 들어오면, myapp Application 안의 urls.py에서 처리한다.

  utilities/ 라고 시작하는 경로 (url)로 들어오면, utilities Application  안의 urls.py에서 처리한다.

  - include()를 사용하기 위해 include를 import한다.

    ```python 
    from django.contrib import admin
    from django.urls import path, include
    from myapp import views
    
    urlpatterns = [
        path('myapp/', include('myapp.urls')),
        path('utilities/', include('utilities.urls')),
        path('admin/', admin.site.urls),
    ]
    ```



#### 5.2.3 Application의 urls.py 

- myapp  Application 의 urls.py 수정

  - http : // localhost/myapp/

    - myapp으로 왔을 때의 root 경로 

  - http : // localhost/myapp/index

    - myapp의 index 페이지 경로

    - myapp의 index로 이동하기 위해서는 `from . import views`를 해야 한다.

      - `from . import views` : 같은 경로 (여기서는 myapp) 에 있는 views.py

      ```python 
      from django.urls import path
      # 같은 경로 안에 있는 views.py
      from . import views
      
      urlpatterns = [
          path('static_sample/', views.static_sample),
          path('user_new/', views.user_new),
          path('user_create/', views.user_create),
          path('art/', views.art),
          path('result/', views.result),
          path('throw/', views.throw),
          path('catch/', views.catch),
          path('', views.index),
      ]
      ```

  <br>

- utilities Application 의 urls.py 수정

  ```python 
  from django.urls import path
  
  urlpatterns = [
      
  ]
  ```

<br>

**그러나...!! 실행하면 아래의 에러 화면이 보인다.**

![1572329146332](https://user-images.githubusercontent.com/39547788/67767034-25a1ad80-fa93-11e9-940d-ea06ff9f2946.png)

<br>

- templates 폴더 내에서 action 등의 경로 요청 코드를 변경해야 한다.

  - 예 > throw & catch 코드 수정

    - throws.html

      ```html
      <form action = "/myapp/catch/" method="GET">
          <input type="text" name="message">
          <input type="submit" value="던져!">
      </form>
      ```

      

<br>

<br>



## 6. 이름공간 (Name space) 정리

![1572329457248](https://user-images.githubusercontent.com/39547788/67767035-25a1ad80-fa93-11e9-8000-bd19c296880f.png)



### 6.1 문제 상황

#### 6.1.1 myapp Application의 index.html 

- 각 Application의 루트 경로로 접속하면 myapp Application의 index.html 템플릿이 렌더링된다.

  - settings.py

    ![1572347204715](https://user-images.githubusercontent.com/39547788/67767054-289c9e00-fa93-11e9-80a8-afeb262c49f8.png)

    

    <br>

  - 어떠한 경우에도 myapp Application의 index.html 템플릿이 렌더링된다.

    - `http://127.0.0.1:8000/utilities/`

      ![1572329693615](https://user-images.githubusercontent.com/39547788/67767036-25a1ad80-fa93-11e9-91a3-42bcfa961a67.png)

      <br>

    - `http://127.0.0.1:8000/myapp/`

      ![1572329722734](https://user-images.githubusercontent.com/39547788/67767038-263a4400-fa93-11e9-97a4-4a8209c213af.png)

      <br>

  

  

#### 6.1.2 utilities Application의 index.html 

- 각 Application의 루트 경로로 접속하면 utilities Application의 index.html 템플릿이 렌더링된다.

  - settings.py

    ![1572347461878](https://user-images.githubusercontent.com/39547788/67767056-289c9e00-fa93-11e9-86a1-6a8f8cb301ac.png)

    <br>

  - 어떠한 경우에도 utilities Application의 index.html 템플릿이 렌더링된다.

    - `http://127.0.0.1:8000/myapp/`

      ![1572329799311](https://user-images.githubusercontent.com/39547788/67767042-26d2da80-fa93-11e9-8f95-3402f8d332a0.png)

      <br>

    - `http://127.0.0.1:8000/utilities`

      ![1572329816902](https://user-images.githubusercontent.com/39547788/67767043-276b7100-fa93-11e9-8d35-7c2dcdab3371.png)

  <br>

### 6.2 이름공간으로 해결

> django는 기본적으로 템플릿(스태택도 동일) 파일을 탐색할 때, 템플릿 폴더를 전부 모아놓고 순서대로 탐색한다.
>
> - 탐색하는 순서
>   - setting.py에 있는 INSTALLED_APPS 리스트 위에서 부터 차례로
>
> 따라서, 중간에 구분하는 폴더를 만들어 주지 않은 경우, 나는 myapp의 index.html 이라는 템플릿을 랜더링하고 싶었지만, 앱 등록 순서상 위에 있는 utilities의 index.html 템플릿이 랜더링 된다.
>
> 그냥 templates 폴더를 방문해서 파일을 찾지 않고, 해당 Application에 맞는 폴더를 찾기 위해 중간에 폴더를 하나 더 생성해 준다.

<br>



#### 6.2.1 templates 적용

**Application으로 구분을 해주는 것 (다른 Application에서 찾지 않도록)**

<br>

- 각 Application 안의 templates 폴더 아래에 Applicatxcion 이름으로 명명된 폴더를 생성한다.

- templates 아래의 html파일들을 위에서 생성한 Application 이름의 폴더로 옮겨준다.

  - 이름 공간 정리 완료 화면

  ![1572347856756](https://user-images.githubusercontent.com/39547788/67767060-29353480-fa93-11e9-92ad-1bacce4b6d32.png)

  <br>

- 각 Application의 views.py 파일에서 `return render()` 을 수정한다.

  >  `return render(request, 'index.html')`의 코드를  `return render(request, 'utilities/index.html')`로 수정한다.

  - 예 > 

    - myapp Application의 views.py

      ```python
      # Create your views here.
      def index(request):
          context = {
              'god' : "폴킴"
          }
          return render(request, 'myapp/index.html', context)
      
      
      # 정보를 던져줄 페이지
      def throw(request):
          return render(request, 'myapp/throw.html')
      ```

      <br>

    - utilities Application의 views.py

      ```python 
      # Create your views here.
      def index(request):
          return render(request, 'utilities/index.html')
      ```

      <br>



#### 6.2.1 static 폴더 적용

![1572331200835](https://user-images.githubusercontent.com/39547788/67767046-276b7100-fa93-11e9-88af-b0389eafd819.png)

<br>

<br>



## 7. 템플릿 상속

> HTML 각 파일마다 `! + tab`을 하면 동일한 CSS 입힐 때도 번거로움이 있다. 
>
> 상속은 기본적으로 코드의 재사용성에 초점을 맞춘다.
>
> 템플릿에서 반복되는 코드를 매번 일일이 치고 있을 여유가 없다. 반복되는 부분은 미리 만들어두고 가져다 쓰자!!

<br>

### 7.1 templates 폴더 통합

> 여러 Application의 templates 폴더를 프로젝트에서 하나의 templates 폴더로 관리한다. 각 Application의 templates 폴더 아래 해당 Application의 이름으로 된 폴더를 프로젝트의 templates 폴더의 하위로 이동시킨다. 

<br>

- 프로젝트 폴더 아래 config/ 아래에 templates 폴더를 생성

  - base.html 파일 추가 

    ![1572348211810](https://user-images.githubusercontent.com/39547788/67767000-21759000-fa93-11e9-8ee3-6d491451500b.png)

    <br>

  - 각 Application 의 templates 아래 Application 이름으로 명명된 폴더를  config/ 아래에 templates 폴더로 이동한다.

    ![1572348791073](https://user-images.githubusercontent.com/39547788/67767004-220e2680-fa93-11e9-8e05-c0e2d7a57adf.png)

<br>

### 7.2 settings.py 수정

- settings.py의 TEMPLATES 를 수정한다.

- `'APP_DIRS' : True` 로 설정했기 때문에 Application의 templates를 우선 탐색한다.

  ![1572348311155](https://user-images.githubusercontent.com/39547788/67767002-21759000-fa93-11e9-9290-74016793157e.png)



<br>

- 프로젝트 내의 templates를 탐색하도록 코드를 수정한다.

  ![1572348377318](https://user-images.githubusercontent.com/39547788/67767003-21759000-fa93-11e9-8a31-929ab9f9d613.png)

<br>

### 7.3 base.html 생성

- 상속받을 여러 html의 기본이 될 base.html 를 작성한다.

  - 작성 요령

    ```django
    {% block [name] %}
    	수정되는 내용을 이곳에 작성한다.
    {% endblock  %}
    ```

    <br>

  - base.html

    ```django
    {% load static %}
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>
        {% block title %}
        {% endblock  %}
      </title>
      {% block css %}
      {% endblock  %}
      
    </head>
    <body>
      <h1>base.html 템플릿을 상속 받았습니다. </h1>
      {% block body %}
        <!-- 이곳만 내용이 수정됨 --> 
      {% endblock %}
    </body>
    </html>
    ```

<br>

### 7.4 base.html 상속

- 상속 코드 작성 요령

  - 가장 상단에 `{% extends 'base.html' %}`를 작성한다.

    ```django
    {% extends 'base.html' %}
    
    {% block css %}
    <link rel="stylesheet" href="{% static 'myapp/stylesheets/sample.css' %}">
    {% endblock %}
    
    {% block body %}
    
    <!-- body 내용 -->
    
    {% endblock  %}
    
    ```

  <br>

- 모든 html 에 추가한다.

  - 예>

    - static_sample.html

      ```django
      {% extends 'base.html' %}
      <!-- 폴더 안의 static 파일을 사용할 수 있도록 아래의 코드 반드시 삽입 -->
      {% load static %}
      
      
      
      {% block css %}
      <link rel="stylesheet" href="{% static 'myapp/stylesheets/sample.css' %}">
      {% endblock %}
      
      
      {% block body %}
      
      <h1>정적 파일 출력을 실습해봅시다.</h1>
      <img src="{% static 'myapp/images/paul.jpg' %}" alt="paul" >
      
      {% endblock  %}
      ```

      - sample.css

        ```css
        body {
            background-color: darkorange;
        }
        ```

        <br>

      - 실행 화면

        ![1572350857743](https://user-images.githubusercontent.com/39547788/67767011-22a6bd00-fa93-11e9-9c8a-88083b92a21b.png)

      <br>

    - throw.html

      ```django
      {% extends 'base.html' %}
      
      {% block body %}
      
      <form action = "/myapp/catch/" method="GET">
          <input type="text" name="message">
          <input type="submit" value="던져!">
      </form>
      
      {% endblock  %}
      ```

      <br>

      - 실행 화면

        ![1572350823364](https://user-images.githubusercontent.com/39547788/67767010-22a6bd00-fa93-11e9-85ce-b1228a233180.png)

        <br>

    - index.html

      ```
      {% extends 'base.html' %}
      
      <h1>안녕 ~ 자소서의 신 {{god}} 님 </h1>
      
      {% block body %}
      <h1>안녕 ~ 자소서의 신 {{god}} 님 </h1>
      <h3>Welcome!! </h3>
      {% endblock  %}
      ```

      <br>

      - 실행 화면

        ![1572350793882](https://user-images.githubusercontent.com/39547788/67767009-220e2680-fa93-11e9-9b5c-3578377bdc87.png)





<br><br>

## 8. 개발환경 관리

> 협업 또는 프로젝트 공유 시,  프로젝트를 받는 다른 사람들이 프로젝트에 필요한 파이썬 패키지들을 정확하게 설치하기 위해 현재 설치되어 있는 패키지 목록을 넘긴다.
>
> - Git Hub에 올릴 때, 불필요하게 패키지들을 같이 올려 용량을 높일 필요가 없다.
>
>   목록만 넘겨주고 받는 사람이 본인 컴퓨터에 알아서 설치할 수 있게 환경 조성까지만 제공한다.
>
> - 파이썬 버전의 경우, 같이 올라가지 않기 때문에, 우리 프로젝트에 필요한 파이썬 패키지에 대한 정보는 되도록이면 README.md에 명시를 해준다.

<br>

### 8.1 패키지 목록 파일

- 현재 가상환경에 설치되어 있는 패키지 리스트 목록을 파일로 만들기

  - requirements.txt  파일 freeze

    ```bash
    $pip freeze > requirements.txt
    ```

<br>

​			![1572336291438](https://user-images.githubusercontent.com/39547788/67767049-28040780-fa93-11e9-85e7-17ad0e82df68.png)

<br>

- requirements.txt  

  ![1572349964603](https://user-images.githubusercontent.com/39547788/67767007-220e2680-fa93-11e9-9a08-6d3cbf591ba1.png)

  

<br>

### 8.2 패키지 자동 설치

- 패키지 리스트 목록을 읽어, 없는 패키지를 자동으로 설치하기

  - requirements.txt  를 읽어서 패키지를 자동으로 설치

    - 설치되어 있는 것은 PASS

      ```bash
      $pip install -r requirements.txt
      ```

      <br>

      ![1572336920504](https://user-images.githubusercontent.com/39547788/67767050-28040780-fa93-11e9-81b6-4f555445ac8c.png)

  

<br>