## CSS

CSS 적용 방법

#### Inline (인라인)

- HTML 요소의 style에 CSS 넣기

<br>

#### Embedding (내부 참조)

- HTML 내부에 CSS 넣기
- HTML head 안에 style 태그를 정의한다.

<br>

#### link File (외부 참조)

- 외부에 있는 CSS 파일을 로드하기
- 컴포넌트 화 

<br>

<br>

### 박스 모델의 구성

#### 기본

- Content

- Padding

  - 상하좌우

- Margin

  - 상하좌우

    ```
    .margin{
        margin-top: 30px;
        margin-right: 20px;
        margin-bottom: 30px;
        margin-left: 20px;
    }
    ```

    

- Border

  - 상하좌우

    ```
    .border{
        border-width: 8px;
        border-style: dotted;
        border-color: slateblue;
        border-top-color: beige;
        border-radius: 25px;
    }
    ```

    

- shorthand

  - 다양한 shortcut 활용도 가능하다.

    - 상하좌우

      ```css
      .margin-shorthand-1{
          /* 상하좌우 적용 */
          margin: 15px;
      }
      ```

      

    - 상하, 좌우

      ```css
      .margin-shorthand-2{
          /* 상하, 좌우 적용 */
          margin: 25px 15px;
      }
      ```

      

    - 상, 좌우, 하

      ```css
      .margin-shorthand-3{
          /* 상, 좌우, 하 적용 */
          margin: 15px 20px 5px;
      }
      ```

      

    - 시계방향 ( 상, 우, 하, 좌)  적용

      ```css
      .margin-shorthand-4{
          /* 시계방향 ( 상, 우, 하, 좌)  적용 */
          margin: 5px 10px 15px 20px;
      }
      ```

      

<br>

<br>

#### display 속성

##### block

- 항상 새로운 라인에서 시작

- 화면 크기 전체의 가로폭을 차지한다. (기본적으로 너비의 100%)

  - margin-right : auto

    - 나머지 빈 곳을 margin  -> 왼쪽 정렬

  - margin-left: auto

    - 나머지 빈 곳을 margin  -> 오른쪽 정렬

  - margin-right : auto

    margin-left: auto

    - 가운데 정렬

<br>

##### inline

- 새로운 라인에서 시작하지 않으며 문장의 중간에 들어간다.
- content의 너비 만큼 가로폭을 치지한다.

<br>

##### inline-block

- block과 inline 레벨 요소의 특징을 모두 갖는다.

<br>

##### none

- 해당 요소를 화면에 표시하지 않는다. (공간조차 사라짐)

  ```css
  .none{
      display: none;
  }
  ```

  

<br>

##### display  : none VS visibility : hidden

- none : 보이지도 않고 공간도 차지하지 않는다.

- hidden : 보이진 않지만 공간은 차지한다.

  ```css
  .hidden{
      visibility: hidden;
  }
  ```

<br>

<br>

### 폰트

- 공백이 있는 폰트 이름은 따음표( '  ' ) 로 묶어준다.

- 폰트로 shorthand 가능하다.

  ```css
  font : font-style   font-weight   line-height   font-size(필수)   font-family(필수) 
  ```

<br>

###### 07_font_text.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="07_font_text.css">
</head>

<body>
    <p>HTML 페이지의 기본 폰트 크기는 16px입니다.</p>
    <p class="font-1">이건 폰트 1</p>
    <p class="font-2">이건 폰트 2</p>
    <p class="font-3">이건 폰트 3</p>
    <p class="font-4">이건 폰트 4</p>
    <p class="font-5">이건 폰트 5</p>

</body>

</html>
```



###### 07_font_text.css

```css
.font-1{
    font-size: 30px;
    /* 공백이 있는 폰트 이름은 따음표로 묶어준다. */
    font-family: 'Times New Roman', Times, serif;
    font-style: italic;
}

.font-2{
    /* 최상위 폰트 크기 * 2 = 32px */
    font-size: 2rem;
    /* Value - Keyword */
    font-weight: bolder;
}

.font-3{
    font-size: 130%;
    /* 공백이 있는 폰트 이름은 따음표로 묶어준다. */
    font-family: 'Courier New', Courier, monospace;
    /* Value - Number */
    font-weight: 700;

}

