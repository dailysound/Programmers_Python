def solution(n,a,b):
    count = 0
    while a!=b:  # 같은 숫자일 때 만남
        a = (a//2) + (a%2)
        b = (b//2) +(b%2)
        count +=1
        if a==b:
            return count
        

# 몫 + 나머지가 동일하면 같이 만난다
#     몫 나머지 합
# 1   0    1   1
# 2   1    0   1
# 3   1    1   2
# 4   2    0   2
# 5   2    1   3
# 6   3    0   3
# 7   3    1   4
# 8   4    0   4