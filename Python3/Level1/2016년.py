import datetime
import time

def solution(a, b):
    c = 2016
    answer = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    return answer[datetime.date(c,a,b).weekday()]