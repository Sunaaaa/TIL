### django

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



#### MVC 

- Model
- View
- Controller



#### MTV 패턴

- Model : 데이터를 관리, 데이터베이스의 모양, 형태를 정의

- Template : 사용자가 보는 화면

- View : 중간 관리자 , Model에 있는 데이터 베이스의 데이터를 꺼내서 가공한다.

  - @app.route() 안에 정의된 함수와 같은 역할

- url.py

  ```python 
  @app.route([request])
  ```

  



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

  - pip install django

    ![1572227659826](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572227659826.png)

  - `pip list` : django 설치 확인

  - `python -m django --version`

    ![1572227722348](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572227722348.png)