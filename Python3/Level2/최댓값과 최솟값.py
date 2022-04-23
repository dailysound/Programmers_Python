def solution(s):
    k = list(map(int, s.split(' ')))
    
    return str(min(k))+ " "+str(max(k))
    