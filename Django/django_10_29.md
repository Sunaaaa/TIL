# 19.10.29 : Start Django2

## 1. HTML Form Tag

- Static Web VS Dynamic Web
  - Static Web 
    - 단순히 html 페이지 여러 개로 구성되어 있는 웹 서비스
  - Dynamic Web
    - 데이터 베이스에 변동을 주어서 데이터 베이스에 따라 웹 페이지의 내용이 바뀌는 웹 서비스

<br>

> Form을 통해 사용자로부터 정보를 받거나 받은 정보를 가공하는 등의 로직을 구현했다.
>
> Dynamic Web을 구현하기 위해서는 Form을 통해서 정보를 요청하는 절차가 반드시 필요하다.

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



### GET VS POST

GET 

- 서버 측에 데이터를 보낼 때 URL에 다 보임

POST

- 내부적으로 안쪽에 숨겨서 보낸다.

HTTP BODY라는 곳에 숨겨서 보낸다.

<br>

<br>

### GET

실습 

- throw 해서 catch

  - views.py

    ```python 
    # 정보를 던져줄 페이지
    def throw(request):
        return render(request, 'throw.html')
    
    # 사용자로부터 정보를 받아서 다시 던져줄 페이지
    # request를 통해서 정보가 들어온다.
    def catch(request):
        # GET으로 보내면 request를 통해서 GET 정보가 들어온다. JSON/딕셔너리
        message = request.GET.get('message')
        context = {
            'message' : message
        }
        
        return render(request, 'catch.html', context)
    ```

    

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

    

  - throw.html

    ```html
    <form action = "/catch/" method="GET">
      <input type="text" name="message">
      <input type="submit" value="던져!">
    </form>
    ```

  - catch.html

    ```html
    <h1>니가 보낸 정보를 잘 받았다.</h1>
    <h1>그 정보의 내용을 <span style="color : red">{{message}}</span> 이란다!</h1>
    ```

- 실행 화면

  ![1572312832847](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572312832847.png)

- 실행 화면

  ![1572312993514](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572312993514.png)



<br>

<br>

#### ASCII ART

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

    

  - art.html

    ```html
    <form action = "/result/" method="GET">
      <input type="text" name="text">
      <input type="submit" value="ASCII ART!">
    </form>
    ```

    

  - result.html

    ```html
    <h2>ASCII ART</h2>
    
    <iframe width="500" height="500" src={{art}}></iframe>
    ```

  - 실행 화면

    ![1572314573687](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572314573687.png)

  - 실행 화면

    ![1572314589073](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572314589073.png)

  

<br><br>