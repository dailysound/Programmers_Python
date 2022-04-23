def solution(arr):
    div = len(arr)
    total = 0
    for i in range(div):
        total += arr[i]
        
    answer = total/div
    return answer