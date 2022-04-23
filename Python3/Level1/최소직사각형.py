def solution(sizes):
    answer = 0
    w = []
    h = []
    tmp = [[0 for j in range(2)] for i in range(1)]
   
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
            
    for i in range(len(sizes)):
        w.append(sizes[i][0])
        h.append(sizes[i][1])
        
    answer = max(w) * max(h)
    return answer