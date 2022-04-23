def solution(left, right):
    answer = 0
    even = []
    odd = []
    cnt = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt +=1
        if cnt % 2 == 0:
            even.append(i)
            cnt = 0
        else:
            odd.append(i)
            cnt = 0
    
    answer = sum(even) - sum(odd)
    return int(answer)