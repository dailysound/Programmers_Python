def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations), 0, -1):
        count = 0
        for j in citations:
            if j >=i:
                count +=1
            if count >=i:
                return i
            if count == 0:
                return 0