# def n_convert(num, base):
#         basic = "0123456789ABCDEF"
#         q, r = divmod(num, base) # 0부터 base(진법)에 맞춰 몫, 나머지 저장

#         if q == 0: # 몫이 0
#             return basic[r]
#         else: # n진수의 다음자리 구하기
#             return n_convert(q, base) + basic[r]

def n_convert(num, base):
    basic = "0123456789ABCDEF"
    r = ''
    if num == 0:
        return '0'
    while num:
        r = basic[num%base] + r
        num //= base
    return r

def solution(n, t, m, p):        
    answer = ""
    temp = []
    
    for i in range(m*t): #범위는 인원수*미리 구할 숫자의 개수만큼
        convert = n_convert(i,n)
        for c in convert:
            temp.append(c) # n_convert 함수에서 구한 숫자들 temp에 추가
    
    for i in range(p-1,m*t,m): # 튜브가 말할 답만 추출하기
        # p-1 튜브의 순서 시작부터 인원수 만큼 건너뛰고 튜브 순서만 추출
        answer += temp[i]
        
    return answer

