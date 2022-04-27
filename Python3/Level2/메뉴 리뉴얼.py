from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for cnt in course: 
        comb_li = [] # 메뉴 구성 개수대로 메뉴 조합한 것을 저장할 리스트
        for order in orders:
            comb_li += combinations(sorted(order),cnt) # 'AC'와 'CA'는 같은 구성이므로 정렬
        order_dict = Counter(comb_li) # 각 조합별 개수 저장
        
        if order_dict: # 값이 존재할 때
            max_count = max(list(order_dict.values())) # 조합별 개수 중 큰 것들 저장
            if max_count >= 2: # 2명 이상이 해당 조합을 주문했다면
                for key, value in order_dict.items(): # 각 조합, 횟수 반복
                    if order_dict[key] == max_count:
                        answer.append(''.join(key))
    return (sorted(answer)) # 오름차순 정렬
        
    