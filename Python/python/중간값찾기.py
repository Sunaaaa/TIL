test = int(input())
my_list = list(map(int, input().split()))
print(sorted(my_list)[len(my_list)//2])