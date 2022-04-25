from itertools import permutations

def solution(k, dungeons):
    dungeons = list(permutations(dungeons, len(dungeons)))
    # 던전을 도는 모든 순서쌍
    num = []
    count = 0 # 탐험한 던전 수

    for dungeon in dungeons:
        pk = k #현재 피로도
        for p, u in dungeon: # p= 피로도, u=소모되는 피로도
            if pk >= p: # 현재 피로도가 최소 피로도 이상이면
                pk-=u # 현재 피로도에서 소모되는 피로도 감소
                count+=1 # 탐험한 던전 수 올리기
            else: # 현재 피로도가 최소 피로도보다 작으면 탐험 종료
                break
        num.append(count) # 조합별 탐험 던전 수 추가
        count = 0
    return max(num) # 그중 가장 많이 탐험한 수 출력