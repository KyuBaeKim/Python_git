# 논리 연산자

a = 3
b = 4
if a == 3 and b == 4 :  # a = 3 b = 4 이면 참
    print("참")

a = 3
b = 5

if a == 3 or b == 4 :  # a = 3  이거나 b = 4
    print("참")

a = 3
if a > 1 and a < 10 : # <---- 1 < a < 10
    print("참")
if 1 < a < 10 : # 파이썬만 이 형식이 지원됨
    print("참")