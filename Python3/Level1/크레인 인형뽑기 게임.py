def solution(board, moves):
    bucket = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                bucket.append(board[j][i-1])    # 크레인이 내려오는 곳에 인형이 있을 때
                board[j][i-1] = 0    # 뽑힌 숫자(인형)은 0으로 변경

                # bucket에 인형이 2개 이상 있을때마다 확인
                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:    # 마지막 두 개의 숫자가 같을 때
                        bucket.pop(-1)    
                        bucket.pop(-1)    # 그 두개를 pop
                        answer += 2     
                break
    return answer