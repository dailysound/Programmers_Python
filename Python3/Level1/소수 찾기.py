def solution(n):
    init = [True] * (n+1)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if init[i] == True:       
            for j in range(i+i, n+1, i):
                init[j] = False
    
    result = [i for i in range(2, n+1) if init[i] == True]
    return len(result)