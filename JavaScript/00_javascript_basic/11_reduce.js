const Tests = [90,85,77,13,58]

/** 
const sum = Tests.reduce(function(total, score){
  return total += score
})
*/

const sum = Tests.reduce((total, score) => total += score)

console.log(sum)