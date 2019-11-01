def solution(arr):

    d = {}
    result = []
    for i in arr:
        if i in d.key():
            result.append((i,d.get(i))
            
        else:
            d[i] = d.get(i,0)

        for key in d.keys():
            d[key] = d.get(key)+1

    print(d)
    print(result)

    # for i in arr:


    answer = 2
    return answer
   

print(solution([2, 1, 3, 1, 4, 2, 1, 3]))
# print([1, 2, 3])