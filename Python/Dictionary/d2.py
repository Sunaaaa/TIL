# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    '민승': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    '건희': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

score_list = []
stu_cnt = 0
print(score_list)

for key, value in scores.items():
    stu_cnt += 1
    print(key, value)

    for k,v in scores.get(key).items():
        print(k, v)
        score_list.append(v)


print(stu_cnt)   
print(sum(score_list)/stu_cnt)
