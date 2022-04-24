def solution(priorities, location):
    if len(priorities) == 1:
        return 1
    leng = len(priorities)
    count = 1
    first = priorities.pop(0) # 대기목록 중 맨 앞의 문서 따로 빼기
    
    while priorities:
        if location > 0:
            if first < max(priorities): # 맨 앞 문서보다 중요도가 높은 문서가 존재하면
                priorities.append(first) # 맨 뒤에 넣기
            else:
                count += 1
            location -= 1 # 문서를 뒤에 넣든 바로 출력하든 내가 원하는 문서의 위치는 하나 땡겨짐
        else: # 내가 원하는 문서의 위치가 0이면
            if first < max(priorities):
                priorities.append(first)
                location = len(priorities) - 1 # 내가 원하는 문서가 맨 뒤에 위치
            else: # 아니면 바로 출력
                break
        first = priorities.pop(0) # 맨 앞 문서 다시 빼고 반복
    
    if not priorities: # 인쇄할 위치가 마지막이면
        answer = leng
    else: 
        answer = count
    return answer

