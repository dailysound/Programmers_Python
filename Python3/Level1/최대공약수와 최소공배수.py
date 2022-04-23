def solution(n, m):
    max_num = 0
    min_num = 0
    answer = []
    
    for i in range(1, max(n,m)+1):
        if (n % i == 0) & (m % i == 0):
            max_num = i
    answer.append(max_num)
    
    min_num = (n * m)//max_num
        
    answer.append(min_num)

    return answer