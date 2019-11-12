# User - Article & Comments

> django가 프로젝트를 실행 시키면, `INSTALLED_APPS` Application을 들고 오고, 각 Application에 해당하는 model들을 import한다. 그래서 import 한 뒤에 사용 할 수 있다. 
>
> - 만약, User를 사용해서 정의한다 했을 때 import 되지 않았을 때 사용해야하는 경우가 발생한다. 
>   - `get_user_model()` 
>     - 클래스의 모델이 먼저 import 될 수 있도록 해야 한다. 
>   - `settings.AUTH_USER_MODEL`
>     - 순서의 영향을 받지 않기 때문에 모델 정의할 때 사용하도록 한다. 

<br>

- User 클래스 가져오는 법

  - settings.AUTH_USER_MODEL

    - return str

    - models.py 에서 모델 정의할 때만 사용한다.

      ```python 
      from django.conf import settings
      settings.AUTH_USER_MODEL
      ```

  - get_user_model()

    - return Class

    - models.py 제외한 모든 곳

      ```
      
      ```



<br>

<br>

## 게시글 작성자 정보 넣기

### [ articles Application ]

- 모델 정의

  - 게시글 작성자에 대한 정보를 넣기 위해 Article 클래스에 User 클래스를 외래키로 설정한다.

    ```python 
    from django.conf import settings
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ```

  - models.py

    ```python 
    from django.db import models
    from imagekit.models import ProcessedImageField
    from imagekit.processors import Thumbnail
    from django.conf import settings
    
    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=40)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
        # 객체 표시 형식 수정
        def __str__(self):
            return f'[{self.title}] {self.content}'
    ```

    <br>



- 마이그레이션

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  <br>

- user 외래키 설정 확인

  ![1573518666673](C:%5CUsers%5Cstudent%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5C1573518666673.png)

  <br>

- 새로운 게시글을 작성할 때 작성자에 대한 정보를 넣는 로직을 추가한다.
  - views.py
    - article이 바로 저장되지 않도록 `article = form.save(commit=False)`를 설정한다.
    - `request.user`를 이용해 게시글 작성자를 설정한 뒤, `article.save()`를 통해 새로운 게시글을 등록한다. 

- 실행 화면

  - index.html

    ![1573520089171](User%20-%20Article%20&%20Comments.assets/1573520089171.png)

  - sqlite3

    ![1573519817399](C:%5CUsers%5Cstudent%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5C1573519817399.png)

