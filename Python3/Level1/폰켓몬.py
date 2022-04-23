def solution(nums):
    pick = len(set(nums))
    
    if len(nums)//2 > pick: #가져가야하는 수가 종류보다 많으면 답은 종류
        return pick
    else: 
        return len(nums)//2