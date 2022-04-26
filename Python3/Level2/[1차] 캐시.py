def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower() # 대소문자 구분 없음
        if cacheSize !=0: # 캐시 용량이 남아있을 때 
            if not city in cache: # cache에 도시가 없을때 miss
                if len(cache) == cacheSize:
                    cache.pop(0) # 선입 캐시 삭제
                cache.append(city) # 마지막에 최근 도시 추가
                time += 5
            else: # 캐시에 도시가 있을 때
                cache.pop(cache.index(city)) # cache에서 해당 도시 제거
                cache.append(city) # 맨 뒤에 다시 저장
                time += 1
        else: # 캐시 사이즈가 0이면 miss 만 발생
            time += 5
            
    return time
                    
                    