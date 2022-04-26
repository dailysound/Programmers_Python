def solution(progresses, speeds):
    date = []
    answer = []
    for p,s in zip(progresses, speeds):
        day = 0
        while p < 100: #각 기능의 배포일 구하기
            p+=s
            day +=1
        date.append(day)
        
    front_day = 0 # 앞 배포일 인덱스 시작
    for i in range(1, len(date)):
        if date[front_day] < date[i]: # 앞 배포일이 뒷 배포일보다 작으면 i-front_day로 개수 구하고 answer에 추가
            # 앞 배포일을 i번째의 날짜로 바꿈
            # 앞 배포일이 뒷 배포일보다 크면 i만 증가한 채로 반복
            answer.append(i-front_day)
            front_day = i
    answer.append(len(date)-front_day)
    
    return answer