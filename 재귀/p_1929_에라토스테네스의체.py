m, n = map(int, input().split())     
b = [False for i in range(n+1)]
b[0] = True
b[1] = True

for i in range(2,n+1):
    if b[i] == True:
        continue
    for j in range(i*2, n+1, 2):
        b[j] = True

print(b.count(False))
for i in range(m,n+1):
    if b[i] == False:
        print(i)