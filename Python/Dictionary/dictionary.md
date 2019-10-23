# Dictionary

### 1. 기본기

- 가장 많이 사용되는 자료형
  - 웹 개발 중 마주칠 가능성이 가장 높다.
- 딕셔너리는 기본적으로 Key와 Value 구조
  - Key
    - 가능 : string, integer, float, boolean
    - 불가능 : list, Dictionary
  - Value : 모든 자료형 가능



#### 1.1 딕셔너리 만들기 (2가지 방법)

##### 첫번째 방법

```python
lunch = {
    '중국집' : '032'
}
```



##### 두번째 방법

```python
lunch = dict(중국집='032')
```



#### 1.2 딕셔너리 내용 추가하기

```python
lunch['분식집'] = '031'
```



#### 1.3 딕셔너리 내용 가져오기 (2가지 방법)

```python
artists = {
    '아티스트' : {
        '폴킴' : '허전해',
        '이민혁' : '아로하'
    }
}
```

- ##### 첫번째 방법

  ```python
  print(artists['아티스트']['폴킴'])  # 허전해
  ```

  

- ##### 두번째 방법

  ```python
  print(artists.get('아티스트').get('폴킴'))  # 허전해
  ```



#### 1.4 딕셔너리 반복문 활용하기

##### 1.4.1 기본 활용

```python
for key in lunch:
    print(key)          # key 값 출력
    print(lunch[key])   # key로 value 추출
# 중국집
# 032
# 분식집
# 031
```



##### 1.4.2 items()

- Key, Value 모두 가져오기

  ```python
  for key, value in lunch.items():
      print(key, value)
  # 중국집 032
  # 분식집 031
  ```

  

##### 1.4.3 values() 

- Value만 가져오기 

  ```python
  for value in lunch.values():
      print(value)
  # 032
  # 031
  ```

  

##### 1.4.3 keys()

- key만 가져오기 

  ```python
  for key in lunch.keys():
      print(key)
  # 중국집
  # 분식집
  ```

  

[연습문제](https://gist.github.com/educiao-hphk/2e18fcbad99d124ebb986ae751c53a71)

bit.do/yeoksam_python33



[연습문제정답](https://gist.github.com/educiao-hphk/1e4e0d72981c8e2ebfa93c67f44b25b2) 

bit.do/yeoksam_answer



[심화문제](https://gist.github.com/educiao-hphk/9aef8d9c59cf592635193aae6ac7cde2) 

bit.do/yeoksam_python_2

