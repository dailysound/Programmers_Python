def solution(s):
    s = s.split(' ')
    total = []
    answer = ""
    
    for i in s:
        total.append(i.capitalize())
    print(total)
    
    answer = " ".join(total)
    return answer