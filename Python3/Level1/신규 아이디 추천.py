def solution(new_id):
    answer = ''
    
    new_id = new_id.lower() # 소문자로 변환
    
    for i in new_id: # 소문자, 숫자, -,_,. 제외한 문자 제거
        if i.islower() or i.isdigit() or i in ["-","_","."]:
            answer += i
    
    while ".." in answer: # ..일 경우 .으로 대체
        answer = answer.replace("..",".")
    
    if answer[0] == ".": # 맨앞, 뒤에 .이 있으면 제거
        if len(answer) >= 2:
            answer = answer[1:]
        else:
            answer = "."
    if answer[-1] == ".":
        answer = answer[:-1]
    
    if answer == "": # 빈 문자열이면 a 대입
        answer ="a"
    
    if len(answer) >= 16: #길이가 16이상이면 15까지 자르고 맨뒤에 .가 있으면 제거
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer