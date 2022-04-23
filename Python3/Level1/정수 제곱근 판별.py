import math

def solution(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        answer = pow(math.sqrt(n)+1, 2)
    else:
        return -1
    return answer