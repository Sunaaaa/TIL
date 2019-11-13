import heapq

def solution(scoville, K):
    s_list = scoville[1:]
    answer = 0
    sco_result = 0
    result = 0
    heap = []
    
    if len(scoville)==1:
        if scoville[0] >= K:
            print('K가 작아')
            return 0
        else:
            print('K가 커')
            return -1



    for i in s_list:
        heapq.heappush(heap, i)
    

    print(heap)
    
    result = scoville[0]
    while True:
        if sco_result >= K:
            return answer
        else :
            a = heapq.heappop(heap)
            sc = [result, a]
            print(min(sc))
            sco_result = min(sc) + ( max(sc) * 2 )
            result = sco_result
            answer += 1

    print(a)


    return -1

print(solution([1, 2, 3, 9, 10, 12],7))
print(solution([3],5))
print(solution([0],0))
print(solution([3],3))
print(solution([3],1))
print(solution([1, 2, 3, 9, 10, 12],7000))