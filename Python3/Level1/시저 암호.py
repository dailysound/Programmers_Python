def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr(ord(i)+n) if ord(i)+n<= 90 else chr(ord(i)-26+n)
        elif i.islower():
            answer += chr(ord(i)+n) if ord(i)+n<= 122 else chr(ord(i)-26+n)
        elif i == " ":
            answer += i
    return answer