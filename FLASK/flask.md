# Flask

## 1. Start Flask

### 1.1 Install

- 첫 시작은 무조건 [공식문서](https://palletsprojects.com/p/flask/)를 참고하자!

<br>

### 1.1.1 가상 환경 진입

> 우리는 앞으로 글로벌 환경이 아닌, 우리 프로젝트에 필요한 버전과 패키지만 사용하기 위해 가상환경에서 개발을 진행한다.

- Python에 내장된 venv를 사용하기

  - 기본 사용법 

    ```bash
    $ python -m venv [가상환경이름]
    ```

  - 어디서든 사용하기 편하게 루트 디렉토리에 가상환경을 생성한다.

    ```bash
    student@M150122 MINGW64 ~
    $ python -m venv venv
    ```

    - 자유롭게 이름 설정이 가능하지만, 편하게 venv로 설정하길 권장 (학습 단계)

  - 가상 환경 설정

  - 가상 환경 종료

  - 이제 개발을 하기 전에 터미널에 **(venv)** 라는 가상환경 표시가 있는지 잘 확인하자!

    ![1571792920465](https://user-images.githubusercontent.com/39547788/67359433-2ec7e180-f59e-11e9-8e68-895d5ad2279e.png)

    <br>

    - 만약 이상한 점이 발견된 경우, `pip list` 라는 명령어를 통해 Flask가 제대로 설치되어 있는지 확인한다.

      ```bash
      $ pip list
      ```

      <br>

      - 실행 화면

        ![1571798467722](https://user-images.githubusercontent.com/39547788/67359457-312a3b80-f59e-11e9-8b23-57fc5c5646c0.png)

        

<br>

- flask 설치

  ![1571792986333](https://user-images.githubusercontent.com/39547788/67359435-2f607800-f59e-11e9-8118-b06204209513.png)



<br><br>

### 1.2 hello.py를 만들어 실행해보기 

#### 1.2.1 서버 실행 코드

- FLASK_APP : FLASK APP을 hello.py로 하고 flask를 실행한다.

  ```
  FLASK_APP=hello.py flask run
  ```

  ![1571793227770](https://user-images.githubusercontent.com/39547788/67359437-2f607800-f59e-11e9-8d64-79c03f63a2b9.png)

  <br>

  - 문제점
    - 서버를 실행하는 명령어가 너무 길다.
    - 코드 내용이 바뀌면 서버를 껐다 다시 켜야한다.

  

  <br>

#### 1.2.2 간단한 서버 실행 코드로 변경하기

- 파일 명을 app.py로 변경

  - 실행 명령어

    ```bash
    $ python app.py
    ```

  - app.py : Flask는 기본적으로 폴더에서 app.py를 실행시킨다.

  - 실제 개발 단계에서도 이름을 app.py로 하는 것을 권장한다.

  - 아래의 코드 추가 작성

    ```python
    # end of file !!!!!
    # debug 모드를 활성화해서 서버 새로고침을 생략한다.
    if __name__ == '__main__':
        app.run(debug=True)
    ```

<br>

<br>

### 1.3 간단한 페이지 랜더링 하기

- Flask import 하기

  ```python
  from flask import Flask
  app = Flask(__name__)
  ```

- 단순한 문자열 return 

  ```python
  from flask import Flask
  app = Flask(__name__)
  
  @app.route('/')
  def hello():
      return "Hello World!"
          
  @app.route('/dohyeon')
  def dohyeon():
      return "저는 무술가 입니다."
  ```

  <br>

  - 실행화면

    ![1571797030535](https://user-images.githubusercontent.com/39547788/67359448-3091a500-f59e-11e9-8e59-3a62abf682f4.png)

    <br>

![1571796943526](https://user-images.githubusercontent.com/39547788/67359445-2ff90e80-f59e-11e9-82b3-4f156f55a51e.png)



<br>

- html 태그 return 가능

  ```python 
  @app.route('/html')
  def html():
      return "<h1>태그도 사용할 수 있어요</h1>"
  ```

  <br>

  - 실행화면

    ![1571797054389](https://user-images.githubusercontent.com/39547788/67359450-3091a500-f59e-11e9-9661-6ac0e2d85115.png)

  <br>

- html 태그 여러 줄 return 가능

  ```python
  @app.route('/html_multiline')
  def html_multiline():
      return '''
      <ol>
          <li>안녕</li>
          <li>안녕2</li>
      </ol>
  
      '''
  ```

  <br>

  - 실행화면

    ![1571797073573](https://user-images.githubusercontent.com/39547788/67359453-3091a500-f59e-11e9-8b9e-43c920a73a3b.png)

<br><br>

### 1.4 동적 페이지 랜더링 하기

> 사용자가 URL 을 통해 입력한 값을 받아서 사용할 수 있다. 

<br><br>

### 1.5 Render_template 

> Templates 폴더를 미리 만들어두고 사용자에게 보여줄 수 있다.

- Templates 폴더 생성

  - Flask는 render_template 메서드를 사용할 때 기본적으로 루트 디렉토리에 있는 Templates라는 폴더를 탐색해서 html 파일을 찾는다.

    - FLASK 폴더 구조

    ![1571806807991](https://user-images.githubusercontent.com/39547788/67359466-325b6880-f59e-11e9-891a-a7aba0d1a3b1.png)

  - (주의) 뒤에 s를 빼면 jinja2 관련 에러가 발생!

    ```
    FLASK / Templates / [이곳에 html 파일들]
    ```

    <br>

- flask에서 제공하는 render_template 모듈 추가하기

  ```python 
  from flask import Flask, render_template
  ```

  - index.html 로 이동한다.

    - app.py

      ```python 
      from flask import Flask, render_template
      app = Flask(__name__)
      
      @app.route('/')
      def hello():
          return render_template('index.html')
      ```

      <br>

    - index.html

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>
          <h1>어서오세요. 안녕 안녕</h1>
      </body>
      </html>
      ```

    <br>

  - 실행화면

    ![1571796209885](https://user-images.githubusercontent.com/39547788/67359442-2ff90e80-f59e-11e9-90e2-cfd96ee5892b.png)



<br>

#### 1.5.1 render_template + parameter (1개)

- 사용자로부터 입력받은 데이터를 출력하는 greeting 페이지 작성

  - String type 의 변수명은 name 으로 데이터를 받는다.

    ```python
    <string:name>
    ```

  - render_template을 활용해 html 페이지에 전달받은 데이터를 출력한다.

    - 변수 사용 시,  **<u>중괄호 2개</u> {{ }}** !!!

    - app.py

      ```python
      # 동적 라우팅 (Variable Routing)
      @app.route('/greeting/<string:name>')
      def greeting(name):
          # return f'안녕~, {name}??'
          return render_template('greeting.html', html_name=name)
      ```

      <br>

    - greeting.html

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>
          안녕 하세요, {{html_name}} 님
      </body>
      </html>
      ```

      <br>

  - 실행 화면

    ![1571795124389](https://user-images.githubusercontent.com/39547788/67359438-2f607800-f59e-11e9-9790-b2220f5083d8.png)

<br>

#### 1.5.1 render_template + parameter (1개 & 2개)

- 세제곱을 돌려주는 cube 페이지 작성

  - 사용자한테 숫자값을 받아, 세제곱한 결과를 보여준다.

    - app.py

      ```python
      @app.route('/cube/<string:num>')
      def cube(num):
          a = int(num)
          b = a*a*a
          return render_template('cube.html', result=b)
      
      @app.route('/cube2/<int:num>')
      def cube2(num):
          return render_template('cube.html', result=num**3)
      
      # 변수 2개
      @app.route('/cube3/<int:num>')
      def cube3(num):
          return render_template('cube3.html', number=num, result=num**3)
      ```

      <br>

    - cube.html

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>
          세제곱한 값은 {{result}} 입니다. 
      </body>
      </html>
      ```

    <br>

    - cube3.html

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>
          {{number}} 을/를 세제곱한 값은 {{result}} 입니다. 
      </body>
      </html>
      ```

      <br>

  - 실행화면

    - cube

      ![1571795873325](https://user-images.githubusercontent.com/39547788/67359440-2ff90e80-f59e-11e9-83e2-88a1dd5e2a2e.png)

      <br>

    - cube2

      ![1571795858805](https://user-images.githubusercontent.com/39547788/67359439-2f607800-f59e-11e9-8e91-5119c1fd5a94.png)

      <br>

    - cube3

      ![1571796820127](https://user-images.githubusercontent.com/39547788/67359443-2ff90e80-f59e-11e9-870b-773ec7c8738e.png)

<br><br>

### 1.6 Jinja2 템플릿 엔진 활용하기

> Flask가 가지고 있는 Joinja1라는 내장 템플릿 엔진을 활용해서 꾸밀 수 있다. 

<br>

#### 1.6.1 조건문

- 조건문 문법

  ```python 
  {% if [조건문] %}
  
  {% else %}
  
  {% endif %}
  ```

  <br>

  - URL을 통해 입력받은 값이 '도현'인 경우와 그렇지 않은 경우를 구분해 화면 출력을 달리한다.

    - app.py

      ```python 
      @app.route('/greeting/<string:name>')
      def greeting(name):
          return render_template('greeting.html', html_name=name)
      ```

      <br>

    - greeting.html

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>
          <h1>당신의 이름은 {{html_name}} 입니다. </h1>
              {% if html_name == '도현'%}
                  <p>어서오세요, 유단자여..</p>
              {% else %}
                  <p>제발 무술을 배우세요..</p>
              {% endif %}
      
      </body>
      </html>
      ```

    <br>

  - 실행화면

    - 도현

      ![1571797959014](https://user-images.githubusercontent.com/39547788/67359454-312a3b80-f59e-11e9-9a8b-7086a9b5a885.png)

      <br>

    - 선아

      ![1571797973446](https://user-images.githubusercontent.com/39547788/67359455-312a3b80-f59e-11e9-8849-72a0c5ff94f1.png)

<br>

#### 1.6.2 반복문

- 반복문 문법

  ```python 
  {% for i in array_list %}
  
  {% endfor %}
  ```

  - 영화 목록을 받아 list로 출력하기 

    - app.py

      ```python 
      @app.route('/movies')
      def movie():
          movie_list = ['82년생 김지영', '조커', '엔드게임', '궁예']
          return render_template('movies.html', movies=movie_list)
      ```

      

    - movies.html

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>
      
          <h2>영화 목록</h2>
          <ul>
              {% for movie in movies %}
                  <li>{{movie}}</li>
              {% endfor %}
              
          </ul>
      
      </body>
      </html>
      ```

    <br>

  - 실행화면

    ![1571797992965](https://user-images.githubusercontent.com/39547788/67359456-312a3b80-f59e-11e9-8520-b57a1defdd6d.png)



<br><br>

## 2. 응답-요청 (Request-Response)

### 2.1 Ping / Pong

#### Ping

- 사용자가 일정한 주소로 요청을 보내면, 사용자가 어떠한 값을 입력할 수 있는 Form이 담겨있는 페이지를 보여준다. 

#### Pong

- 사용자로부터 Form 입력 데이터를 전달받고, 데이터를 가공해서 다시 보여준다.

- Ping / Pong

- Method="GET" : 서버 측에 어떤 OO를 달라고 요청을 보냄 

  - 요청 코드 : user_name = request.args.get('user_name')

  - app.py

    ```python 
    # ping : 사용자로부터 입력을 받을 Form 페이지를 넘겨준다. 
    @app.route('/ping')
    def ping():
        return render_template('ping.html')
    
    # pong : 사용자로부터 Form 데이터를 전달받아서 가공한다. 
    # ping에서부터 데이터를 받음
    # request 추가
    @app.route('/pong')
    def pong():
        user_name = request.args.get('user_name')
        return render_template('pong.html', user_name=user_name)
    ```

  <br>

  - ping.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    
    <body>
        <!-- 사용자가 submit을 누르면 데이터가 pong에서 가공됨 -->
        <form action="/pong" method="GET">
            이름 : <input type="text" name="user_name"><br>
            <input type="submit"><br>
        </form>
    </body>
    
    </html>
    ```

    <br>

  - pong.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h2>{{user_name}} 님 안녕하세요! 데이터가 저희 서버로 들어왔어요.</h2>
    </body>
    </html>
    ```

    <br>

  

  - 실행화면

    - Text Form 에 이름 입력

      ![1571804440398](https://user-images.githubusercontent.com/39547788/67359458-31c2d200-f59e-11e9-8350-7a1562754cc2.png)

      <br>

    - 사용자가 입력한 데이터를 전달받아 화면에 출력

      ![1571804484349](https://user-images.githubusercontent.com/39547788/67359459-31c2d200-f59e-11e9-948c-e5c6bd2ff4ec.png)

<br>

### 2.2 Fake Naver & Google

> 위 Ping / Pong 구조에서 온전히 우리 웹 서비스 내에서 요청과 응답 프로세스를 구현했다. 하지만, 사용자로부터 요청만 받은 뒤, 데이터를 처리해서 돌려주는 응답 프로세스를 다른 서버 측에 넘겨줄 수 있다. 



<br>

#### Fake naver

- Form에서 검색어를 입력받아 naver 검색 수행

  - app.py

    ```python 
    # fake naver
    @app.route('/naver')
    def naver():
        return render_template('naver.html')
    ```

    <br>

  - naver.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <form action="https://search.naver.com/search.naver">
            <input type="text" name="query">
            <input type="submit">
        </form>
    </body>
    </html>
    ```

    <br>

- 실행화면

  - Form 에 검색할 검색어 입력

    ![1571805638464](https://user-images.githubusercontent.com/39547788/67359460-31c2d200-f59e-11e9-9436-d1af30150e79.png)

    <br>

  - naver에서 검색을 수행한다. 

    ![1571805680196](https://user-images.githubusercontent.com/39547788/67359461-31c2d200-f59e-11e9-8471-30b74e3b91c7.png)

<br>

#### Fake  google

- Form에서 검색어를 입력받아 google 검색 수행

  - app.py

    ```python
    # fake google
    @app.route('/google')
    def google():
        return render_template('google.html')
    ```

    <br>

  - google.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <form action="https://www.google.com/search">
            <input type="text" name="q">
            <input type="submit">
        </form>
    </body>
    </html>
    ```

    <br>

- 실행화면

  - Form 에 검색할 검색어 입력

    ![1571805725495](https://user-images.githubusercontent.com/39547788/67359463-325b6880-f59e-11e9-92a0-3a305ae4e237.png)

    <br>

  - google에서 검색을 수행한다. 

    ![1571805756826](https://user-images.githubusercontent.com/39547788/67359464-325b6880-f59e-11e9-827d-bc02bdb3280b.png)

<br>

### 2.3 GodMadeMe (신이 나를 만들 때)

> [신이 나를 만들 때](https://kr.vonvon.me/quiz/2998) 를 구현해보자.

- 사용자로부터 이름을 입력받아, 랜덤으로 특성 3개를 사용자에게 보여준다.

  - app.py

    ```python 
    import random
    
    # 사용자로부터 이름을 입력받을 Form 페이지
    @app.route('/vonvon')
    def vonvon():
        return render_template('vonvon.html')
    
    
    # 전달받은 이름을 기준으로 넘겨줄 각종 정보를 가공해서 돌려주는 (응답) 로직!
    @app.route('/godmademe')
    def godmademe():
    
        # 1. 사용자가 입력한 데이터를 가져온다. (Flask의 request 기능 사용)pytho
        user_name = request.args.get('user_name')
    
        # 2. 사용자에게 보여줄 여러가지 재밌는 특성 리스트를 만든다.
        first_list = ['잘생김', '못생김', '많이 못생김', '많이 잘생김', '앙주']
        second_list = ['자신감', '귀찮음', '쑥쓰러움', '열정적임']
        third_list = ['허세', '물욕', '식욕', '똘기']
    
        # 3. 특성 리스트에서 랜덤으로 하나씩을 선택한다. 
        first_choice = random.choice(first_list)
        second_choice = random.choice(second_list)
        third_choice = random.choice(third_list)
    
    
        # 4. 가공한 정보를 템플릿에 담아서 사용자에게 보여준다.
        return render_template('godmademe.html', user_html=user_name, first_html=first_choice, second_html=second_choice, third_html=third_choice)
    ```

    <br>

  - vonvon.html

    - text  form의 속성을 `name="user_name"`으로 설정했기 때문에 서버에서 user_name이라는 이름으로 받을 수 있다.

      - form 의 action 설정하기!  `form action="/godmademe"`

      ```html
      <!DOCTYPE html>
      <html lang="en">
      
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      
      <body>
          <form action="/godmademe">
              <input type="text" name="user_name" placeholder="당신의 이름을 입력해주세요.  :) ">
              <input type="submit">
          </form>
      </body>
      
      </html>
      ```

    <br>

  - godmademe.html

    - 랜덤으로 생성된 3개의 parameter를 전달받아 화면에 출력한다.

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta http-equiv="X-UA-Compatible" content="ie=edge">
          <title>Document</title>
      </head>
      <body>
          <h1>신이 {{user_html}} 을 만들 때</h1>
          <p>{{first_html}}</p>
          <p>{{second_html}}</p>
          <p>{{third_html}}</p>
      </body>
      </html>
      ```

  <br>

- 실행화면

  - 사용자 이름 입력

    ![1571810505542](https://user-images.githubusercontent.com/39547788/67366460-81a99500-f5ae-11e9-8ff7-96062e79e239.png)

    <br>

  - 신이 김선호를 만들 때

    ![1571810473322](https://user-images.githubusercontent.com/39547788/67366459-81a99500-f5ae-11e9-99cd-2b6661a2a96f.png)

    <br>

  - 신이 이수연을 만들 때 (CSS 추가)

    ![1571814062914](https://user-images.githubusercontent.com/39547788/67366465-82422b80-f5ae-11e9-9833-a50dd0f8c5b6.png)

<br>



### 2.4 아스키 아트 (ASCII Art)

> [ASCII Art API](http://artii.herokuapp.com/) 를 이용해 문자를 넘겨 그림을 그린다.
>
> - 파이썬 requsets 모듈 숙달하기 (API요청)

<br>

- API를 사용하기 위해 가상환경 (venv)에서 requests 모듈을 설치한다.

  ```bash
  $ pip install requests
  ```

  - 설치 확인

    ![1571811793839](https://user-images.githubusercontent.com/39547788/67366461-81a99500-f5ae-11e9-9af3-721c493cd17e.png)

  <br>

- 설치된 requests 모듈을 import 한다.

  ```python 
  import random, requests
  ```

  <br>

- 사용자로부터 입력을 받은 text 입력받고, 랜덤으로 font를 설정하여 ASCII ART로 변환해서 돌려준다.

  - app.py

    ```python 
    # 1. 사용자로부터 임의의 텍스트를 입력받아서, 아스키 아트로 변환해서 돌려준다.
    # 이때, ASCII Art의 폰트는 랜덤으로 하나를 지정해서 변환한다.
    @app.route('/catch')
    def catch():
        return render_template('catch.html')
    
    
    @app.route('/result')
    def result():
        # 1. 사용자가 입력한 Form 데이터를 가져온다.
        text = request.args.get('word')
    
        # 2. ARTII API로 요청을 보내서, 응답 결과를 변수에 담는다. (폰트 정보)
        # requests.get([URL]) 을 통해 가져온 데이터를 text 로 담는다.
        fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    
        # 3. 가져온 폰트들을 리스트 형태로 바꾼다.
        fonts_list = fonts.split('\n')
    
        # 4. 폰트 하나를 랜덤으로 선택한다.
        my_font = random.choice(fonts_list)
    
        # 5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 담아서 API에게 요청한다.
        result = requests.get(f'http://artii.herokuapp.com/make?text={text}+art&font={my_font}').text
    
        # 6. 최종 결과물을 사용자에게 돌려준다.
        return render_template('result.html', result=result)
    ```

    <br>

  - catch.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    
    <body>
        <form action="/result">
            <input type="text" name="word" placeholder="텍스트를 입력해주세요.  :) ">
            <input type="submit">
        </form>
    </body>
    
    </html>
    ```

    <br>

  - result.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    
    <body>
        <pre>
                {{result}}
        </pre>
    </body>
    
    </html>
    ```

- 실행화면

  - ASCII ART를 수행할 단어 입력

    ![1571812907008](https://user-images.githubusercontent.com/39547788/67366463-82422b80-f5ae-11e9-8404-4b6283005f3d.png)

    <br>

  - ASCII ART_1

    ![1571812880543](https://user-images.githubusercontent.com/39547788/67366462-81a99500-f5ae-11e9-823e-e2bf3ee507e6.png)

    <br>

  - ASCII ART_2

    ![1571812921010](https://user-images.githubusercontent.com/39547788/67366464-82422b80-f5ae-11e9-8792-e783b8dadc44.png)

    <br>

<br>