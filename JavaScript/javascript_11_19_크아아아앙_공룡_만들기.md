# 크아아아앙 공룡 만들기

## 1. Callback Function

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

```javascript
function doSomething(task){
	alert(`자, 이제 ${task} 준비를 시작해볼까?`)
}

undefined
doSomething('해커톤')
```



<br>

#### 1.2.2 익명 함수인 콜백 함수 추가

- 먼저 doSomething()이 수행 된후, 익명 함수로 정의한 콜백 함수가 수행된다. 

  ```javascript
  function doSomething(task, callback){
  	alert(`자, 이제 ${task} 준비를 시작해볼까?`)
  	callback()
  }
  
  undefined
  doSomething('해커톤', function(){
  	alert('당장 이번주 금요일부터 시작이야...')
  })
  undefined
  ```



#### 1.2.3 기명 함수인 콜백 함수로 변경해서 추가

- 우리가 원하는 시점에 함수를 호출해서 사용할 수 있게 되었다. 

  ```
  
  ```

  





<br><br>

## 2. EventListener

### 2.1 정의

- 특정한 이벤트가 발생했을 때 실행되는 함수 또는 절차

  1. 무엇을 -> EventTarget
  2. 언제 -> Type의 행위를 했을 떄
  3. 어떻게 -> (주로) Listener에 구현된 함수를 실행

- `addEventListener` 메소드 구성 요소

  > ```javascript
  > EventTarget.addEventListener(type, listener)
  > ```
  >
  > - **EventTarget** : 이벤트 리스너를 등록할 대상 ( -> DOM 노드)
  > - **type** : 이벤트 유형을 뜻하는 문자열 (`click`, `mouseover` 등)
  > - **listener** : 이벤트가 발생했을 때 처리를 담당하는 콜백 함수 
  >   - 인수로 이벤트 객체인 `e`를 전달 받는다. 

<br>

### 2.2 예시

1. (무엇을) 특정한 DOM요소를 
   - button을
2. (언제) 어떠한 행동을 했을 때 
   - click 했을 때
3. (어떻게) 한다. 
   - '뿅' 한다.



```php+HTML
<html>
  <head></head>
  <body>
    <div id="my">
    </div>

    <button id="this-button"> Click me!</button>

    <script>
      // 1. 무엇을 -> 버튼을 (EventTarget)
      const button = document.querySelector('#this-button')
      // 2. 언제 -> 'click' 하면 (type : 'click')
      button.addEventListener('click', function(event){
        console.log(event)
        const area = document.querySelector('#my')
        // 3. 어떻게 -> '뿅'하고 나온다.
        area.innerHTML = '<h1>뿅</h1>'

      })

    </script>

  </body>
</html>
```

![1574130335045](../../../AppData/Roaming/Typora/typora-user-images/1574130335045.png)

<br>

<br>

## 3. Google dino

### 3.1 BOM & DOM

### 3.2 사전 준비