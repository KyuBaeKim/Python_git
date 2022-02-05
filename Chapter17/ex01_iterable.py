# interable 객체
# 열거 가능 객체

nums = [11, 22, 33]

# for문의 내부 구조
# 클래스를 -> Iterable(순환) 하게 만들 수 있다.
it = iter(nums)
while True :
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)