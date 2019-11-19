const numbers = [1,2,3,4,5]

// 첫번째 인덱스
numbers[0] 

// undefined -> 정확한 양의 정수만 가능
numbers[-1] 

// Array의 길이 
numbers.length

// 원본 파괴 
numbers.reverse()
numbers 
// [5,4,3,2,1]

numbers.reverse()
numbers
// [1,2,3,4,5]

// push - Array에 새로운 요소 추가 후 Array의 길이 return 
// 기본적으로 push 이후에는 Array의 length를 return 한다.
numbers.push('a')
// 6
numbers
// [1,2,3,4,5,'a']

// pop : 배열의 가장 마지막 요소 제거 후 return  
// Array의 가장 마지막 요소를 return 후 출력
numbers.pop()
// 'a'
numbers
// [1,2,3,4,5]


// unshift : 배열 가장 앞에 요소 추가
// 맨 앞에 추가
// 추가된 이후에 length를 return 한다.
numbers.unshift('a')
// 6 
numbers
// ['a', 1,2,3,4,5]


// shift : 배열의 가장 앞의 요소 제거 
numbers.shift('a')
// 'a'
numbers
// [1,2,3,4,5]

numbers.push('a', 'b')
numbers
// [1,2,3,4,5, 'a', 'b']

numbers.unshift('a')
numbers
// ['a', 1,2,3,4,5, 'a', 'b']

// 가장 먼저 있는 'a'의 인덱스를 return 
numbers.indexOf('a')
// 0

// 가장 먼저 있는 'b'의 인덱스를 return 
numbers.indexOf('b')
// 8

// 만약, 찾고자 하는 요소가 Array에 없는 경우 -1을 return 
numbers.indexOf('c')
// -1


//join : Array의 요소를 join 함수 인자를 기준으로 묶어서 문자열로 return 
// ','를 기준으로 문자열을 return 한다. 
numbers.join()
// 'a,1,2,3,4,5,a,b' (기본값은 ',')

// 각 요소를 '-'로 붙여 문자열을 return 한다. 
numbers.join('-')
// 'a-1-2-3-4-5-a-b'

// 모든 요소가 다 붙어서 문자열을 return 한다. 
numbers.join('')
// 'a12345ab'