def solution(phone_number):
    num = len(phone_number[:-4])*'*'
    num2 = phone_number[-4:]
    answer = num+num2
    return answer