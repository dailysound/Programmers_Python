def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max((i//n),(i%n))+1)
    
    # 인덱스를 n으로 나눈 나머지, 몫 중 큰 값에 1을 더하면 해당 위치의 값을 알 수 있다
    # n=3일때
    # index [0,1,2,3,4,5,6,7,8]
    # value [1,2,3,2,2,3,3,3,3]
    
    return answer