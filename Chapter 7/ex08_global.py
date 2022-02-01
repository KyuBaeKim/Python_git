# 전역변수

salerate = 0.9

def kim():
    print("오늘의 할인율 :", salerate)

def lee():
    price = 1000
    print("가격 : ",price*salerate)

kim()
salerate = 1.1
lee()

# 읽기 : 스택(지역변수 공간) --> 전역공간
# 쓰기 : 스택(없으면 생성)