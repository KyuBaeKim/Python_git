# 함수를 매개변수로 넘기는 작업
from time_utill import get_elapse_time

def work1():
    for a in range(1000):
        print(a)

def work2():
    sum = 0
    for a in range(1, 100001):
        sum += a


def main():
    # 1에서 1000까지의 합을 구하는데 걸리는 시간을 출력하세요

    # 함수를 매개변수로 전달하는 것 ->  sort, map, filter
    elapse_time = get_elapse_time(work1)
    # 함수의 참조가 넘어간다.
    # elapse -> 흐르다.
    
    print(elapse_time)

    elapse_time = get_elapse_time(work2)
    print(elapse_time)
main()
