import bisect
def solution(info, query):
    infos = {}
    temp = []
    answer = []
    for item in info:
        item = item.split()
        key, score = tuple(item[:4]), int(item[-1]) # 점수 전까지 key, 점수는 score에 저장
        temp.append((key, score))
    # 점수가 낮은것 부터 정렬 x[1] = 점수
    temp.sort(key=lambda x:x[1])
    
    for item in temp:
        key, score = item
        if key not in infos: # key가 딕셔너리에 없으면 새로 만들어서 저장
            infos[key] = []
        infos[key].append(score)
    
    
    for q in query:
        q = q.split()
        q = list(filter(lambda x:x != 'and',q)) # list 안쓰면 filter 타입으로 반환 <filter object at ~~> 이런식
        
        # 점수랑 문의 구분하기
        q_score = int(q[-1]) # 기준 점수
        q = q[:-1]
        
        # 딕셔너리의 키 저장
        q_key = list(infos.keys())
        
        
        for i in q:
            if i == '-':
                continue
            q_key = list(filter(lambda x: i in x, q_key))

        q_info = [infos[x] for x in q_key] 
        q_result = 0

        for score in q_info:
            index = bisect.bisect_left(score, q_score) # 쿼리의 기준 점수가 어디 인덱스에 들어갈지 
            # 예시 arr = [0,1,2,3,4,5] n=3일 때 bisect_left(arr, n) 이면 index = 3 / bisect_right(arr, n)이면 index=4
            cnt = len(score) - index
            q_result += cnt

        answer.append(q_result)

    return answer