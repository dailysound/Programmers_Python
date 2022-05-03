def clear(board, m, n):
    pop_set = set() # 중복 계산이 되지 않도록 set을 사용한다
    for i in range(1, n): #(1,1) 부터 시작해 왼쪽, 위쪽, 왼쪽 대각선 위쪽을 비교하며 4칸이 같은 블록을 찾는다
        for j in range(1, m):
            if board[i][j] == board[i-1][j-1] == board[i][j-1] == board[i-1][j] !='_':
                pop_set |= set([(i,j),(i-1,j-1),(i-1,j),(i,j-1)])
    
    for i, j in pop_set:
        board[i][j] = 0 # 터진 좌표의 값을 0으로 만든다
    for i ,row in enumerate(board):
        empty = ['_'] * row.count(0) # 0이된 개수만큼 '_'를 위치시킨다
        board[i] = empty + [block for block in row if block !=0]
    return len(pop_set) # 터진 곳의 길이(개수) 반환

def solution(m,n,board):
    count = 0
    board = list(map(list, zip(*board))) # 행과 열을 바꾼 후 사용한다
    
    while True:
        pop = clear(board, m, n)
        if pop == 0:
            return count
        count+=pop