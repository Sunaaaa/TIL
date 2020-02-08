n = int(input())
cnt = 0
for i in range(0,100):
    flag = True
    if i <= 1:
        continue
    h = i//2
    for j in range(2,h+1):
        if i%j==0:
            flag = False
            break

    if flag==True:
        print(i)
        cnt+=1


print(cnt)