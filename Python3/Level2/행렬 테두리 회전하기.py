def solution(rows, columns, queries):
    answer = []
    arr = [[0 for col in range(columns+1)] for row in range(rows+1)] # 행렬 생성
    value = 1 # 1부터 채울거니까
    
    # 좌표와 인덱스가 같게 해줌
    for row in range(1, rows+1): # 1부터 순서대로 숫자 저장
        for col in range(1, columns+1):
            arr[row][col] = value
            value += 1
    
    for x1, y1, x2, y2 in queries:
        temp = arr[x1][y1] # 기준점 / 회전이 끝나고 마지막에 겹치는 부분에 넣어줘야함
        mini = temp # 회전할 때마다 최소값 비교 # 1번예 기준 처음에는 8이 들어가 있음
        
        for i in range(x1,x2): # 왼쪽 세로 회전 (↑ 방향)
            move = arr[i+1][y1]
            arr[i][y1] = move
            mini = min(mini, move)
            
        for i in range(y1, y2): # 하단 가로 회전 (← 방향)
            move = arr[x2][i+1]
            arr[x2][i] = move
            mini = min(mini,move)
            
        for i in range(x2, x1, -1): # 우측 세로 회전 (↓ 방향)
            move = arr[i-1][y2]
            arr[i][y2] = move
            mini = min(mini, move)
            
        for i in range(y2, y1, -1): # 상단 가로 회전 (→ 방향)
            move = arr[x1][i-1]
            arr[x1][i] = move
            mini = min(mini,move)
            
        arr[x1][y1+1] = temp
        answer.append(mini) 
    
    return answer