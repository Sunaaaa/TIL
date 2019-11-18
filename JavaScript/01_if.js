const userName = prompt("What is your name?")

message = ''

if (userName === '도현'){
  message = '<h1>유단자... 까불지마요..</h1>'
    
} else if (userName === '혁진'){ 	
  message = '<h1>감자 ...혁진 감자합니다.</h1>'
} else {
  message = `<h1>${userName} .. 누구? ? </h1>`
}

document.write(message)		