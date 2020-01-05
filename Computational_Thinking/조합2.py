# 문제2 
# x+y+z=100의 자연수 해를 모두 출력하는 프로그램을 작성하라. 

count = 0
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            if x+y+z==100:
                count+=1
                print('x :', x, 'y :', y, 'z :', z )

print(count)