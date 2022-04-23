def solution(n):
    answer = []
    result = 0
    sentence = str(n)
    
    for i in sentence:
        answer.append(int(i))
    
    result = sum(answer)

    return result