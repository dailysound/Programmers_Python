def solution(a, b):
    nsum = 0
    for i in range(len(a)):
        nsum += (a[i] * b[i])
        
    return (nsum)