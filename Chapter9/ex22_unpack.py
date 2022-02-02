# 튜플
# unpack : 컬렉션 안의 원소들에 네이밍 할 수 있다. ---> 튜플, 리스트 다 동작한다.

def main():
    names = "이순신", "김유신", "강감찬"
    lee, kim, kang = names #unpack
    print(lee)
    print(kim)
    print(kang)

    a, b = 12, 34
    print(a, b)
    
    a, b = b, a
    print(a, b) 
main()