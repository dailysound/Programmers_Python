import itertools
def solution(word):
    list1 = ['A','E','I','O','U']
    list2 = list(map(list, itertools.product('AEIOU',repeat=2)))
    list3 = list(map(list, itertools.product('AEIOU',repeat=3)))
    list4 = list(map(list, itertools.product('AEIOU',repeat=4)))
    list5 = list(map(list, itertools.product('AEIOU',repeat=5)))
    
    word_dict = list1 +list2 +list3 +list4+list5
    
    for i in range(len(word_dict)):
        word_dict[i] = ''.join(word_dict[i])
    
    word_dict.sort()
    
    return word_dict.index(word)+1