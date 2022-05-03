def solution(numbers):
    answer = []
    
    for num in numbers:
        bnum = list('0' + bin(num)[2:]) # bin을 사용하면 앞에 0b가 붙는데 이거 제외하고 표시
        # 짝수 일때 맨 뒤의 0을 1로 바꿈
        index = ''.join(bnum).rfind('0') # 오른쪽부터 0 찾기
        bnum[index] = '1'
        
        # 홀수 일때 맨뒤의 0을 1로 바꾼 후 다음번 값을 0으로 바꿈
        if num % 2 ==1:
            bnum[index+1] = '0'
        
        answer.append(int(''.join(bnum),2)) # 2진수를 10진수로 바꿀 때 int() 함수를 사용
    return answer