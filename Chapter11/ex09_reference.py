# 복사본이라 a에 영향을 끼치지 않음
def modify(x):
    x = 1000
    print(f'x : {x}')

def main ():
    a = 10
    modify(a)
    print(f'a : {a}')
 # 복사본만 바꼈기 때문에 a = 10이 찍힌다.
main()    