// ES5 for loop
var iot1 = ['도현', '혁진', '은애']

console.log("ES5")
for (var i = 0; i < iot1.length; i++){
  console.log(iot1[i])
}

console.log("====")

// ES6+
console.log("ES6 + ")
const IOT1 = ['수연', '승찬', '한석', '경희', '영선']
IOT1.forEach(function(student){
  console.log(student)
})

// 한줄로 리팩토링 가능!
console.log("====")

console.log("한줄")
IOT1.forEach(student => console.log(student))

// forEach는 기본으로 들어오는 retirn 값이 없다. 
console.log("====")

console.log("RETURN 값이 없다 .")
const result = IOT1.forEach(
  student => console.log(student)
)
console.log("RETURN 값")
console.log(result)


// [실습] for를 forEach로 바꾸기 
// for

console.log('for')
console.log('--------')

function handleStudents_for(){
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
handleStudents_for()

console.log('')
console.log('')
console.log('')

console.log('forEach')
console.log('--------')

// forEach
function handleStudents_forEach(){
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
handleStudents_forEach()

console.log('')
console.log('')
console.log('')

// [실습] images 배열 안에 있는 정보를 곱해 넓이를 구하여, areas 배열에 저장하세요.
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