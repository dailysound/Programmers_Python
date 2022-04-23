def solution(n):
    answer = ""
    
    while(n):
        if n % 3 != 0: # n이 3의 배수가 아니면
            answer += str(n%3) # 나머지 answer에 저장
            n = (n//3) # 몫 계속 나누기
        else: # n이 3의 배수이면
            answer += "4" # 끝자리는 계속 4이므로 더해줌
            n = (n//3)-1 # 나눈 몫에서 1 빼기
    
    return answer[::-1]
            