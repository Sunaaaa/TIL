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











## 3. Loop

### 3.1 while 문





### 3.2 for 문







## 4. 함수 (function)

> 함수 선언식 (statement) : 코드가 실행되기 전에 로드된다.
>
> 함수 표현식 : 



### 4.1 선언식 

- 인터프리터가 함수에 닿지 않았는데 위로 끌어올려 (호이스팅) 실행시킨다. 



### 4.2 표현식 

- 함수 정의되기 전에 함수가 호출이 되면 ERROR







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