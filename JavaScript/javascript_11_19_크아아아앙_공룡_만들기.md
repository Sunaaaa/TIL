# 크아아아앙 공룡 만들기

## Callback Function

### 1.1 정의

> "좀 이따 너 실행 끝나면, 나 다시 불러줘! (Call Back)"

- **다른 함수에 인수로 넘겨지는 함수**
- 특정 이벤트가 발생했을 때, 시스템에 의해 호출되는 함수
- 자주 사용되는 대표적인 예 -> 이벤트 핸들러 처리 



- `<script>`태그 추가 

  ```html
  <html>
    <head></head>
    <body>
      <button id="my-button"> 클릭해주세요 </button>
  
      <script>
        const button = document.getElementById('my-button')
      </script>
  
    </body>
  </html>
  ```

  ![1574128326646](tpassets/1574128326646.png)

- 이벤트 핸들러 사용하기

  - '클릭해주세요' 버튼을 누르면 console 창에 '버튼이 클릭됨' 이 출력된다. 

    ```html
    <html>
      <head></head>
      <body>
        <button id="my-button"> 클릭해주세요 </button>
    
        <script>
          const button = document.getElementById('my-button')
          button.addEventListener('click', function(){
            console.log('버튼이 클릭됨')
          })
        </script>
    
      </body>
    </html>
    ```

    <br>



### 1.2 예시

#### 1.2.1 함수 정의



#### 1.2.2 



#### 1.2.3 