.font-4{
    /* Value - Keyword */
    font-size: small;
}

.font-5{
    /* 폰트로 shorthand 가능 */
    /* 
        font : 
        font-style font-weight line-height
        font-size (필수) font-family (필수) 
    */
    font: italic 2rem Courier;
}
```

<br>

- 실행 화면

  ![1571732173317](https://user-images.githubusercontent.com/39547788/67268819-67a97d00-f4f0-11e9-8d4a-8b67a72c5ada.png)

<br>

<br>

### Position 

#### static

- 기본적인 요소의 배치 순서에 따라 위 -> 아래, 왼쪽 -> 오른쪽으로 순서에 따라 배치된다.

- 부모 요소의 위치를 기준으로 배치된다.

<br>

#### relative

- 기본 위치를 기준으로 좌표 프로퍼티 (top, bottom, left, right) 를 사용하여 위치를 이동한다.
- 음수도 가능하다.

<br>

#### absolute

- 부모 요소 또는 가장 가까이 있는 조상 요소를 기준으로 좌표 프로퍼티 (top, bottom, left, right)만큼 이동한다. 
- 부모가 Static일 경우
  -  브라우저의 body를 기준으로 위치
- 부모가 Static이 아닌 경우
  - 부모를 기준으로 위치

<br>

#### fixed

- 부모 요소와 관계없이 브라우저의 viewport를 기준으로  좌표 프로퍼티 (top, bottom, left, right)를 사용하여 위치를 이동시킨다. 
- 

<br>

##### 08_position.html

- Static

  - 기본 위치 - 최 상단부터 쌓임

- Absolute

  - 모든 부모가 Static 인 경우
    - absolute는 body를 기준으로 위치한다.
  - 부모 중에 Static이 아닌 것이 있는 경우

  

  ###### 08_position.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <link rel="stylesheet" href="08_position.css">
  </head>
  
  <body>
      <h2>1. Static (기본 위치 - 최 상단부터 쌓임)</h2>
      <div>static</div>
      <div>static</div>
  
      <h2>2-1. Absolute : 모든 부모가 Static 인 경우</h2>
      <!-- 부모가 Static일 경우, absolute는 body를 기준으로 위치한다. -->
      <!-- parent는 Static -->
  
      <div class="parent">
          <div class="absolute">absolute1</div>
      </div>
  
      <h2>2-2. Absolute : 부모 중에 Static이 아닌 것이 있는 경우</h2>
      <div class="parent relative">
          <div class="absolute">absolute2</div>
      </div>
  
  
  </body>
  
  </html>
  ```

  ###### 08_position.html

  ```
  body{
      height: 10000px;
  }
  
  div{
      width: 100px;
      height: 100px;
      background-color: skyblue;
      margin-top: 5px;
      text-align: center;
  }
  
  .parent{
      background-color: burlywood;
  }
  
  .absolute{
      position: absolute;
      top: 50px;
      left: 30px;
      background-color: blueviolet;
  }
  
  .relative{
      position: relative;
  }
  ```

  <br>

