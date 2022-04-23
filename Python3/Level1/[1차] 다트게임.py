def solution(dartResult):
    tmp = ''
    score = []
    
    for i in dartResult:
        if i.isnumeric():
            tmp += i
        elif i == 'S':
            tmp = int(tmp) ** 1
            score.append(tmp)
            tmp = ''
        elif i == 'D':
            tmp = int(tmp) ** 2
            score.append(tmp)
            tmp = ''
        elif i == 'T':
            tmp = int(tmp) ** 3
            score.append(tmp)
            tmp = ''
            
        if i == '*':
            if len(score) >=2:
                score[-1] = score[-1] * 2
                score[-2] = score[-2] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * (-1)        
                

    print(sum(score))