# 1 ~ 100까지 합 계산
# 총 합 = total 합 할 변수 = num
num = 1
total = 0
while num <= 100:
    total += num
    num += 1
print("total =", total)

# 이 소스 구조를 활용해서
# 홀수의 합과 짝수의 합을 구해 출력하세요 .

num = 1
total1 = 0
total2 = 0
while num <= 100 :
    if num % 2 == 0:
        total1 += num
    else :
        total2 += num
    num += 1
print("짝수의 합 = ", total1)
print("홀수의 합 = ", total2)