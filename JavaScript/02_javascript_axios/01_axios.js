const axios = require('axios')

// axios를 통해 GET 요청
axios.get('https://jsonplaceholder.typicode.com/posts/1')
.then(response => {
  console.log(response)
})
.catch(error => {
  console.log(error)
})