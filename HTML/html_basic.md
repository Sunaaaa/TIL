# Web 개념

#### 1.1 Static Web VS Dynamic Web

- Static Web

  - 정적인 웹
  - 클라이언트가 서버 측에 정보를 달라고 요청을 하면, 서버는 클라이언트에게 준비해온 정보를 건네준다.

  <br>

- Dynamic Web

  - 동적인 웹
  - 동적동적동적동적동적
  - 유후윻우흐우후읗우흥후





## HTML

#### Hyper Text

- 비 선형적으로 이루어진 텍스트
- Hyper Linl를 통해 텍스트를 이동한다.
- Hyper Text를 주고 받는 규약 (Hyper Text Transfer Protocol)
- HTTP (S)



- HTML 파일 : HTML 로 작성된 문서 파일
- GET 요청 : HTML 로 작성된 문서파일 단 하나를 Client에 제공
- POST 요청 : 



- meta 정보 
- Open Graph

#### 웹 페이지 3요소

- HTML
- CSS
- JavaScript



#### 1. HTML 문서 기본 구조

```html
<!-- 1. !DOCTYPE : 문서 형식 선언부 -->
<!DOCTYPE html>
<!-- 2. html : 문서 시작과 끝 지정 -->
<!-- 2-1. lang : 스크린 리더, 검색 엔진 필터링 도움 -->
<html lang="ko">

<!-- 3. head : 브라우저에게 건너줄 정보 -->
<head>
    <!-- 3-1. text의 Encoding 방식 -->
    <meta charset="UTF-8">
    <title>인트로 페이지</title>
</head>

<!-- 4. body : 실제 사용자가 볼 내용 -->
<body>

</body>
</html>
```

<br>

#### 2. Tag와 DOM TREE

#### 2-1 주석 (Comment)

```html
<!-- 주석 내용 -->
```

<br>

#### 2-2 요소 (Element)

- 여는 태그 닫는 태그
- 태그와 내용으로 구성 

<br>

#### 2-3 Self-closing element

- 닫는 태그가 없는 태그도 존재

  ```html
  <img src="url"/>
  ```

#### 2-3-1 속성 (Attribute)

- id, class, style 속성은 태그와 상관없이 모두 사용 가능

  ```html
  <a href="https://google.com"> </a>
  ```

  - 공백 없음
  - 쌍 따움표

<br>

#### 2-4 DOM 트리

- 태그는 중첩되어 사용가능
- 형제 관계

<br>

#### 2-5 시맨틱 태그 (Semantic Tag)

- Semantic  : 단순히 보여주는 것이 아니라 의미를 부여 한다.
- div 등의 태그에 의미를 부여함
- header, nav, article, aside, footer 등 

<br>

#### 2-6 검색 엔진 최적화 (SEO)

- Search Engine Optimizer



3 HTML Tag 활용

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
        <!-- 제목 (Heading) -->
        <h1>나는 h1!</h1>
        <h2>나는 h2!</h2>
        <h3>나는 h3!</h3>
        <h4>나는 h4!</h4>
        <h5>나는 h5!</h5>
        <h6>나는 h6!</h6>

        <!-- 글씨 굵게 (Blod) -->
        <p><b>저는 굵은 글씨에요.</b></p>
        <p><strong>저는 굵은 글씨에요. (권장)</strong></p>

        <!-- 글씨 기울이기 (Italic) -->
        <p><i>기울기울</i></p>

        <!-- 글씨 기울이기 (emphasized) -->
        <p><em>저는 강조 의미를 가진 기울임 입니다. </em></p>

        <!-- 글씨 하이라이트 (Highlighted) -->
        <p>이곳은 <mark>멀티캠퍼스 역삼</mark> 입니다.</p>
        <!-- 글씨 하이라이트 (Highlighted) -->
        <p>이곳은 <mark>멀티캠퍼스 역삼</mark> 입니다.</p>

        <!-- del (취소선) / ins (밑줄) -->
        <p>This is <del>del</del></p>
        <p>This is <ins>ins</ins></p>

        <!--sub (아래 첨자) / suo (윗 첨자) -->
        <p>This is <sub>sub</sub></p>
        <p>This is <suo>suo</suo></p>

        <!--p / br -->
        <!-- ctrl + alt + 아래 화살표 -->
        <p>
                This is p!<br>
                This is p!                    
        </p>

        <!-- pre -->
        <pre>
                from flask import flask
                app = Flask(__name__)
        </pre>
    
        <!-- q / blockquote -->
        <q>
            선아 said, "HTML은 꿀잼."
        </q>
        <blockquote>
            Hello, HTML!
        </blockquote>
    
        <!-- ol / ul / li -->
        <!-- 순서가 있는 리스트 -->
        <ol>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
        </ol>

        <!-- 순서가 없는 리스트 -->
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
        </ul>

    </body>
