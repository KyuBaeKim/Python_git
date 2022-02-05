#
# 온도 센서(온도계)
# 클래스명 : Temperature
# 데이터: 온도(value), 기록(온도, 측정시간), 위치, 측정가능 범위
# 기능: 측정하기, 범위 초과시 .. , 기록보여주기()
#

from datetime import datetime
import random
import time


class Temperature:
    def __init__(self, location, min_value, max_value) -> None:
        self.value = None
        self.records = []
        self.location = location
        self.min_value = min_value
        self.max_value = max_value
        
    # 측정하기
    
    def measure(self):
        
        # min_value, max_value 사이의 랜덤한 값으로 측정되게
        # 값은 소수점 둘째자리까지..
        self.value = round(random.uniform(self.min_value, self.max_value), 2)
        now = datetime.now()
        
        self.records.append((now, self.value))
        return now, self.value
    
# 히터
# 클래스 : Hitter
# 데이터 : 온도, 장소, 운영 기준 온도, 상태
# 기능 : 켜기, 끄기, 운영, 온도 설정  
class Hitter:
    def __init__(self, location) -> None:
        self.temp = Temperature(location, -5, 35)
        self.location = location
        self.criteria = 19
        self.status = False # 전원 상태 : 꺼짐(default)
        
    def turn_on(self):
        self.satus = True
        print(f'보일러가 켜졌습니다. 장소 : {self.location} 온도 : {self.temp.value}도')
        
    def turn_off(self):
        self.satus = False
        print(f'보일러가 꺼졌습니다. 장소 : {self.location} 온도 : {self.temp.value}도')
        
    def run(self):
        # 온도를 측정해서, 기준 온도 이하이면 보일러 켜기, 기준온도 이상이면 보일러 끄기
        now, temp = self.temp.measure()
        
        if(temp < self.criteria and self.status == False):
            self.turn_on()
            
        elif(temp >= self.criteria and self.status == True):
            self.turn_off()

        else:
            pass
        
    def set_criteria(self, temp):
        self.criteria = temp
def main():
    # 1초 간격으로 온도를 측정해서
    # 장소, 측정한 시간, 온도를 출력하세요.
    # room_temp =  Temperature('안방', -5, 35)
    # while True :
    #     time.sleep(1) # 1초간 대기
    #     now, value = room_temp.measure()
    #     print(f'장소 : {room_temp.location}  시간 : {now}  온도 : {value}')
    
    hitter = Hitter('안방')
    hitter.set_criteria(15)
    while True:
        time.sleep(1)
        hitter.run()
        
main()
            
            