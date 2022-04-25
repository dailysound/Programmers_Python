def solution(dirs):
    s = set()
    answer = 0
    d={'U':[0, 1], "D":[0, -1], "R":[1, 0], "L":[-1, 0]}
    x=0  # 처음 위치
    y=0
    
    for dir in dirs:
        mx = x + d[dir][0] 
        my = y +d[dir][1]
        if -5<= mx <= 5 and -5 <= my <= 5: #이동 가능한 좌표로 이동하면 길 저장해두기
            m1 = (x, y, mx, my) #m1,m2는 같은 길
            m2 = (mx, my, x, y)
            
            if m1 not in s: # 저장된 길에 m1이 없으면 m1,m2 둘다 추가
                s.add(m1)
                s.add(m2)
                answer +=1

            x, y = mx, my

    return answer