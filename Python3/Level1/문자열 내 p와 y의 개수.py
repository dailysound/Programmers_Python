def solution(s):
    s = s.lower()
    count_p = 0 
    count_y = 0
    for i in range(len(s)):
        if s[i] == 'p':
            count_p +=1
        if s[i] == 'y':
            count_y +=1
    if count_p == count_y:
        answer = True
    else:
        answer = False
    return answer