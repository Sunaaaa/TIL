# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

score_list = []

for v in score.values():
    score_list.append(v)
    
# print(score_list)

print(sum(score_list))

