def solution(s):
    match = []
    for i in range(len(s)):
        if not match:
            match.append(s[i])
        else:
            if s[i] == match[-1]: # match의 마지막 값과 일치하면 match에서 문자열 빼기
                match.pop()
            else: # 일치하지 않으면
                match.append(s[i])
                
    if match: #match에 값이 들어가 있으면 성공적으로 수행 못한 경우임
        return 0
    else:
        return 1