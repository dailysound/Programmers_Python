def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = format(arr1[i],'b')
        arr2[i] = format(arr2[i],'b')
        
        blink = ''
        arr_sum = str(int(arr1[i]) + int(arr2[i]))
        #print(arr_sum)
        if len(arr_sum) < n:
            arr_sum = '0' * (n-len(arr_sum)) + arr_sum
    
        for i in arr_sum:
            if i == '0':
                blink = blink + ' '
            else:
                blink = blink + "#"
        answer.append(blink)
        
    return answer