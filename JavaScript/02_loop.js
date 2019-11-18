
// while loop

let i = 0 
while (i<6){
  console.log(i)
  i++
}


// for loop
// JavaScript 의 가장 기본적인 반복문
// for 문에서 사용할 변수 하나를 정의하고, 그 변수가 특정 조건에 false 값이 될 때까지 계속 연산-반복

for (let j = 0; j < 6; j++){
  console.log(j)
}


// Python 의 for in 문법과 비슷하게 사용가능!
const numbers = [1,2,3,4,5]
for (let number of numbers){
  console.log(number)
}

// number 값 재 할당이 필요없으면 상수 사용 가능!
// 직접 list를 지정하는 것도 가능하다.
for (let number of [1,2,3,4,5]){
  console.log(number)
}