# 인수의 기본값
# default value

def calcstep(begin, end = 1, step = 1): #항상 뒤에서 부터 배정을 해야한다.
    total = 0
    for num in range(begin, end + 1, step):
        total += num
    return total

print("1 ~ 10 = ", calcstep(1, 10, 2))
print("2 ~ 10 = ", calcstep(2, 10, 2))
print("1 ~ 100 = ",calcstep(1, 100))