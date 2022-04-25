def solution(n, words):
    sword = [words[0]] # 말한 단어 추가할 리스트
    for i in range(1, len(words)):
        # if not sword: #말한 단어에 없으면 추가
        #     sword.append(words[i])
        # else:
        if words[i] in sword: # 말한 단어 또 말하면
            return [(i%n)+1,(i//n)+1]
        elif words[i-1][-1:] != words[i][:1]: # 단어의 앞글자가 앞 단어의 뒷글자와 다르면
            return [i%n+1,i//n+1]
        else:
            sword.append(words[i])
    return [0,0] #아무도 틀린 사람이 없으면