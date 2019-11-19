// 숫자가 담긴 배열의 각 요소에 각각 2를 곱하여 새로운 배열 만들기

// ES5
// 원본을 건드리지 않았기 때문에 원본이 유지된다.
var numbers = [3,2,1]
var doubleNumbers = []

for (var i = 0; i<numbers.length; i++){
  doubleNumbers.push(numbers[i]*2)
}
// console.log(doubleNumbers)
// console.log(numbers)

// console.log('')
// console.log('')
// console.log('')

// ES6+
// helper method를 사용해서 바꿔보자 
const NUMBERS = [1,2,3]
// return 하는 값이 있기 때문에 변수에 담을 수 있다. 
// 없는 경우 undefined
// const DOUBLE_NUMBERS = NUMBERS.map(function(number){ return number*2 })

// 한줄로 
const DOUBLE_NUMBERS = NUMBERS.map(number => number*2 )

// console.log(DOUBLE_NUMBERS)
// console.log(NUMBERS)



// map helper를 사용해서 images 배열 안의 객체들의 height들만 저장되어 잇는 heights 배열을 만들어보자.
const images = [
  { height : '34px', width : '59px' },
  { height : '22px', width : '135px' },
  { height : '681px', width : '592px' },
]

const heights = images.map(function(image){
  return image.height
})
// const heights = images.map(image => image.height)
// console.log(heights)


// map helper를 사용해서 "distance/time => 속도"를 저장하는 새로운 배열 speeds를 만드시오.
const trips = [
  { distance : 34, time : 10 },
  { distance : 90, time : 20 },
  { distance : 111, time : 28 },
]

/* 
const speeds = trips.map(function(trip){
  return trip.distance / trip.time
})
 */
const speeds = trips.map(trip => trip.distance/trip.time)
console.log(speeds)
console.log('speeds' + speeds)