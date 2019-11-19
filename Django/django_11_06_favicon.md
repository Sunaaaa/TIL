# Favicon

> [Favicon](https://www.favicon-generator.org/) 이미지를 제작하여, 애플리케이션의 Favicon 을 Customizing 할 수 있다. 

<br>

- 해당 application 하위에 favicon이라는 디렉토리를 생성한 뒤, favicon.ico 파일을 넣어준다. 

![1573002903531](https://user-images.githubusercontent.com/39547788/68260342-1cf73b80-0080-11ea-9046-fe729adef2e6.png)

<br>

- base.html에 아래의 코드 추가!

  ```javascript
  <link rel="shortcut icon" href="{% static 'articles/favicon/favicon.ico' %}" type="image/x-icon" >
  ```

  
<br>

- favicon 적용 화면 

  ![1573003386470](https://user-images.githubusercontent.com/39547788/68260343-1cf73b80-0080-11ea-856e-217d7febfed3.png)

<br>