def solution(tickets):

    # 여행 경로를 담는 변수 선언
    routes = {}

    # tickets에 담긴 ticket들을 하나씩 꺼내어 사전에 담는다 
    # 출발지를 기준으로 출발지가 같은 여정의 도착지들을 dic에 담는다 
    for t in tickets:
        routes[t[0]] = routes.get(t[0],[]) + [t[1]]

    # r : 출발지
    # routes[r] : 출발지가 같은 여정의 도착지 리스트   
    for r in routes:
        routes[r].sort(reverse=True)  

    
    stack = ['ICN']
    path = []

    while len(stack) > 0:
        top = stack[-1]

        # 출발지가 top인 곳이 아예 없거나 다 사용한 경우
        if top not in routes or len(routes[top])==0:
            path.append(stack.pop())
        
        else:
            # 가장 마지막에 있는 도착지를 가져온다. 
            # -> 알파벳의 역순 (Z부터)으로 정렬했기 때문에 리스트의 끝에 있는 요소가 알파벳 순서가 앞서게 된다. 
            stack.append(routes[top][-1])

            # 해당 도착지는 경로에서 삭제 (pop) / 슬라이싱
            routes[top] = routes[top][:-1]

    # path[::-1] 역순
    return path[::-1]