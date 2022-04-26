def solution(s):
    answer = []
    s = s[2:-2] # 앞 뒤의 괄호 제거
    s = s.split("},{") # 사이사이의 괄호 제거
    s.sort(key=len) #원소의 길이가 작은순으로 정렬
    for i in s:
        new_s = i.split(',') # 각각의 원소를 , 기준으로 구분
        for j in new_s: # 구분된 원소들 하나씩
            if int(j) not in answer: # 배열에 없으면 추가
                answer.append(int(j))
    return answer
    
    