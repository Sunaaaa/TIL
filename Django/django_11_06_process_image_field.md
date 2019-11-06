# ProcessedImageField

> 이미지 업로드를 통해 사용자로부터 이미지를 받을 때, 과도한 크기의 이미지가 업로드 되면 서버의 부하를 야기시킨다. 또 Thumbnail 크기가 너무 커지기 때문에 조절이 필요하다
>
> **djangi-imagekit을 활용해서 이미지 업로드 이미지 크기를 조절해보자!**
>
> - 사용자로부터 이미지를 업로드 받는 그 순간에 조절된 이미지 크기를 받을 수 있다. 
> - READ 로직을 수행할 때에도 일정하고 동일한 크기로 이미지를 보일 수 있다.

<br>

## 1. 라이브러리 설치

```bash
$ pip install Pillow
$ pip install pilkit
$ pip install django-imagekit
```

<br>

### [ Pillow ]

- PIL (Python Image Library) 프로젝트에서 fork 되어 나온 라이브러리
- Python3을 지원하지 않기 때문에 Pillow를 많이 쓴다.

<br>

### [ pilkit ]

- Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리
- 다양한 Processsors 지원
  - Thumbnail
  - Resize
  - Crop ...

<br>

### [ django-imagekit ]

- 이미지 썸네일 Helper

<br>



- 라이브러리 설치 확인

  ![1572999784740](https://user-images.githubusercontent.com/39547788/68260371-3a2c0a00-0080-11ea-82e5-5478ac277667.png)

<br>

<br>

## 2. App 등록

### INSTALLED_APPS 등록

- settings.py

  ```python 
  INSTALLED_APPS = [
      'articles',
      'students',
      'jobs',
      .
      .
  
      'imagekit',
      
      .
      .
      .
  ]
  ```

<br>

## 3. Modeling

- 기존의 models.py

  ```python
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
  
      # 원래 대로 라면, 새로운 필드를 추가하고 나면, makemigrations 할때, 
      # 어떤 값을 넣을 것인지 Django 가 물어본다. 기본적으로 blank = False이기 때문이다.
      # blank=True : '빈 문자열' 이 들어가도 된다.
      image = models.ImageField(blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      # 객체 표시 형식 수정
      def __str__(self):
          return f'[{self.pk}] : {self.title} '
  ```

- models.py 변경

  ```python 
  from django.db import models
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
  
      image = ProcessedImageField(
          processors=[Thumbnail(200,300)],    # 처리할 작업
          format='JPEG',              # 이미지 포맷
          options={                   # 각종 추가 옵션
              'quality' : 90
          },
          upload_to = 'articles/image' # 저장 위치
          # 실제 경로 : MEDIA_ROOT/articles/image
      )
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      # 객체 표시 형식 수정
      def __str__(self):
          return f'[{self.pk}] : {self.title} '
  
  ```

  <br>

## 4. Migration

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- ProcessedImageField의 인자로 들어가는 옵션들은 수정을 하더라도 다시 migration 하지 않아도 바로바로 적용이 된다.

<br>

![1573000497627](https://user-images.githubusercontent.com/39547788/68260370-39937380-0080-11ea-80b4-bf775354b7ba.png)



<br>

 

























































