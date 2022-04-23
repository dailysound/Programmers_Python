def solution(N, stages):
    fail_rate = {}
    pclist = []
    fclist = []
    for i in range(1, N+1):
        pcount = 0
        fcount = 0
        for j in range(len(stages)): 
            if stages[j] >= i:  # 각 스테이지 별 도전한 사용자 수
                pcount += 1
            if stages[j] == i:  # 각 스테이지 별 실패한 사용자 수
                fcount +=1 
            
        pclist.append(pcount)
        fclist.append(fcount)
        if pcount == 0:
            fail_rate[i] = 0
        else:
            fail_rate[i] = fclist[i-1]/pclist[i-1]
    
    answer = sorted(fail_rate, key =lambda x : fail_rate[x], reverse=True)

    
    return answer