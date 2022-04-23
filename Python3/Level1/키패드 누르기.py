def solution(numbers, hand):
    answer = ""
    keypad = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)}
    
    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:  # 2,4,6,8
            cur = keypad[i] #눌러야하는 키 딕셔너리에서 찾기
            lcur = keypad[lhand] #현재 왼손 위치
            rcur = keypad[rhand]  #현재 오른손 위치
            ldis = abs(cur[0] - lcur[0]) + abs(cur[1] - lcur[1])
            rdis = abs(cur[0] - rcur[0]) + abs(cur[1] - rcur[1])
            
            if ldis < rdis: #왼손이 더 가까울 때
                answer += 'L'
                lhand = i
            elif ldis > rdis: #오른손이 더 가까울 때
                answer += 'R'
                rhand = i
            else:  #거리가 같으면 hand값에 따라 사용
                if hand == "left":
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i
                    
    return answer