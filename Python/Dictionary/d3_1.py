# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
'''
출력 예시)
서울 : 평균온도
대전 : 평균온도
광주 : 평균온도
부산 : 평균온도
'''

for key, values in cities.items():
    # print(key, ':', sum(values)/len(values))
    print(f"{key} : {sum(values)/len(values)}")
