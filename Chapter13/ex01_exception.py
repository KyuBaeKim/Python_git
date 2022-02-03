# 예외 처리
# 예외 종류

str = "89점"
try: # 예외가 발생할 것 같은 곳에 예의 주시해라
    score = int(str)
    print(score)
except: # 예외가 발생 하면 실행해라
    print("예외가 발생했습니다.")

print("작업완료")

print()
while True:
    # while문을 통해 예외가 생기더라도 성공 케이스가 나올떄까지 로직이 돌아간다.
    str = input("점수를 입력하세요 : ")
    try: # 성공 케이스만 신경쓰면된다.
        score = int(str)
        print("입력한 점수 : ", score)
        break
    except:
        print("점수 형식이 잘못되었습니다.")
print("작업완료")