import re
def solution(files):
    # 숫자 기준으로 구분
    split = [re.split(r"([0-9]+)",file) for file in files]
    
    answer = sorted(split, key=lambda  x: (x[0].lower(), int(x[1])))
    
    answer = [''.join(i) for i in answer]

    return answer