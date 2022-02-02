# random 모듈
# 0 ~ 1 사이의 난수 리턴 (1은 미포함)
# .randint(begin, end) : begin ~ end 사이의 정수 난수를 리턴 (end도 포함)
# .randrange(begin, end) : begin ~ end 사이의 정수 난수를 리턴 (end도 미포함)
# .uniform(begin, end) : begin ~ end 사이의 실수 난수를 리턴 (end도 포함)

import random

def main():
    for i in range(5):
        print(random.random())
    print()
    
    for i in range(5):
        print(random.randint(1,10))
    print()

    for i in range(5):
        print(random.randrange(1,10))
    print()
    
    for i in range(5):
        print(random.uniform(1,10))
    print()
     
    
    # .choice -> random으로 골라줌
    food = ["짜장면", "짬뽕", "탕수육", "군만두"] 
    print(random.choice(food))
    print()
    
    #.shuffle -> random하게 섞음
    
    print(food)
    random.shuffle(food)
    print(food)
    print()
    
    # .sample -> choice 개념인데 뽑을 갯수를 지정가능함
    print(random.sample(food,2))
main()
    