- 실행 화면

  ![1571731820398](https://user-images.githubusercontent.com/39547788/67268817-67a97d00-f4f0-11e9-8c8b-ebc7ae1ec03a.png)

<br>

##### 09_box.html

- 5개의 상자를 주어진 위치에 위치시킨다. 

  ```css
  .big-box {
      position: relative;
      margin: 100px auto 500px;
      border: 5px solid black;
      width: 500px;
      height: 500px;
    }
    
    .small-box {
      width: 100px;
      height: 100px;
      position: absolute;
    }
    
    #red {
      background-color: red;
      position: absolute;
      top: 400px;
      left: 400px;
      /* 큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기 */
    }
    
    #gold {
      background-color: gold;
      position: fixed;
      bottom: 50px;
      right: 50px;
      
      /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */
    }
    
    #green {
      background-color: green;
      position: absolute;
      top: 200px;
      left: 200px;
  
      /* absolute 이용해서 큰 사각형의 가운데 위치시키기 */
    }
    
    #blue {
      background-color: blue;
      position: relative;
      left: 100px;
      top: 100px;
  
      /* relative를 사용해서 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기 */
    }
    
    #pink {
      background-color: pink;
      position: absolute;
      top: 0px;
      left: 0px;
      /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
    }
  ```

  <br>

- 실행 화면

  ![1571730369986](https://user-images.githubusercontent.com/39547788/67268815-67a97d00-f4f0-11e9-9e6a-dde5f834a72a.png)

<br><br>

##### 09_box_more.html

- 7개의 상자를 주어진 위치에 위치시킨다. 

  ```css
  .big-box {
      position: relative;
      margin: 100px auto 500px;
      border: 5px solid black;
      width: 500px;
      height: 500px;
    }
    
    .small-box {
      width: 100px;
      height: 100px;
    }
    
    #red {
      background-color: red;
      position: absolute;
      bottom: 0px;
      right: 0px;
      /* 큰 사각형 내부의 우측 하단 모서리에 빨간 사각형 위치시키기 */
    }
    
    #gold {
      background-color: gold;
      /* 브라우저의 하단에서 50px, 우측에서 50px 위치에 고정하기 */
      position: fixed;
      bottom: 50px;
      right: 50px;
    }
    
    #green {
      background-color: green;
      position: absolute;
      top: 200px;
      left: 200px;
  
      /* absolute 이용해서 큰 사각형의 가운데 위치시키기 */
    }
    
    #blue {
      background-color: blue;
      position: absolute;
      top: 100px;
      left: 100px;
  
      /* relative를 사용해서 큰 사각형 좌측 상단 모서리에서 100px, 100px 띄우기 */
    }
    
    #pink {
      background-color: pink;
      position: absolute;
      top: 0px;
      left: 0px;
  
      /* 큰 사각형 내부의 좌측 상단 모서리로 옮기기*/
    }
    #purple {
      background-color: purple;
      /* 초록 사각형의 우측 하단 모서리에 보라 사각형 좌측 상단 모서리 맞대기 */
      position: absolute;
      top: 100px;
      left: 100px;
    }
    
    #orange {
      background-color: orange;
      /* 파란 사각형 오른쪽 위 모서리에 오렌지 사각형 좌측 하단 모서리 맞대기 */
      position: absolute;
      top: -100px;
      left: 100px;
    }
    
  ```

  <br>

- 실행 화면

  ![1571730439561](https://user-images.githubusercontent.com/39547788/67268816-67a97d00-f4f0-11e9-8a85-09df228e631e.png)



<br>

<br>

### 크기 단위

1. 픽셀 (pixel)
   - 일반적으로 브라우저에서는 1/96인치를 **절대 단위**로 인식한다.
2. 퍼센트 (%)
3. em / rem
   - 

4. Viewport 단위

   - vm

     ```css
     .div-vw{
         width: 20vw;
         height: 20vw;
         background-color: indianred;
     }
     ```

     

   - vh

     ```css
     .div-vh{
         width: 20vh;
         height: 20vh;
         background-color: rgba(49, 255, 176, 0.952);    
     }
     ```

     

   - vmin

     ```css
     .div-vmin{
         width: 10vmin;
         height: 12vmin;
         background-color: yellowgreen;
     }
     ```

     

   - vmax

     ```css
     .div-vmax{
         width: 10vmax;
         height: 12vmax;
         background-color: thistle;
     }
     ```

     

<br>

<br>

### 선택자

1. 전체 선택자

   ```css
   *{
       color: yellowgreen;
   }
   ```

   <br>

2. 태그 선택자

   ```css
   h1{
       color: brown;
   }
   ```

   <br>

3. 클래스 선택자

   ```css
   .aqua{
       color: aqua;
   }
   ```

   <br>

4. 아이디 선택자

   ```css
   #violet{
       color: violet;
   }
   ```

   <br>

- **선택자 우선 수위**
  1. !important
     - 정말 필요할 때만 쓰기
     - 남용하면 코드가 파국으로 치닫는다.
  2. inline style 속성
     - 필요할 때만 쓰기
     - 님용하면 유지보수가 매우 힘들다. (CSS 파일로만 유지보수 할 수는 없다 .)
  3. 아이디 선택자
  4. 클래스 선택자
  5. 태그 선택자
  6. 전체 선택자



<br>

<br>



