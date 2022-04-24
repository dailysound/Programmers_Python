def solution(brown, yellow):
    answer = []

    for width in range(1, yellow+1):
        if yellow % width != 0: # 직사각형이 아닌 경우 제거
            continue

        height = yellow // width

        if width < height: # 가로가 세로보다 길거나 같아야 함
            continue
        
        brown_h = height + 2
        brown_w = width + 2
        n_browin = (brown_h * brown_w) - yellow

        if n_browin == brown:
            answer.append(brown_w)
            answer.append(brown_h)
            break
    return answer
