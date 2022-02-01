# 함수 정의
def calcrange(begin, end):
    total = 0
    for num in range(begin, end + 1) :
        total += num
    return total

# 함수 호출 --> 함수르 호출할 때의 매개변수의 갯수와 형태를 일치 시켜줘야 한다.
# 위치가 안맞거나 비어 있을경우 positional argument: 'end' 이런식의 에러가 뜬다.
print("3 ~ 7의 합 =", calcrange(3, 7))