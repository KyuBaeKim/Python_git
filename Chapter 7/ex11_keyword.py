# 키워드 인수
# 이름을 정의 하여 인수를 대입할 수 있도록한다.


# 위치 기반과 키워드 인수를 혼용할 때 주의사항
# 위치 기반 인수를 먼저쓰고, 뒤에 키워드 인수를 사용
# print("3 ~ 5", calcstep(Step = 1, end = 5, 3))-->에러가 난다.

def calcsum(begin, end, step) :
    total = 0
    for num in range(begin, end + 1, step):
        total += num   
    return total

def main() :
    print(" 3 ~ 5", calcsum(3, 5, 1))
    
    print(" 3 ~ 5", calcsum(begin = 3, end = 5,  step = 1))
    print(" 3 ~ 5", calcsum(step = 1, end = 5, begin = 3))
    
    print(" 3 ~ 5", calcsum(3, 5, step = 1))
    print(" 3 ~ 5", calcsum(3, step = 5, end = 1))
main()