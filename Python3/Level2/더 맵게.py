import heapq
def solution(scoville, K):
    cnt = 0 # 더한 횟수
    
    scoville.sort()
    
    while scoville[0] <= K: # 정렬 후 맨 앞이 기준 숫자보다 높으면 다 기준점을 넘기기 때문
        if len(scoville) == 1:
            return -1
        min_sum = heapq.heappop(scoville)
        min_sum += (heapq.heappop(scoville))*2
        heapq.heappush(scoville, min_sum)
        cnt += 1 # 섞은 횟수 올리기
        
    return cnt