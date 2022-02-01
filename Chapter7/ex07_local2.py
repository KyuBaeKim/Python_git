# 지역볌수
def kim():
    temp = "김병장의 지역변수"
    print(temp)

def lee():
    temp = 2**10
    kim()
    print(temp)

def park(a):
    temp = a * 2
    lee()
    print(temp)

park(6)