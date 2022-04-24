def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = len(prices) -i -1 #끝까지 안떨어질 경우 미리 저장
        
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                time = j - i
                break
        answer.append(time)
    # answer.append(0) # 마지막 원소는 비교할 숫자가 없음
    return answer
                