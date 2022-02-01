# 전역 변수
price = 1000
def sale():
    
    # 전역변수 쓰기작업
    global price # 함수내 price를 전역변수로 지정해 줌
    # * 이 작업은 최대한 안하는 것이 좋음
    price = 500
    
sale()
print(price)