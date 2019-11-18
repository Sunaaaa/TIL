function (num) {return num ** 3}

const cube = function (num) {return num ** 3}
console.log(cube(2))
const squareRoot = num => num ** 0.5
console.log(squareRoot(2))

console.log(
    function (num) {return num ** 3}(2)
)

console.log(
    (num => num ** 0.5)(4)
)