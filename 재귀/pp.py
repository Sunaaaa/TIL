n = int(input())
my_list = list(map(int, input().split()))
cnt = 0
for i in my_list:
    flag = True
    if i <= 1:
        continue
    if i==2:
        cnt+=1
        continue

    h = i//2
    for j in range(2,h+1):
        if i%j==0:
            flag = False
            break

    if flag==True:
        cnt+=1

print(cnt)