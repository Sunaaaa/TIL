# 1.1 딕셔너리 만들기 (2가지 방법)
# 첫번째 방법
lunch = {
    '중국집' : '032'
}

# 두번째 방법
lunch = dict(중국집='032')

# 1.2 딕셔너리 내용 추가하기
lunch['분식집'] = '031'

# 1.3 딕셔너리 내용 가져오기 (2가지 방법)
artists = {
    '아티스트' : {
        '폴킴' : '허전해',
        '이민혁' : '아로하'
    }
}

# 폴킴의 대표곡은?
# 첫번째 방법
print(artists['아티스트']['폴킴'])  # 허전해

# 두번째 방법
print(artists.get('아티스트').get('폴킴'))  # 허전해


# 1.4 딕셔너리 반복문 활용하기
# 1.4.1 기본 활용
for key in lunch:
    print(key)          # key 값 출력
    print(lunch[key])   # key로 value 추출
# 중국집
# 032
# 분식집
# 031



# 1.4.2 items() : Key, Value 모두 가져오기
for key, value in lunch.items():
    print(key, value)
# 중국집 032
# 분식집 031


# 1.4.3 values() : Value만 가져오기 
for value in lunch.values():
    print(value)
# 032
# 031


# 1.4.3 keys() : key만 가져오기 
for key in lunch.keys():
    print(key)
# 중국집
# 분식집
