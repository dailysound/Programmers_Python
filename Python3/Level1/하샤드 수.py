def solution(x):
    answer = False
    num = 0
    num1 = [int(i) for i in str(x)]
    for i in range(len(num1)):
        num += num1[i]
    if x % num == 0:
        answer = True
    return answer