</html>
```



3-1. list의 bullet 모양 변경

3-2. a 태그의 default 값은 현재 창에서 띄우기 

- 새로운 창으로 띄우고 싶을 때는 target = "_blank"를 지정한다.

```
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>마크업 연습 - 프로그래밍 교육</title>
</head>
<body>
     <h1>프로그래밍 교육</h1>
     <hr>
     <!-- a 태그
        _self : 현재 창에서 이동 (default) 
        _blank : 새로운 창에서 이동 -->
     <a href="https://docs.python.org/3/" target="_blank">
        <h2>파이썬</h2>
     </a>

     <h3>Number Type</h3>
     <p>파이썬에서 숫자형은 아래와 같이 있다.</p>
     <ol>
        <li>int</li>
        <li>float</li>
        <li>complex</li>
        <li><del>str</del></li>
    </ol>
    

     <h3>Sequence</h3>
     <p>파이썬에서 시퀀스는 아래와 같이 있다.</p>


     <p><strong>시퀀스는 for문을 돌릴 수 있다.</strong></p>
     <ol>
        <li>str</li>
        <li>list</li>
        <li>tuple</li>
        <li>range</li>
    </ol>


    <hr>
<!-- a 태그
        _self : 현재 창에서 이동 (default) 
        _blank : 새로운 창에서 이동 -->
    <a href="https://developer.mozilla.org/en-US/" >
        <h2>파이썬</h2>
    </a>
    <h2>웹</h2>
    <h3>기초</h3>
    <ul>
       <li style="list-style-type: square">HTML</li>
       <li>CSS</li>
    </ul>

</body>
</html>
```



### 01_tag.html

- 다양한 태그 연습
- 프로그래밍 교육
  - hr
  - p / pre
  - ul / ol
  - a 태그
  - 동영상 삽입
  - img



### 02_table.html

- table 태그를 활용하여 점심 메뉴 테이블을 만들기

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
      <table border="1px solid red">
              <tr>
                  <th></th>
                  <th>월</th>
                  <th>화</th>
                  <th>수</th>
              </tr>
              <tr>
                  <td>A코스</td>
                  <td rowspan="2">짬뽕</td>
                  <td colspan="2">초밥</td>
              </tr>
              <tr>
                  <td>B코스</td>
                  <td>김치찌개</td>
                  <td>삼계탕</td>
              </tr>
      </table>
  </body>
  </html>
  ```

  

- 실행화면

  ![1571708558215](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571708558215.png)



### 03_festival.html

