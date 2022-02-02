# time 모듈
# 1970년 1월 1일 자정을 기준으로 경과한 시간을 초 단위로 표현 
# --> 에폭(Epoch) 시간 또는 유닉스 시간
import time
print(time.time())
print("-"*30)

t = time.time()
print(time.ctime(t))
# 사람이 볼 수 있는 형태로 시간을 출력해라

print("-"*30)

t = time.time()
print(time.localtime(t))
# 현재 컴퓨터의 로컬 타임을 호출

print("-"*30)
now = time.localtime()
print(f"{now.tm_year}년 {now.tm_mon}월 {now.tm_mday}일")
print(f"{now.tm_hour}:{now.tm_min}:{now.tm_sec}")

# import datetime
from datetime import datetime
now = datetime.now()
print(f"{now.year}년 {now.month}월 {now.day}일")
print(f"{now.hour}:{now.minute}:{now.second}")
