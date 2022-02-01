# def calcscore (name, *score, **option) :

def calcscore (name, *args, **kwargs) : # 관례로 쓰인다.
    print(name)
    print(args)
    print(kwargs)
    total = 0
    for s in args :
        total += s
        
    print("총점 :", total)
    if kwargs.get('avg'): # 'avg' 키가 없으면 디폴트 값이 된다.
        print("평균 :", total/len(args))

def main():
    # calcscore("홍길동", 88, 99, 77, avg = True)
    # calcscore("고길동", 99, 88, 95, 85, avg = False)

    hong_score = [88, 99, 7]
    go_score = [99, 88, 95, 85]
    option = {
        'avg' : True,
        'total' : True,
    }
    calcscore('홍길동', *hong_score, avg=True)
    calcscore('고길동', *go_score, **option)
    #  *go_score *hong_score 리스트를 펼쳐서서 가변인수로 전달
    # **option 사전을 펼쳐서 키워드 가변인수로 전달.
main()
        