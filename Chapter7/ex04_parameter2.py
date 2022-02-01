def intsum(*ints): # *ints ---> 가변인수 (튜플)
    print(type(ints)) #  *ints의 타입이 튜플이다.
    print(ints) # 가변인수 : 여러 인수가 들어갈 수 있다.
    total = 0
    for num in ints : # 튜플도 리스트 처럼 for문 사용가능.
        total += num
    return total

print(intsum(1, 2, 3))
print(intsum(5, 7, 9, 11, 13))
print(intsum(8, 9, 6, 2, 9, 7, 5, 8))