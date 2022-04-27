import math
# 시간 분단위로 계산하기
def Minutes(time):
    h,m = map(int,time.split(':'))
    return h * 60 + m

def solution(fees, records):
    answer = []
    
    # 기본시간, 요금, 단위시간, 요금 저장
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    car_num_dict = dict()
    
    for record in records:
        # 공백을 기준으로 시간, 차번호, 상태 저장하기
        time, car_num, state = record.split()
        car_num = int(car_num) # 차번호 정수형으로 바꾸기
        
        if car_num in car_num_dict: # 차번호가 차번호 딕셔너리에 존재하면
            car_num_dict[car_num].append([Minutes(time),state]) # 시간, 상태를 리스트로 추가
        else:
            car_num_dict[car_num] = [[Minutes(time), state]] 
        
    flist = list(car_num_dict.items()) # 딕셔너리의 요소들을 리스트로 변환
    flist.sort(key=lambda x: x[0]) # 차번호 기준, 번호가 작은 순으로 정렬
    
    for f in flist: 
        T = 0
        for ff in f[1]: # [시간,상태]
            if ff[1] == "IN":
                T -= ff[0]
            else:
                T += ff[0]
        
        if f[1][-1][1] == "IN": # 제일 마지막 상태가 입차 상태일 경우
            T += Minutes("23:59") # 23:59분에 출차 된 것으로 간주
        
        if T <= basic_time: # 누적 주차 시간이 기본 시간 이하이면 기본 요금 청구
            answer.append(basic_fee)
        else:
            answer.append(basic_fee + (math.ceil((T-basic_time)/unit_time)*(unit_fee)))
            
    return answer