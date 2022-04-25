def solution(board):
    h = len(board)
    w = len(board[0])
    answer = 0

    if len(board) <2 and 1 in sum(board,[]):
        return 1
    
    for i in range(1, h):
        for j in range(1, w):
            if board[i][j] ==1:
                board[i][j] = min(board[i-1][j],board[i-1][j-1],board[i][j-1]) +1
                answer = max(answer, board[i][j])
    return answer**2
            