# 두 가지 이상의 복합 정보를 이용할 경우 모두 클래스로 이용한다.
# 사용이유 : 재사용성 떄문에

from sympy import re


class Human:
    def __init__(self, name, age) -> None: # 2. self 인스턴스에 대한 참조변수를 파이썬이 지정해줌
        self.name = name
        self.age = age 
        
    def intro(self): # 4. kim이 intro의 self에 전달
        print(str(self.age) + "살" + self.name + "입니다.") # 6. 출력 실행
        
    def __str__(self) -> str:
        return f'<Human name = {self.name}, age={self.age}>'

def main():
    kim = Human("김규배", 26) # 1. 인스턴스 생성
    kim.intro() # 4. kim.intro() 함수 실행
    
    lee = Human("이승우", 45)
    lee.intro()
    
    print(kim.name, kim.age) 
    print(lee.name, lee.age)

    print(kim)
    print(lee)