def solution(s):
    zero = 0
    re = 0
    while (1):
        re +=1
        zero += s.count('0')
        s= s.replace('0','') # 0제거하기
        new_s = bin(len(s))[2:] #0제거 후 길이 2진 변환
        if new_s == '1':
            break
        else:
            s = new_s

            
    return [re, zero]
        
        
        
