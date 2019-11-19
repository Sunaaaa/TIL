// for loop
// var students = [
//   { name : '서혁진' , age : 25 },
//   { name : '오은애' , age : 24 },
//   { name : '공선아' , age : 24 },
//   { name : '이도현' , age : 25 },
//   { name : '최주현' , age : 27 },
// ]

// var student = []
// for (var i = 0; i<students.length; i++){
//   if (students[i].age === 27){
//     student = students[i]
//     break // 원하는 조건에 도달하면 escape loop
//   }
// }


// console.log(student)


// find Helper
const STUDENTS = [
  { name : '서혁진' , age : 25 },
  { name : '오은애' , age : 24 },
  { name : '공선아' , age : 24 },
  { name : '이도현' , age : 25 },
  { name : '이수연' , age : 21 },
]

// const STUDENT = STUDENTS.find(function(student){
//   return student.age === 27
// })
const STUDENT = STUDENTS.find(student => student.age === 27)

console.log(STUDENT)
