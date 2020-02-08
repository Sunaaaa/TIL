T=int(input())
arr=[2,3,5,7,11]

for i in range(T):
    num=int(input())
    cnt=[0 for i in range(5)]
    for j in range(len(arr)):
        while num%arr[j]==0:
            cnt[j]+=1;
            num=num/arr[j];					
    print(f'#{i+1}', end=' ')
    for j in cnt:
        print(j, end=' ')
    print()