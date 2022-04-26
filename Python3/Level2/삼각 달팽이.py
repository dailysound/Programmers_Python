def solution(n):
    # 반복 횟수는 n과 같음 (아래 -> 오른쪽 -> 위쪽 -> 아래 ...)
    # 이동 횟수는 1씩 감소 (n -> n-1 -> n-2 ... 1)
    # 방향이 3가지 = 나머지가 0이면 아래, 1이면 오른쪽, 2이면 위쪽으로 위치 이동
    answer = [[0 for j in range(1,i+1)] for i in range(1, n+1)]
    x = -1 # 처음엔 무조건 내려가는 방향
    y =  0
    num = 1
    
    for i in range(n): # 0 ~ n-1번 반복
        for j in range(i, n):
            if i % 3 == 0: # 아래
                x+=1
            elif i % 3 == 1: # 오른쪽
                y+=1
            else: # 위쪽
                x-=1
                y-=1
            answer[x][y] = num # (0,0) 일때 1 저장
            num+=1
    return sum(answer,[])