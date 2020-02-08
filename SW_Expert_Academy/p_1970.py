T=int(input())
m=[50000,10000,5000,1000,500,100,50,10]
for i in range(T):
    cnt=[]
    money=int(input())
    for j in range(len(m)):
        cnt.append(money//m[j])
        money=money%m[j] 
    print(f'#{i+1}')
    for j in cnt:
        print(j,end=" ")
    print()