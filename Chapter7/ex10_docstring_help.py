# docstring

def calcsum(n):
    """1 ~ n까지의 합계를 구해 리턴하는 함수"""
    total = 0
    for i in range(n + 1):
        total += i
    return total

help(calcsum)
print(calcsum(10))