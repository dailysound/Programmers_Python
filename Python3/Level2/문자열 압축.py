def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2)+1):
        # 자를 수 있는 최대 길이는 문자열 길이의 반이다
        # ex) 8 'aabbaccc' -> 4 'aabb' 'accc' / 5 'aabba' 'ccc??' -> 에러 발생
        c = '' # 문자열을 잘랐을 때 나오는 문자열 저장
        count = 1
        temp = s[:i] # 처음 부분은 무조건 저장되어 있어야 함
        for j in range(i, len(s),i): # i만큼 문자열 자르기
            if temp == s[j:j+i]: # s의 다음 문자와 temp의 문자가 같으면 count 증가
                count +=1
            else:
                if count!=1:
                    c = c + str(count) +temp
                else: #1은 생략 가능
                    c = c + temp
                temp = s[j:j+i]
                count = 1
        if count != 1:
            c = c + str(count) + temp
        else:
            c = c + temp
        
        
        answer.append(len(c))
    print(min(answer))