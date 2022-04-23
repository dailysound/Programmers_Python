def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[len(participant)-1]

# def solution(participant, completion):
#     hashDict = {}
#     sumHash = 0
    
#     for part in participant:
#         hashDict[hash(part)] = part
#         sumHash += hash(part)
        
#     for comp in completion:
#         sumHash -= hash(comp)
        
#     return hashDict[sumHash]