def solution(people, limit):
    answer = 0
    people.sort()
    
    start = 0 # 리스트 시작지점
    end = len(people) - 1 # 리스트의 마지막
    while start <= end: 
        answer +=1 # 구출할 수 없는 경우는 없음
        if people[start] + people[end] <= limit: # 가장 가벼운 사람 + 무거운 사람이 기준보다 작거나 같으면
            start +=1 
        end -=1
    
    return answer