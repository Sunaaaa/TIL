// for loop 활용
var students = [
  { name : '서혁진', type : 'male' },
  { name : '공선아', type : 'female' },
  { name : '남찬우', type : 'male' },
  { name : '이도현', type : 'female' },
]

var strongStudents = []
for (var i = 0; i<students.length; i++){
  if(students[i].type === 'female'){
    strongStudents.push(students[i])
  }
}

console.log(students)         // 원본 유지 
console.log(strongStudents)   // 새로운 배열
console.log(students[i].name) // 객체 내 속성 접근하기


// filter Helper 활용