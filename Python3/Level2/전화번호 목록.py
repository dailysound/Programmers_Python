def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                return False
                break
    return True
    
# import heapq

# def solution(phone_book):
#     if len(phone_book) == 1:
#         return True
    
#     heapq.heapify(phone_book) # 이미 원소가 들어있는 리스트를 힙으로 만들기
#     p_num = heapq.heappop(phone_book) # 제일 작은 값 빼서 p_num에 저장하기
#     answer = True
#     while phone_book:
#         i = len(p_num)
#         if p_num == phone_book[0][:i]: # 여기서의 phone_book[0]은 p_num에 가장 작은 값을 넣고 난 후 그 다음으로 작았던 값 (== 초기 리스트의 2번째 값)
#             return False
#         p_num = heapq.heappop(phone_book)
#     return answer