// ES5

// var books = ['자바스크립트 입문', '장고 웹 프로그래밍']
// var comics = {
//   'DC' : ['Aquaman', 'Jocker'],
//   'Marvel' : ['Avengers', 'Spider Man']
// }

// var magazines = null
// var bookShop = {
//   books : books,
//   comics : comics,
//   magazines : magazines
// }

// console.log(bookShop)
// console.log(typeof bookShop)
// console.log(bookShop.books)
// console.log(bookShop.books[0])


// ES6 이후 

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

console.log("ES6")
console.log(bookShop)
console.log("")
console.log(typeof bookShop)
console.log("")
console.log(bookShop.books)
console.log("")
console.log(bookShop.books[0])
console.log("")