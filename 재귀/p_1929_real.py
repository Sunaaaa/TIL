def isP(num):
    if i <= 1:
        return False
    # h = i//2
    for j in range(2,i*i+1):
        if i%j==0:
            return False
    return True

import time
start = time.time() 
m, n = map(int, input().split())     
for i in range(m,n+1):
    if isP(i):
        print(i)
print("time :", time.time() - start)