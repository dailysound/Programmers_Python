def solution(n):
    next_num = n
    nc = bin(n).count('1') # 주어진 10진수 2진수로 변환 후 1의 개수 nc에 저장
    nec = 0
    while nc != nec: # 주어진 수의 1의 개수와 다음 수의 1의 개수가 다름
        next_num+=1 # 숫자 하나 올리기
        nec = bin(next_num).count('1') # 올린 수 2진수 변환 후 1의 개수 nec에 저장
    answer = next_num # 1의 개수가 같으면 그때의 다음수가 정답
    
    return answer