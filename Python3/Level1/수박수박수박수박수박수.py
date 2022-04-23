def solution(n):
    answer = '수박'
    if n==1:
        return str(answer[0])
    elif n%2==0:
        return str(answer*(n//2))
    else:
        return str(answer * (n//2) + answer[0])