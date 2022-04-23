def solution(answers):
    count = [0, 0, 0] #각 수포자 맞은 개수
    one = [1,2,3,4,5] 
    two = [2,1,2,3,2,4,2,5] 
    three = [3,3,1,1,2,2,4,4,5,5] 
    
    for i in range(len(answers)):
        ans = answers[i]
        if (one[i%len(one)] == ans):
            count[0] +=1
        if(two[i%len(two)] == ans):
            count[1] +=1
        if(three[i%len(three)] == ans):
            count[2] +=1
    
    answer = []
    for i in range(len(count)):
        if (count[i] == max(count)):
            answer.append(i+1)

    return (sorted(answer))