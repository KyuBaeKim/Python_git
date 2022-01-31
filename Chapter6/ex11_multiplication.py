# 구구단 출력
#
# 출력
# 3 x 1 = 3
# ...
# 3 x 9 = 27

dan = 0
for dan in range(2, 10):
    print(dan, '단')
    for n in range(1, 10):
        result = dan * n
        print(dan, "x", n, "=", result)
    print()