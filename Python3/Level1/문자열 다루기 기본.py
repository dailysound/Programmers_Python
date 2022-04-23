def solution(s):
    answer = False
    slen = len(s)
    if s.isnumeric():
        answer = True
    return answer and (slen == 4 or slen == 6)