def solution(s):
    cnt = 0
    if s.count('(') != s.count(')'): # (와 )의 개수가 다르면 올바르지 않은 괄호
        return False
    
    for i in s:
        if i == '(':
            cnt+=1
        else:
            cnt-=1
            
        if cnt < 0: # 중간에 한번이라도 음수가 되면 짝이 안맞는다는 것
            return False
    
    return True