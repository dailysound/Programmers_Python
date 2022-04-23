def solution(lottos, win_nums):
    answer = []
    unknown = lottos.count(0)
    match = 0
    
    for i in lottos:
        if i !=0 and i in win_nums: # 숫자가 0이 아니고 당첨 번호에 있을 때
            match +=1
            
    answer.append(7-(match + unknown)) #최소로 맞춤
    answer.append(7-match) # 최대로 맞춤
    
    if unknown == 6: # 다 모를 때
        answer = [1, 6]
    elif unknown == 0 and match == 0: # 모든 번호를 알지만 맞는게 없을 때
        answer = [6, 6]
   
    return answer