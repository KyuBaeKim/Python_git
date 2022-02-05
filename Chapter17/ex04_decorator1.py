# 일급시민

# 대입연산자로 작용 했을 떄
def add(a, b):
    print(a+b)
plus = add
plus(1, 2)

# 매개변수로 작용 했을 떄
def calc(op, a, b):
    op(a, b)

def add(a, b):
    print(a + b)

def multi(a, b):
    print(a * b)

calc(add, 1, 2)
calc(multi, 3, 4)