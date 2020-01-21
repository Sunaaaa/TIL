test = int(input())
for t in range(1,test+1):
    n = int(input())
    my_list = list(map(int, input().split()))
    my_list.sort()

    max_num = 0
    answer = 0
    for i in my_list:
        cnt = my_list.count(i)
        if cnt >= max_num:
            max_num = cnt
            answer = i 

    print(f'#{t} {answer}')
