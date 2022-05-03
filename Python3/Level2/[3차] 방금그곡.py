def Replace(music):
    if 'A#' in music:
        music = music.replace('A#','a')
    if 'C#' in music:
        music = music.replace('C#','c')
    if 'D#' in music:
        music = music.replace('D#','d')
    if 'F#' in music:
        music = music.replace('F#','f')
    if 'G#' in music:
        music = music.replace('G#','g')
    return music

def solution(m, musicinfos):
    m = Replace(m) # 네오가 기억한 멜로디 중 #이 붙은 음이 있을 수 있기 때문에 치환 작업 해줌
    answer = []
    turn = 0 # 먼저 입력된 음악 판단용

    for info in musicinfos:
        turn +=1
        music = info.split(',') # 곡별로 나눔
        # ['12:00', '12:14', 'HELLO', 'CDEFGAB'] 이런식으로 들어가게된다.
        
        music_title = music[2]
        start_time = music[0].split(':') # 시작시간
        end_time = music[1].split(':') # 종료시간
        
        play_time = (int(end_time[0])*60 + int(end_time[1])) - (int(start_time[0])*60 + int(start_time[1])) # 곡 재생 시간
        
        # #이 붙은 음 치환하기
        replaced = Replace(music[3])
        # ABCDEF -> ABCDEF / CC#B -> CcB
        
        # 음악 재생시간 동안의 음
        m_play = (replaced*play_time)[:play_time] 
        # 재생시간만큼 음을 반복한 후 재생시간만큼 자르기
        # 재생시간이 5이고 음이 ABC이면 ABCABCABCABCABC -> ABCAB 로 구해짐
   
        if m in m_play:
            answer.append([play_time, turn, music_title])
    
    # answer에 아무것도 없으면 "None"
    if not answer:
        return "(None)"
    # 결과의 길이가 1이면 바로 제목 반환
    elif len(answer) == 1:
        return answer[0][2]
    # 결과의 길이가 2이상이면 재생된 시간이 긴 음악, 먼저 입력된 음악 순으로 정렬 후 제목 반환
    else:
        answer = sorted(answer, key= lambda x:(-x[0],x[1]))
        return answer[0][2]
                
            