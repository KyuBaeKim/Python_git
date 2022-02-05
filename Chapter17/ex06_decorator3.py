def inner():
    print("결과를 출력합니다.")

    
def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-"*20)
    return wrapper

# 1) 장식자 함수는 내부 함수 리턴
# 2) 원래 함수로 다시 이름 저장
inner = outer(inner) # <- 데코레이션 지시
inner()
