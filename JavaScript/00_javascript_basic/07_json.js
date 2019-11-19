// JavaScript Object -> String

// stringify의 인자로 주어진 string을 JSON 형태로 변환

console.log("Object -> String")
// JSON Object -> String
const jsonData = JSON.stringify({
  도현 : '합기도',
  혁진 : '감자',
})

console.log(jsonData)
console.log(typeof jsonData)


console.log(" ---------------------------- ")
console.log("String -> Object")
// String -> Object
const parseData = JSON.parse(jsonData)

console.log(parseData)
console.log(typeof parseData)

/** 
[ Object VS JSON  ]

JSON
- 데이터를 표현하기 위한 단순 문자열 (String)

Object
- JavaScript의 Key-Value Pair의 자료구조

**/