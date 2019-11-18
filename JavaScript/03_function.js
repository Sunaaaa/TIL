// // 선언식
// console.log(add(2,1))
// function add(num1, num2){
//   return num1 + num2
// }
// console.log(add(2,1))

// // 표현식
// // 변수에 담는 것ㅇ 
// console.log(sub(2,1))
// const sub = function(num1, num2){
//   return num1-num2
// }
// console.log(sub(2,1))

// // type을 확인하면 둘다 function으로 동일!
// // 작동 방법만 다름 
// console.log(typeof(add))
// console.log(typeof(sub))


// // ## 화살표 함수 (Arrow Function)
// const iot1 = function(name){
//   return 'hello! ${name}!!'
// }


// // 1. function 키워드 삭제
// const iot1 = (name) => {return 'hello! ${name} '}

// // 2. ( ) 생략 (함수 매개변수 하나일 경우)
// const iot1 = name => {return 'hello! ${name} '}

// // 3. { }, return 생략 (바디 부분에 표현식 1개)
// const iot1 = name => 'hello! ${name} '


// let square = function(num){
// 	return num ** 2
// }

// // 1. function 키워드 삭제
// square1 = (num) => {return num ** 2}
// console.log(square(2))
// // 2. ( ) 생략 (함수 매개변수 1개 )
// square1 = num => {return num ** 2}
// console.log(square(2))

// // 3. { }, return 생략 (바디 부분에 표현식 1개)
// square1 = num => num ** 2
// console.log(square(2))


// // 4. 인자가 없다면...? ( ) 혹은 _로 표시 가능!
// let noArgs = () => {return 5}
// noArgs()

// let noArgs = _ => {return 5}
// noArgs()

// let noArgs = _ => 5
// noArgs()

// // 5.
// // 5-1. object를 return 
// // 객체를 return할 때는 return 키워드를 명시적으로 적어준다. 
// let returnObject = () => {return {key:'value'}}
// console.log(returnObject())
// console.log(typeof(returnObject()))


// // 5-2. return을 적지 않으려면?
// // () 를 붙인다.
// returnObject = () => ({key : 'value'})
// console.log(returnObject())
// console.log(typeof(returnObject()))


// // 6. 기본 인자 부여하기 (Default Args)
// 인자 개수와 상관없이 반드시 괄호를 붙인다. 
const sayHello = (name='혁진') => `안녕! ${name} `
console.log(sayHello('선아'))
