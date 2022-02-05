import time

def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-"*20)
    return wrapper

# 데코레이터 함수(@elapse가 가능 하도록)정의
# -> 내부 함수를 정의해서 리턴

def elapse(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'{func.__name__} 함수 실행 시간: {end - start}')
    return wrapper

# 데코레이터 두 개 붙이는 것도 가능하다.
# inner = elapse(outer(inner))
@elapse
@outer
def inner():
    print("결과를 출력합니다.")

def main():
    inner()
main()