- tabel 태그를 활용해 음악 페스티벌 타임 테이블 만들기

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <style>
          body{
              font-weight: bold;
          }
  
          td{
              border: 1px solid gray;
          }
      </style>
  </head>
  <body>
      <h1>2019 타임 테이블</h1>
      <table>
          <tr>
              <th>TIME</th>
              <th>INDOOR</th>
              <th colspan="2">OUTDOOR</th>
          </tr>
          <tr>
              <td> </td>
              <td>소극장</td>
              <td>잔디마당</td>
              <td>대공연장</td>
          </tr>
          <tr>
              <td>10:00</td>
              <td rowspan="2">안녕하신가영</td>
              <td> </td>
              <td>10CM</td>
          </tr>
  
          <tr>
              <td>13:00</td>
              <td rowspan="2">선우정아</td>
              <td rowspan="2">참깨와 솜사탕</td>
          </tr>
          <tr>
                  <td>15:00</td>
                  <td> </td>
          </tr>
          <tr>
              <td>17:00</td>
              <td>크러쉬</td>
              <td> </td>
              <td>폴킴</td>
          </tr>
      </table>
  </body>
  </html>
  ```

- 실행 화면

  ![1571709997023](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571709997023.png)



- summary / caption / thead / tbody / tfoot

  - tfoot

    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <style>
            body {
                font-weight: bold;
            }
    
            td {
                border: 1px solid gray;
            }
        </style>
    </head>
    
    <body>
        <!-- summary : 스크린 리더로 접근하는 분들에게 테이블을 어떻게 접근해야 하는지 안내
                        But, HTML5에서는 summary 속성 대신 caption 요소의 내용을 더 이해하기 쉽도록 작성하길 권장한다.
        -->
        <table summary="락 페스티벌 시간표이며 내부 소극장 외부 잔디마당과 대공연장 총 3곳에서 10 시부터 17시까지  ">
            <!-- caption : 표의 제목! 무조건 table의 첫번째 자식으로 와야 한다. -->
            <caption>
                <h1>2019 타임 테이블</h1>
            </caption>
    
            <!-- thead : 테이블의 제목을 그룹화! 한번만 선언 가능하다. -->
            <thead>
                <tr>
                    <th>TIME</th>
                    <th>INDOOR</th>
                    <th colspan="2">OUTDOOR</th>
                </tr>
            </thead>
            <!-- tbody : 테이블의 본문을 그룹화! 여러번 선언 가능하다. -->
            <tbody>
                <tr>
                    <td> </td>
                    <td>소극장</td>
                    <td>잔디마당</td>
                    <td>대공연장</td>
                </tr>
                <tr>
                    <td>10:00</td>
                    <td rowspan="2">안녕하신가영</td>
                    <td> </td>
                    <td>10CM</td>
                </tr>
    
                <tr>
                    <td>13:00</td>
                    <td rowspan="2">선우정아</td>
                    <td rowspan="2">참깨와 솜사탕</td>
                </tr>
                <tr>
                    <td>15:00</td>
                    <td> </td>
                </tr>
                <tr>
                    <td>17:00</td>
                    <td>크러쉬</td>
                    <td> </td>
                    <td>폴킴</td>
                </tr>
            </tbody>
    
            <!-- tfoot : 테이블 하단 요약 부분을 그룹화! 한번만 선언 가능하다. -->
            <tfoot>
    
            </tfoot>
        </table>
    </body>
    
    </html>
    ```

- 실행 화면은 동일함





### 05_orderForm.html

- 샌드위치 주문서 Form 만들기

- input number 의 min / max / step 속성을 부여하여 사이즈의 범위를 지정한다.

  ```html
  <input type="number" step="15" min="15" max="30">
  ```

- select 의 disable의 속성을 부여하여 사용되지 않도록 한다.

  - select  속성
    - autofocus : 페이지가 로드되었을 때 해당 목록으로 바로 포커스가 맞춰집니다.
    - disabled : 화면에는 보이지만 사용할 수 없도록 만듭니다.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=<for>, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  
  <body>
      <h1>FORM</h1>
      <form action="">
          이름 : <input type="text" placeholder="이름을 입력해주세요"> <br>
          날짜 : <input type="date" > <br>
  
          <!-- radio -->
          <h3>1. 샌드위치 선택</h3>
          <input type="radio" name="sandwich" value="egg" >에그 마요 <br>
          <input type="radio" name="sandwich" value="blt">이탈리안 비엠티 <br>
          <input type="radio" name="sandwich" value="tba">터키 베이컨 아보카도
          <br>
          <hr>
  
          <h3>2. 사이즈 선택</h3>
          <input type="number" step="15" min="15" max="30"> <br>
          <hr>
          
          <!-- select -->
          <h3>3. 빵</h3>
          <select name="bread" id="select-bread">
                  <option value="1">허니오트</option>
                  <option value="2" disabled >플랫 브레드</option>
                  <option value="3">하티 이탈리안</option>
          </select>
          <br>
          <hr>
  
          <!-- checkbox -->
          <h3>4. 야채 / 소스</h3>
          <input type="checkbox" name="option" value="1">토마토 <br>
          <input type="checkbox" name="option" value="2">오이 <br>
          <input type="checkbox" name="option" value="3">할라피뇨 <br>
          <input type="checkbox" name="option" value="4" >핫 칠리<br>
          <input type="checkbox" name="option" value="5">바베큐<br>
  
          <br>
          <!-- submit (제출) -->
          <input type="submit" value="주문하기">
  
      </form>
  </body>
  
  </html>
  ```

  

- 실행 화면

  ![1571712257480](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571712257480.png)





#### Web Developer 설치

![1571645260749](https://user-images.githubusercontent.com/39547788/67188257-e508bb00-f426-11e9-8750-d6b897c8cc35.png)

![1571645301435](https://user-images.githubusercontent.com/39547788/67188259-e508bb00-f426-11e9-9267-12edd6b3f2a9.png)