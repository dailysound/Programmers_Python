from itertools import combinations
def solution(nums):
    result = []
    num = 0
    count = 0
    
    li = list(combinations(nums,3))
    
    for i in li:
        num = sum(i)
        result.append(num)
        
    for i in result:
        idx = 0
        for j in range(1, i+1):
            if i % j == 0:
                idx += 1
        
        if idx == 2:
            count +=1
        
    return count