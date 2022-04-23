def solution(land):
    for i in range(1, len(land)): # 첫 행 제외하고 두번째 행부터 
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:]) # 기준점이랑 겹치지 않는 열 구해서 더한 후 최대값 저장
    
    return max(land[len(land)-1]) #마지막행에 모두 더한 값이 있으므로 마지막행에서 최대값 구하기