const me = {
  // key 가 한 단어일 때
  name : '선호', 

  // key가 여러 단어일 때, ' '로 감싸준다.
  'phone number' : '01012345678',

  appleProducts : {
    iphone : 'xs', 
    watch : 'series5', 
    macbook : 'pro2019'
  }
}

// key가 한단어일 때 
console.log(me.name)
// "선호"

// key가 여러단어일 때는 []를 통해 접근
console.log(me['name'])
// "선호"
console.log(me['phone number'])
// "01012345678"

console.log(me.appleProducts)
// { iphone : 'xs', watch : 'series5',  macbook : 'pro2019' }

console.log(me.appleProducts.iphone)
// "xs"
