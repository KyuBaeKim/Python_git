# 함수 안에 return이 있을 경우 값을 반환한 후 종료 되지만
# 함수 안에 yield가 있을 경우 값을 반환해도 함수가 종료되지 않는다.
def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index: index + 2]


solarterm = seqgen('입춘우수경칩춘분청명곡우입하소만망종하지소서대서')

# 함수내에서 yeild 예약어가 사용 된 경우
# 함수가 실행 되는게 아님.
# Generator 객체리르 만들어지게 됨

print(solarterm)
print(dir(solarterm))



for k in solarterm:
    print(k, end = ',')