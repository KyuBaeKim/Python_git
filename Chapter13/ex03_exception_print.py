import traceback
# 에러가 난 경로를 알려준다.
mode = 'DEV' #PRODUCT

# 변수 하나를 지정 한 뒤 현재 상황이 개발 모드인지
# 아니면 실행 모드인지 지정해 준 뒤 시스템 상태를 확인한다.

def covert(value):
    return int(value)

def work():
    str = "89점"
    # score = int(str)
    score = covert(str)
    print(score)

def main():
    try:
        work()
    except Exception as e :
        print(e)
        if mode == 'DEV' :
            traceback.print_exc() # traceback을 통해 에러가 난 위치를 알려준다.
    print("작업완료")
main()