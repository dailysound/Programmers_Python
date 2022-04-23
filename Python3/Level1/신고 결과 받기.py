from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list) # 각 유저별 신고 횟수 초기화
    cond_user = [] # k번 이상 신고된 유저
    
    report = set(report) #중복된 신고 결과 제거
    
    report_user = defaultdict(set) # 신고한 유저
    reported_num = defaultdict(int) # 신고당한 횟수
    
    for blink in report:
        user_a, user_b = blink.split() # 공백 기준으로 신고한사람 a, 신고당한 사람 b
        
        reported_num[user_b] +=1
        report_user[user_a].add(user_b)
        
        if reported_num[user_b] == k:
            cond_user.append(user_b) #k번 신고당한 유저 리스트에 추가
    
    for s in cond_user:
        for i in range(len(id_list)):
            if s in report_user[id_list[i]]:
                answer[i] +=1
                
    return answer