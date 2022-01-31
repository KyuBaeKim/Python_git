# for문
# ranger(시작, 끝 [, 증가값 = 1])
# 끝은 범위에서 포함 되지 ㅇ낳는다
# 증가값을 지정하지 않으면 1씩 증가

from ast import Num
from socket import NI_MAXHOST


total = 0
for num in range(1, 101) :
    total += num
print("total =", total)

total = 0
for num in range(2, 101, 2) :
    total += num
print("total = ", total)

START = int(input("시작 값 ="))
END = int(input("끝 값 ="))
total = 0
for num in range(START , END + 1) :
    total += num
print(START, '~', END, '까지의 합 : ', total, sep = '')