# 예외의 종류
# NameError
# ValueError --> 점수 형식이 벗어날 경우
# ZeroDivisionError
# IndexError --> 인덱스 에러가 일어날 경우
# TypeError

str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]

except ValueError:
    print("점수의 형식이 잘못되었습니다.")
except IndexError:
    print("첨자 범위를 벗어났습니다.")

print("작업완료")
print()

str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]

except (ValueError, IndexError):
    print("점수의 형식이나 첨자가 잘못되었습니다.")

print("작업완료")