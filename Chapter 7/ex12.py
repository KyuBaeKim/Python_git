# 키워드 가변 인수
def calcstep(**args):
    print(type(args))
    print(args)
    begin = args['begin']
    end = args['end']
    # step = args['step']
    step = args.get('step', 1)# 디폴트 값을 만들어 주려면 get인자를 사용
    
    total = 0
    for num in range(begin, end + 1, step) :
        total += num
    return total

def main():
    print("3 ~ 5 = ", calcstep(begin = 3, end = 5, step = 1))
    print("3 ~ 5 =", calcstep(step = 1, end = 5, begin = 3))
    print("3 ~ 5 =", calcstep(step = 1, end = 5, begin = 3, test= 1000))
    print("3 ~ 5 =", calcstep(step = 1, end = 5, begin = 3, test= 1000, test1 = 200000))
    print("3 ~ 5 =", calcstep( end = 5, begin = 3))
main()