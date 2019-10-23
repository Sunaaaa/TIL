# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

min_t = 1000
min_c = ''
max_t = -1000
max_c = ''

for key, value in cities.items():
    if max(value) > max_t:
        max_t = max(value)
        max_c = key

    if min(value) < min_t:
        min_t = min(value)
        min_c = key

print('가장 추웠던 곳 : ', min_c)
print('가장 더웠던 곳 : ', max_c)


