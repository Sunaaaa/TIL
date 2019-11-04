# Seed Data(Initial Data) 입력하기

> 우리가 애플리케이션을 제작할 때, 미리 준비해둔 데이터 혹은 애플리케이션 테스트용 데이터가 필요한 경우가 종종 있다. 이때, 우리가 하드 코딩으로 일일이 넣을 수 있다. 그러나 fixures라는 기능을 이용해서 준비해둔 데이터를 쉽게 데이터 베이스에 넣을 수 있다. 

<br>

<br>

## 1. Seed Data  활용

- Seed Data  활용하는 방법

  1. 애플리케이션의 데이터 베이스를 하드 코딩으로 미리 만든다.

     - 이후 `dump data` 명령어를 통해 fixture 데이터 형태로 만들어두고,

       데이터 베이스를 초기화시켜도 `loaddata` 명령어를 통해 다시 데이터를 불러와서 사용할 수 있다. 

  2. 이미 Seed Data를 제공받았을 경우, 그냥 fixtures 폴더에 넣어두고 불러와서 사용한다.

- fixture 데이터 내용을 바꾸거나, 모델링 해둔 애용을 바꾸고 싶으면, 반드시 다시 `loaddata` 과정을 수행한다.



<br>

<br>

## 1. 이미 데이터가 있는 경우

