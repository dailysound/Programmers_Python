def solution(clothes):
    closet = {}
    result = 1
    
    for i in clothes:
        if i[1] in closet.keys(): # dict의 keys 중 clothes의 키가 있으면 값 추가
            closet[i[1]].append(i[0])
        else:  # 없으면 리스트 추가
            closet[i[1]] = [i[0]]
        
    for value in closet.values(): # dict의 값들 중 하나씩 돌리면서 경우의 수 구하기
        result = result * (len(value) + 1) 

    return result-1  # 아무것도 안입는 경우 빼기