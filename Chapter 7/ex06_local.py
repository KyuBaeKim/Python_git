# 지역변수와 전역변수 구분
#def kim() 안의 print는 def kim()안의 지역변수(temp)부터 읽는다.
temp = '이병장의 전역변수' # 전역변수
def kim():
    temp = "김병장의 지역변수" # 지역변수
    print(temp)
kim()
print(temp)