def solution(record):
    info = {}
    msg = []
    ids = []
    
    for log in record:
        log_v = log.split()
    
        if log_v[0] == "Enter":
            info[log_v[1]] = log_v[2] # 딕셔너리에 유저아이디와 유저네임 저장
            ids.append(log_v[1]) # 아이디만 추가
            msg.append(info[log_v[1]]+"님이 들어왔습니다.")
        elif log_v[0] == "Leave":
            ids.append(log_v[1])
            msg.append(info[log_v[1]]+"님이 나갔습니다.")
        else: # log_v[0] == "Change" 이면 userid에 해당하는 이름을 변경
            info[log_v[1]] = log_v[2]
  
    for i in range(len(msg)):
        username = info[ids[i]] # 모아둔 아이디에 해당하는 유저네임 저장
        if msg[i][len(msg[i])-7:] == "들어왔습니다.":
            msg[i] = username+"님이 들어왔습니다."
        else:
            msg[i] = username+"님이 나갔습니다."
            
    return msg