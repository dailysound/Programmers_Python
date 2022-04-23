def solution(n):
    main = ''
    answer = 0
    while(1):
        if n > 1:
            main+=str(n%3)
            n=(n//3)
        if n < 3:
            main+=str(n)
            break
    for i in range(len(main)):
        answer += int(main[-(i+1)]) * (3**i)
    return answer