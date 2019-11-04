# 2019-10-31(목) 전생 직업 APP

> [Faker API](https://faker.readthedocs.io/en/master/)를 활용한 전생 직업 App을 만들어 보자. 

<br>

## [Flow]

[1. 사전 작업]

- Faker API 사용법 익히기 -> Shell_plus 이용
- 'jobs' Application 생성
  - name : 입력받은 사용자 이름
  - past_job : 전생 직업
- 관리자 페이지 등록



<br>

[2. 기능 구현]

- 사용자 이름을 입력 받는 함수 (HTML Form 건네줌)

  [기본]

  - 이름에 따라 전생 직업을 알려주는 함수 

    - Faker API를 통해 직업정보 가져오기

    - 해당 이름을 처음 조회할 때 이름-직업 정보를 DB에 저장시켜버림

      즉, 이름을 여러번 조회하더라도 처음 저장된 직업이 바뀌지 않음

  [심화]

  - GIPHY API를 사용해서 직업에 따른 움짤도 함께 보여주기
    - GIPHY API 회원가입 & API KEY 발급 받기
    - 공식문서 보면서 요청 보내서 움짤 받아보기 
      - 주소창에 URL + 쿼리 스트링 직접 넣어보면서 사진 정보가 잘 오는지 먼저 확인을 하는게 좋다.

<br>

## 1.1 Faker 설치 

```bash
$pip install Faker
```

- 설치 완료 

  ![1572503050399](https://user-images.githubusercontent.com/39547788/67948173-90382200-fc28-11e9-8ef3-b4838c09466d.png)

  <br>



### 1.1.1 Faker 사용하기

> Shell_Plus를 이용해 Faker를 익혀보자.

<br>

- shell_plus 실행

  ```bash
  $ python manage.py shell_plus
  ```

  <br>

  - Faker import 하기

    ```python 
    In [1]: from faker import Faker
    ```

  - Faker 생성

    ```python 
    In [3]: fake = Faker()
    ```

    <br>

    - Faker의 name

      ```python 
      In [3]: fake = Faker()
      
      In [4]: fake.name()
      Out[4]: 'Sheila Jones'
      
      In [5]: fake.name()
      Out[5]: 'Patrick Gutierrez'
      
      In [6]: fake.name()
      Out[6]: 'Michael Sharp'
      ```

      <br>

    - Faker의 address

      ```python 
      In [7]: fake.address()
      Out[7]: 'USCGC Booker\nFPO AA 86948'
      
      In [8]: 
      
      In [8]: fake.address()
      Out[8]: '42404 John Plain\nAndersontown, IA 45609'
      ```

      <br>

    - Faker의 text

      ```python 
      In [9]: fake.text()
      Out[9]: 'Talk sport its environmental truth. Less political anything food.\nBit later big soon heavy practice. Much agree back speak whom agent media. Population bed once capital network challenge method.'
      
      In [10]: fake.text()
      Out[10]: 'Someone land hotel soon fast gun. Where middle current reduce.\nAttorney yard
      world. Cultural stop thought inside wall. Feeling activity man discover itself name.
      ```

      <br>

    - Faker의 job

      ```python 
      In [11]: fake.job()
      Out[11]: 'Herpetologist'
      
      In [12]: fake.job()
      Out[12]: 'Runner, broadcasting/film/video'
      
      In [13]: fake.job()
      Out[13]: 'Horticultural consultant'
      ```

      

    <br>

  - 한글로 Faker 생성

    ```python 
    In [15]: fake=Faker('ko_KR')
    
    In [16]: fake.job()
    Out[16]: '의무기록사'
    
    In [17]: fake.job()
    Out[17]: '악기제조 및 조율사'
    
    In [18]: fake.job()
    Out[18]: '치과기공사'
    
    In [19]: fake.job()
    Out[19]: '간호조무사'
    
    In [20]: fake.job()
    Out[20]: '통신공학 기술자 및 연구원'
    
    In [21]: fake.job()
    Out[21]: '건설자재 시험원'
    
    In [22]: fake.job()
    Out[22]: '가구 제조 및 수리원'
    ```

    <br>

## 1.2 jobs Application 

### 1.2.1 Application 생성

```bash
$ python manage.py startapp jobs
```

- 생성화면

  ![1572503798673](https://user-images.githubusercontent.com/39547788/67948174-90382200-fc28-11e9-87d0-2e9befbc5dd5.png)

<br>

### 1.2.2 Application 등록

- settings.py 에 jobs Application을 등록한다.

![1572503922246](https://user-images.githubusercontent.com/39547788/67948175-90382200-fc28-11e9-8525-a3ae51fcd552.png)

<br>



### 1.2.3 Model 등록 및 Migrate

- models.py

  ```python 
  from django.db import models
  
  # Create your models here.
  class Job(models.Model):
      name = models.CharField(max_length=30)
      past_job = models.TextField()
  
      # def __str__(self):
      #     return f'[{}]'
      
  ```

  <br>

- Model 등록

  ```bash
  $ python manage.py makemigrations
  ```

  - 실행 화면

    ![1572504054839](https://user-images.githubusercontent.com/39547788/67948178-90d0b880-fc28-11e9-9522-2dfc5c1eddf9.png)

  <br>

- Model 등록 확인  `showmigrations`

  ```bash
  $ python manage.py showmigrations
  ```

  - 확인

    ![1572505292884](https://user-images.githubusercontent.com/39547788/67948179-90d0b880-fc28-11e9-8708-b96794f34f6a.png)

  <br>

- migrate! 후 테이블 생성 확인

  ```bash
  $ python manage.py migrate
  ```

  - 실행 화면

    ![1572505376994](https://user-images.githubusercontent.com/39547788/67948181-90d0b880-fc28-11e9-97a6-d3c64bab488f.png)

  <br>

  - sqlite로 확인

    ![1572505451166](https://user-images.githubusercontent.com/39547788/67948183-91694f00-fc28-11e9-80de-effc34bf03f2.png)

  

  <br>

## 1.3 관리자 페이지에 등록

- admin.py

  ```python 
  from django.contrib import admin
  from .models import Job
  
  # Register your models here.
  
  # 커스터 마이징한 ModelAdmin
  class JobAdmin(admin.ModelAdmin):
      list_display = ('pk', 'name', 'past_job',)
  
  admin.site.register(Job, JobAdmin)
  ```

  <br>

  - 실행 화면

    ![1572506269263](https://user-images.githubusercontent.com/39547788/67948184-91694f00-fc28-11e9-953a-4691e8f64cd3.png)

<br>





