def solution(numbers):
    num = list(map(str, numbers)) # str으로 바꾼 뒤 list로 변환
    num.sort(key = lambda x : x * 3, reverse=True) 
    # key 조건에 맞게 정렬
    # x3 하는 이유 : 원소 크기가 1,000이하 이므로 3자리 숫자로 맞춰서 비교하려고
    # 문자열은 ASCII 값으로 치환 후 정렬, 
    
    answer = str(int(''.join(num)))
    # int 후에 str하는 이유 : 모든 값이 0일 때를 처리하기 위해
    
    return answer
