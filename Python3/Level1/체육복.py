def solution(n, lost, reserve):
    nlost = list(set(lost) - set(reserve))
    nreserve = list(set(reserve) - set(lost))
    
    answer = n - len(nlost) 
    
    print(nlost, nreserve)
    
    for i in nlost:
        if i-1 in nreserve:
            answer += 1
            nreserve.remove(i-1)
        elif i+1 in nreserve:
            answer +=1
            nreserve.remove(i+1)
    
    return answer