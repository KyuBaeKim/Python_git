import time

def inner():
    print("결과를 출력합니다.")

def outer(func):
    print("-"*20)
    func()
    print("-"*20)

def elapse(func): # 함수의 실행 시간 측정 및 시간 출력 함수
    start = time.time()
    func()
    end = time.time()
    print(end-start)

def hello():
    print("안녕하세요")
    

def main():
    outer(inner)
    outer(hello)

    elapse(hello)
    elapse(inner)
main()