def solution(p):
    # 1과정
    if not p:
        return ""
    
    #2과정
    u,v = divide(p)
    
    #3과정
    if check_u(u):
        #3-1과정
        return u + solution(v)
    #4과정
    else:
        #4-1과정
        answer = '('
        #4-2과정
        answer += solution(v)
        #4-3과정
        answer += ')'
        
        #4-4과정
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer

    
    # 문자열 u와 v로 분리
def divide(p):
    lc = 0
    rc = 0
    for i in range(len(p)):
        if p[i] == '(':
            lc +=1
        elif p[i] == ')':
            rc +=1
        if lc == rc: # (와 )의 개수가 같으면 count는 0이고 그때의 i까지가 균형잡힌 괄호 문자열이므로 u에 저장/나머지 괄호 문자열은 v에 저장
            return p[:i+1], p[i+1:]

# u가 올바른 괄호 문자열인지 확인        
def check_u(u):
    check = []
    
    for i in u:
        if i == '(':
            check.append(i)
        else:
            if not check:
                return False
            check.pop()
    return True
