def solution(n):
    answer = []
    
    for i in range(0, n+1): # 숫자 만큼 반복문 돌리기
        if i == 0: # 0/1일 때 리스트에 값 그냥 넣기(초기)
            answer.append(i)
        if i == 1:
            answer.append(i)
        if i >= 2: # 2부터 더하기 가능
            total = answer[i-1] + answer[i-2]
            answer.append(total % 1234567) # 더한 수를 1234567로 나눈 나머지값을 리스트에 저장
            # 돌릴때마다 안나누면 표현할 수 있는 값의 범위를 넘어가서 실패
            
    result = answer[n] # 리스트에 있는 나머지 값들 중 n번째 수가 정답
    return result