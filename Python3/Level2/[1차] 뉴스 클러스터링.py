def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    new_str1 = []
    new_str2 = []
    inter_li = []
    sum_li = []  
    
    for i in range(1, len(str1)):
        if str1[i-1:i+1].isalpha():
            new_str1.append(str1[i-1:i+1]) 
            sum_li.append(str1[i-1:i+1])
            
    copy1 = new_str1.copy()
    copy2 = new_str1.copy()
    
    for i in range(1, len(str2)):
        if str2[i-1:i+1].isalpha():
            new_str2.append(str2[i-1:i+1])
    
    for i in new_str2:
        if i in copy1:
            copy1.remove(i)
            inter_li.append(i)
            
    for i in new_str2:
        if i not in copy2:
            sum_li.append(i)
        else:
            copy2.remove(i)
    
    if len(sum_li) == 0:
        return 65536
    else:
        return int(len(inter_li) /len(sum_li) * 65536)
   