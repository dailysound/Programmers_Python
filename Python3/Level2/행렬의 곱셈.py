def solution(arr1, arr2):
    alen = len(arr1)
    blen = len(arr2[0])

    answer = [[0] * blen for _ in range(alen)]

    for i in range(alen):
        for j in range(blen):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer