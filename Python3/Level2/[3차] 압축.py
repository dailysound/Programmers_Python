# def solution(msg):
#     answer = []
#     dic ={chr(i+64):i for i in range(1, 27)} # 대문자와 색인 맞추기
#     new_index = 27 # 새로 저장할 색인 시작 번호
    
#     search = ''
#     i = 0
#     while i<len(msg):
#         search += msg[i] # 한글자씩 더하기
        
#         if search in dic: # dic에 존재하면 계속 진행
#             i+=1
#             continue
#         else: # dic에 없는 문자일 경우
#             dic[search] = new_index # dic에 색인과 함께 추가
#             new_index += 1 # 색인 번호 증가
#             s = search[:-1] # 마지막자리 전까지는 dic에 존재
#             answer.append(dic[s]) # 마지막 자리 전까지의 단어의 색인 추가
#             serach = ''
#     answer.append(dic[search]) # 마지막 문자의 색인 추가
    
#     print(answer)

def solution(msg):
    answer = []
    dic ={chr(i+64):i for i in range(1, 27)} # 대문자와 색인 맞추기
    
    new_index = 27 # 새롭게 추가될 문자의 색인 시작 번호
    search = ''
    i = 0
    j = 0
    
    while True:
        j+=1
        if not msg[i:i+j] in dic: # 한글자씩 늘려가면서 dic에 있는지 찾기
            #없다면
            dic[msg[i:i+j]] = new_index # dic의 맨 뒤에 추가
            answer.append(dic[msg[i:i+j-1]]) # 그 전의 글자 색인 추가
            i = i+j-1
            j = 0
            new_index+=1
        else:
            if i+j-1 == len(msg): # 모두 검사한 것
                answer.append(dic[msg[i:i+j-1]]) # 마지막 글자의 색인 추가
                break
                
    return answer
                
            

            