# 문제 3.
# 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.

number = int(input('숫자를 입력하세요: '))

print("짝수" if number%2==0 else "홀수")

# 숫자를 입력하세요: 5
# 홀수

# 2로 나누었을 때 나머지가 나오면 홀수 

if number % 2 :
    print('홀수!')
else :
    print('짝수!')