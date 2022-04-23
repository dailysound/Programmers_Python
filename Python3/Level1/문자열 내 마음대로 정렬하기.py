def solution(strings, n): 
    return list(sorted(strings, key = lambda x: (x[n], x.lower())))