- `manage.py dumpdata > [파일명]`

  - 현재 애플리케이션에서 가지고 있는 데이터를 빼낼 수 있다.

  - json 파일을 직접 작성하지 않고 현재 DB에 있는 데이터를 json으로 뽑아내고 싶다면 아래의 명령을 사용하면 된다.

  - 이전 DB가 날아가더라도 dumpdata를 통해 빼둔 데이터들을 다시 한번 활용할 수 있다. 

    ```bash
    $ manage.py dumpdata > movies.json
    ```

    <br>

    - dump 뜨기

      ![1572834568676](https://user-images.githubusercontent.com/39547788/68100457-725e0c00-ff0b-11e9-8399-7c9d22518572.png)

      <br>

    - movies.json 파일이 생생된다. 

      - movies.json 생성 확인!

      ![1572834611715](https://user-images.githubusercontent.com/39547788/68100458-725e0c00-ff0b-11e9-8362-f6247515f604.png)

      <br>

      - movies.json 

        ```json
        [
            {
                "model": "movies.movie",
                "pk": 1,
                "fields": {
                    "title": "\uae00\ub798\uc2a4",
                    "title_en": "Glass",
                    "audience": 339707,
                    "open_date": "2019-01-09",
                    "genre": "\ub4dc\ub77c\ub9c8",
                    "watch_grade": "15\uc138\uc774\uc0c1\uad00\ub78c\uac00",
                    "score": 7.69,
                    "poster_url": "https://movie-phinf.pstatic.net/20181227_126/1545900402100CiQHx_JPEG/movie_image.jpg",
                    "description": "24\uac1c\uc758 \uc778\uaca9\u318d\uac15\ucca0 \uac19\uc740 \uc2e0\uccb4\u318d\ucc9c\uc7ac\uc801 \ub450\ub1cc \ud1b5\uc81c\ubd88\uac00\ud55c 24\ubc88\uc9f8 \uc778\uaca9 \ube44\uc2a4\ud2b8\ub97c \uae68\uc6b4 \ucf00\ube48, \uac15\ucca0 \uac19\uc740 \uc2e0\uccb4 \ub2a5\ub825\uc744 \uc9c0\ub2cc \uc758\ubb38\uc758 \ub0a8\uc790 \ub358, \ucc9c\uc7ac\uc801 \ub450\ub1cc\ub97c \uc9c0\ub2cc \ubbf8\uc2a4\ud130\ub9ac\ud55c \uc124\uacc4\uc790 \ubbf8\uc2a4\ud130 \uae00\ub798\uc2a4, \ub9c8\uce68\ub0b4 \uadf8\ub4e4\uc774 \ud55c \uc790\ub9ac\uc5d0 \ubaa8\uc774\uac8c \ub418\uace0 \uc774\ub4e4\uc758 \uc874\uc7ac\uac00 \uc138\uc0c1\uc5d0 \ub4dc\ub7ec\ub098\uba74\uc11c \uc608\uc0c1\uce58 \ubabb\ud55c \uc77c\uc774 \ubc8c\uc5b4\uc9c0\ub294\ub370..."
                }
            },
            {
                "model": "contenttypes.contenttype",
                "pk": 1,
                "fields": {
                    "app_label": "movies",
                    "model": "movie"
                }
            },
                 
            .
            .
            .
                
            
            {
                "model": "auth.permission",
                "pk": 28,
                "fields": {
                    "name": "Can view session",
                    "content_type": 7,
                    "codename": "view_session"
                }
            }
        ]
        ```

        

    

  <br>

  <br>

## 3. 준비해둔 fixture 데이터들을 넣고 싶은 경우

> **csv** (Comma-Seperated Values)
>
> - 데이터 들을 콤마(,)로 구분해서 비교적 간단한 Text 형태의 포맷으로 바꾼 형식
> - 스프레드 시트, 엑셀에서 주로 활용한다. 
> - 불필요한 서식이 모두 제거되어 데이터의 크기가 축소된다.
>
> 
>
> **json으로 테스트 데이터를 저장해서 migration 전에 load한다.**
>
> 
>
> fixture 는 장고가 데이터 베이스에 import 할 수 있는 데이터의 모음으로 아래의 세가지 포맷의 fixture들을 불러올 수 있다.
>
> - JSON
> - XML
> - YAML
>
> 
>
> **프로젝트를 진행할 때 Seed Data(Initial Data)를 제공받았을 경우, Seed Data 형식을 먼저 확인하고 형식에 맞게 모델링 하자!**

<br>

<br>





### 3.1 스프레드시트를 이용해서 csv 파일로 빼기

- pk 추가 (Model과 같은 형식으로 구성해줌)

- 쉼표로 구분되는 csv 형식으로 저장한다.

  ![1572840133381](https://user-images.githubusercontent.com/39547788/68100459-725e0c00-ff0b-11e9-88ce-e3b84c8f9152.png)

<br>



### 3.2 fixtures 폴더 생성

- fixtures 폴더를 생성하고, 위에서 생성한 csv 파일을 넣는다.

  ![1572840414135](https://user-images.githubusercontent.com/39547788/68100460-72f6a280-ff0b-11e9-9168-4b2d045d3e43.png)



<br>

### 3.3 csv2json-fixture

> This script can be used to convert CSV data to [Django fixtures](https://docs.djangoproject.com/en/stable/howto/initial-data/) JSON format.

<br>

- csv2json-fixture를 다운받아 movies.csv 파일을 넣는다.

  

  ![1572841919112](https://user-images.githubusercontent.com/39547788/68100449-712cdf00-ff0b-11e9-82bb-93693f233832.png)

<br>

- csv2json.py의 내용 변경 For 한글 인코딩

  ![1572840923923](https://user-images.githubusercontent.com/39547788/68100462-72f6a280-ff0b-11e9-93f7-9942ecd16ef7.png)

  <br>

  

- csv2json.py가 있는 곳에서 git bash를 열어 csv 파일을 json 형식의 파일로 저장한다.

  ```bash
  $ python csv2json.py movies.csv movies.Movie
  ```

  <br>![1572841822540](https://user-images.githubusercontent.com/39547788/68100463-72f6a280-ff0b-11e9-96cf-e75c8dce4f77.png)

  <br>

  

- movies.json 파일 생성 확인

  ![1572841839807](https://user-images.githubusercontent.com/39547788/68100448-712cdf00-ff0b-11e9-83f9-08d123156fe6.png)

  <br>

- fixtures 밑에  movies.json 을 넣는다.

  ![1572842463175](https://user-images.githubusercontent.com/39547788/68100452-71c57580-ff0b-11e9-84c8-e50c6c84fd97.png)

  <br>



- 데이터 베이스에 데이터 넣기

  ```bash
  $ python manage.py loaddata movies.json
  ```

  <br>

  ![1572842527046](https://user-images.githubusercontent.com/39547788/68100453-71c57580-ff0b-11e9-8bca-f57d50fa7a69.png)

  <br>

  - 실행 전

    ![1572842617511](https://user-images.githubusercontent.com/39547788/68100455-71c57580-ff0b-11e9-9d6f-746700caf58d.png)

    <br>

  - 실행 후

    ![1572842614704](https://user-images.githubusercontent.com/39547788/68100454-71c57580-ff0b-11e9-8b18-669e02a0139e.png)





<br>

<br>

## 4 django가 Fixture 파일을 찾는 방식

- 기본적으로 애플리케이션 안에 있는 `fixtures` 라는 디렉토리를 탐색한다.

  - 구조

  ![1572842261401](https://user-images.githubusercontent.com/39547788/68100450-712cdf00-ff0b-11e9-98d5-f978e70f990d.png)

  <br>

- 환경설정에 `FIXTURE_DIR` 옵션을 통해 django가 바라보는 또 다른 디렉토리를 정의할 수 있다. 

  - `loaddata`  명령어를 수행할 때, 다른 경로보다 우선적으로 탐색한다.

    

<br>



















