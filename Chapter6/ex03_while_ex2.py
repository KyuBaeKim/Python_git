# 151 ~ 300의 홀수의 합
num = 151
total = 0

while num <= 300:
    total += num
    num += 2
print("total = ", total)

# 입력
# 시작값 : 20
# 종료값 : 40

# 출력 
# 20 ~ 40까지 합 : xxxx
# 한 번 초기화 되서 바뀌지 않는 값은 대문자로 성정하는 것이 좋다.

START = int(input("시작값 = "))
END =  int(input("끝값 = "))
total = 0
num = START

while num <= END :
    total += num
    num += 1
print(START, '~', END, "까지의 합 : ", total)
