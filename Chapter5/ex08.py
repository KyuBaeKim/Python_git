# 숫자 하나를 입력하여 짝수와 홀수르 판별하시오.

num = int(input("숫자를 입력하세요 : "))

if (num%2) == 0 :  # 짝수
    print("짝수입니다")

else :
    print(num,'은/는 홀수입니다.', sep = "")