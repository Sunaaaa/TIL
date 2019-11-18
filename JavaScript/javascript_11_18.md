# JavaScript Syntax basics





## 0. 사전 준비 

> HTML로 뼈대를 잡고 CSS로 꾸미고, JavaScript로 활력을 불어 넣는다. 
>
> JavaScript로 서버까지 구축할 수 있도록 Node.js 등장!!
>
> - Node.js 발표와 동시에 JavaScript가 브라우저 종속적인 언어가 아닌 서버 구축까지 가능해지면서 Hot 한 언어로 급부상한다.
>
> - `Express.js` (서버), `React.js `(프론트), `Vue.js` (프론트) 등 JavaScript 기반의 수 많은 프레임워크, 라이브러리 들이 현대 웹 개발 트랜드를 주도라고 있다.

<br>

### 0.1 Node.js 설치

- node.js 공식 홈페이지에서 [다운로드](https://nodejs.org/ko/)
  - LTS Vercion (안정적)
  
  - Windows Installer (.ms) 64bit
  
    ![1574043022907](tpassets/1574043022907.png)



<br>

- 설치 확인

  ```bash
  $ node -v
  v12.13.0
  ```



<br>

### 0.2 VS Code Python & JavaScript Indenting 설정

- settings.py

  ![1574049827422](tpassets/1574049827422.png)

  <br>

  ```python 
  {
      .
      .
      
      "editor.tabSize": 2,
      "[python]" : {
          "editor.tabSize": 4,
      }, 
  
      .
      .
  
  }
  ```

  <br>

  

- VSCode 환경 설정

  ![1574049784199](tpassets/1574049784199.png)

  <br>

  ![1574049716781](tpassets/1574049716781.png)

  <br>



### 0.3 Naming Convention

#### lower Camel Case

- 단봉 낙타 표기법
- JavaScript의 기본 표기법



#### Upper Camel Case

- 쌍봉 낙타 표기번



#### snake_case



#### kebob-case



### 0.4 Extentions (추천)

- `auto close tag`
- `rainbow brackets`
- `indent-rainbow`

<br>



실행 방법

```bash
$ node [파일명]
```

![1574044421490](tpassets/1574044421490.png)

## 1. Variable

### 1.1 let (변수)

- 값을 재할당 할 수 있는 변수를 선언하는 키워드

- 변수 선언은 한 번만 할 수 있다.

  ```javascript
  // let (변수)
  let x = 1
  let x = 4
  x = 3 // 재할당
  console.log(x)
  ```

  ![1574049627355](tpassets/1574049627355.png)

  <br>

  - 그러나, 할당은 여러 번 할 수 있다. 

    ```javascript
    // let (변수)
    let x = 1
    x = 3 // 재할당 가능
    console.log(x)
    ```

    ![1574044421490](tpassets/1574044421490.png)

    <br>

- 블록 유효 범위 (`Block Scope`) 를 갖는 지역 변수 

  ```javascript
  let x = 1
  if (x===1){
    // if문 만큼의 유효범위를 가지고 있다. 
    // 벗어나면 접근 불가능!
    let x = 2
    console.log(x)  // 2
  }
  console.log(x)    // 1
  ```

  ![1574044751393](tpassets/1574044751393.png)

<br>



### 1.2 const (상수) 

- 값이 변하지 않는 상수를 선언하는 키워드 
  - 상수의 값은 재할당을 통해 바뀔 수 없고, 재선언도 **불가능**하다.
- `let`과 동일하게 `Block Scope`를 갖는다.
- 가능한 모든 선언에서 상수를 써야 한다.
  - 일단 상수를 사용하고, 값이 바뀌는게 자연스러운 상황이면 그때 변수(`let`)로 바꿔서 사용하는 것을 권장한다.



- 초기값을 생략하면 **ERROR** 발생

  ```javascript
  // 상수 
  // 초기값을 생략하면 ERROR
  const MY_FAV
  ```

  ![1574049656414](tpassets/1574049656414.png)

  <br>

- 상수 값 할당

  ```javascript
  // MY_FAV를 상수로 정의하고 그 값을 7로 함
  const MY_FAV = 7
  console.log("My Favourite number is ... " + MY_FAV)
  ```

  <br>

- 상수 값 재할당

  ```javascript
  
  ```

- 상수 재 선언

  ```
  
  ```

  



- 변수 와 상수는 어디에 써야 할까?
  - 어디에 변수를 쓰고, 어디에 상수를 쓰는지에 대한 결정은 프로그래머의 몫
  - `파이 근삿값`과 같은 상수가 적절 (변할 일이 없는 값)
- `var` VS `let` VS `const`
  - `var` : 할당 및 선언 자유, 함수 스코프
  - `let` : 할당 자유, 선언은 한번만, 블록 스코프
  - `const` : 할당과 선언 한번만, 블록 스코프 
- `var`는 호이스팅과 같은 문제를 야기하기 때문에, 앞으로는 `let`과 `const`를 사용해서 개발을 진행하자!!!







## 2. 조건문

### 2.1 if문

```javascript
const userName = prompt("What is your name?")

message = ''

if (userName === '도현'){
  message = '<h1>유단자... 까불지마요..</h1>'
    
} else if (userName === '혁진'){ 	
  message = '<h1>감자 ...혁진 감자합니다.</h1>'
} else {
  message = `<h1>${userName} .. 누구? ? </h1>`
}

document.write(message)		
```

- 프롬프트를 이용해서 받은 `userName`을 받아 if문을 실행하고, `userName`을 확인해보자!

  ![1574053038541](tpassets/1574053038541.png)

  <br>

  ![1574053046831](tpassets/1574053046831.png)

  <br>

  ![1574053056624](tpassets/1574053056624.png)

<br>



## 3. Loop

### 3.1 while 문

```
let i = 0 
while (i<6){
  console.log(i)
  i++
}
```

![1574053105865](tpassets/1574053105865.png)

<br>

### 3.2 for 문

1. JavaScript 의 가장 기본적인 반복문

   - for 문에서 사용할 변수 하나를 정의하고, 그 변수가 특정 조건에 false 값이 될 때까지 계속 연산-반복

     ```
     for (let j = 0; j < 6; j++){
       console.log(j)
     }
     ```

     ![1574053228162](tpassets/1574053228162.png)

     <br>

2. Python 의 for in 문법과 비슷하게 사용가능!

   ```
   const numbers = [1,2,3,4,5]
   for (let number of numbers){
     console.log(number)
   }
   ```

   ![1574053248755](tpassets/1574053248755.png)

   <br>

3. number 값 재 할당이 필요없으면 상수 사용 가능!

   - 직접 list를 지정하는 것도 가능하다.

     ```
     for (let number of [1,2,3,4,5]){
       console.log(number)
     }
     ```

     ![1574053276755](tpassets/1574053276755.png)

     <br>





## 4. 함수 (function)

> 함수 선언식 (statement) : 코드가 실행되기 전에 로드된다.
>
> 함수 표현식 : 



### 4.1 선언식 

- 인터프리터가 함수에 닿지 않았는데 위로 끌어올려 (호이스팅) 실행시킨다. 

  - 함수 정의보다 함수 호출이 먼저된 경우

    ```
    console.log(add(2,1))
    function add(num1, num2){
      return num1 + num2
    }
    ```

    

  - 함수 호출보다 함수 정의가 먼저된 경우

    ```
    function add(num1, num2){
      return num1 + num2
    }
    console.log(add(2,1))
    ```

    



### 4.2 표현식 

- 함수 정의되기 전에 함수가 호출이 되면 ERROR

  - 함수 정의보다 함수 호출이 먼저된 경우

    ```
    console.log(sub(2,1))
    const sub = function(num1, num2){
      return num1-num2
    }
    ```

    

  - 함수 호출보다 함수 정의가 먼저된 경우

    ```
    const sub = function(num1, num2){
      return num1-num2
    }
    console.log(sub(2,1))
    ```

    



### 4.3 type

- type을 확인하면 둘다 function으로 동일!

  작동 방법만 다르다.

  ```
  console.log(typeof(add))
  console.log(typeof(sub))
  ```

  



<br>

## 5. 화살표 함수 (Arrow Function)

> ES6 이후에 나왔으며, 기존의 funciton과 중괄호 숫자를 줄이기 위해 고안된 문법
>
> 1. `function` 키워드 생략 가능
> 2. 함수에 매개변수 하나 -> () 생략 가능
> 3. 함수 바디에 표현식 하나 -> {}, return  생략 가능
>
> 
>
> - 화살표 함수의 경우 `function` 키워드로 정의한 함수와 100% 동일하지 않다. 
> - 화살표 함수는 항상 **익명함수 (Anonymouse Function) !!!**





1. `function` 키워드 생략 가능
2. 함수에 매개변수 하나 
3. 함수 바디에 표현식 하나 
4. 인자가 없는 경우 
5. 객체를 return 하는 경우
   - `return `키워드 有
   - `return `키워드 無
6. 기본 인자 부여





## 익명 / 1회용 함수 (Anonymouse Function)

> JavaScript에서는 1회용으로 사용하는 함수의 이름을 짓지 않아도 된다. 
>
> 일반적으로 함수를 정의하고 변수에 함수를 저장하는 과정 등을 거쳐 실행한다. 
>
> 하지만, `즉시실행함수`는 함수가 선언되자마자 즉시 실행된다. 
>
> <hr>
>
> **Why ?**  **초기화**에 사용한다.
>
> - `즉시 실행함수`는 선언되자마자 실행되기 때문에, 같은 함수를 다시 호출할 수 없다. 그래서 초기화 부분에 주로 사용한다.



- `function`키워드를 활용해서 함수를 선언할 때는, 이름을 지정하지 않으면 ERROR가 난다. 

  ```javascript
  function (num) {return num ** 3}
  ```



해결!

1. 기명 함수로 만들기 (변수, 상수에 할당)

   ```javascript
   const cube = function (num) {return num ** 3}
   ```

   - 화살표 함수 또한 기본적으로 익명함수이지만, 변수 및 상수에 할당해서 기명함수처럼 사용 가능

     ```javascript
     const squareRoot = num => num ** 0.5
     ```

2. 익명함수 바로 실행시키기

   ```javascript
   console.log(function (num) {return num ** 3}(2))
   console.log((num => num ** 0.5)(4))
   ```

   





## 6. 배열 (Array)







## 7. Object

> JavaScript 또한 객체지향!

```
const me = {
  // key 가 한 단어일 때
  name : '선호', 

  // key가 여러 단어일 때, ' '로 감싸준다.
  'phone number' : '01012345678',

  appleProducts : {
    iphone : 'xs', 
    watch : 'series5', 
    macbook : 'pro2019'
  }
}
```







### 7.2 ES5 방식

```javascript
// ES5

var books = ['자바스크립트 입문', '장고 웹 프로그래밍']
var comics = {
  'DC' : ['Aquaman', 'Jocker'],
  'Marvel' : ['Avengers', 'Spider Man']
}

var magazines = null
var bookShop = {
  books : books,
  comics : comics,
  magazines : magazines
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books)
console.log(bookShop.books[0])
```





### 7.3 ES6 이후 

- 객체의 Key와 Value가 똑같으면, 마치 배열처럼 한번만 작성 가능

  ```javascript
  var books = ['자바스크립트 입문', '장고 웹 프로그래밍']
  var comics = {
    'DC' : ['Aquaman', 'Jocker'],
    'Marvel' : ['Avengers', 'Spider Man']
  }
  
  var magazines = null
  var bookShop = {
    books,
    comics,
    magazines
  }
  
  console.log(bookShop)
  console.log(typeof bookShop)
  console.log(bookShop.books)
  console.log(bookShop.books[0])
  
  
  ```

  





### JSON

> **JSON** (JavaScript Object Notation) : JavaScript 객체 표기법
>
> 웹에서 데이터를 주고받을 때 대표적으로 JSON, XML, YAML 형식 등이 있다. **주로 JSON을 사용한다.**
>
> - Key-Value 형태의 자료구조를 JavaScript Object와 유사한 모습으로 표현하는 표기법
> - 하지만 JSON을 모습만 비슷할 뿐, 실제 Object처럼 사용하기 위해서는 다른 언어들과 마찬가지로 **parsing (구문 분석) 하는 작업이 필요**하다.

<br>

JSON : String

JavaScript Object : Object



#### [ Object VS JSON  ] 

JSON

- 데이터를 표현하기 위한 단순 문자열 (String)

Object

- JavaScript의 Key-Value Pair의 자료구조









## 8. Array Helper Method

> **Helper** 란 **자주 사용하는 로직을 재활용**할 수 있게 만든 일종의 Library
>
> ES6부터 본격적으로 사용되기 시작했다. 
>
> [MDN](https://developer.mozilla.org/ko/)를 참고하여 더우우우우우우우우우우욱더 상세한 사용법을 알아보자!

<br>

### 8.1 forEach

- `arr.forEach(callback(element, index, array))`

  - 주어진 callback 함수를 배열에 있는 각 요소에 대해 한번씩 실행

    ```javascript
    const IOT1 = ['수연', '승찬', '한석', '경희', '영선']
    IOT1.forEach(function(student){
      console.log(student)
    })
    ```

    





#### [실습] 

#### 1. for를 forEach로 바꾸기 

##### for

```javascript
function handleStudents(){
  const students = [
    { id : 1, name : '오은애', status : '응애?'},
    { id : 15, name : '서혁진', status : '기염둥이....?'},
    { id : 28, name : '김영선', status : '너무 쉽네 JS...'},
  ]

  for (let i = 0; i < students.length; i++){
    console.log(students[i])
    console.log(students[i].name)
    console.log(students[i].status)
  }
}
handleStudents()
```



<br>

##### forEach

```javascript
function handleStudents(){
  const students = [
    { id : 1, name : '오은애', status : '응애?'},
    { id : 15, name : '서혁진', status : '기염둥이....?'},
    { id : 28, name : '김영선', status : '너무 쉽네 JS...'},
  ]

  students.forEach(students => {
    console.log(students)
    console.log(students.name)
    console.log(students.status)
  })
}
handleStudents()
```

- 실행 결과는 같다 

  ![1574059170995](tpassets/1574059170995.png)

  <br>



#### 2. images 배열 안에 있는 정보를 곱해 넓이를 구하여, areas 배열에 저장

```javascript
const images = [
  { height : 30, width : 55 },
  { height : 50, width : 178 },
  { height : 81, width : 35 },
]
const areas = []

// forEach
images.forEach(images => {
  areas.push(images.height * images.width)
})

console.log(areas)
```

- 실행 결과

  ![1574059480580](tpassets/1574059480580.png)

  <br>















