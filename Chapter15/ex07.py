# 상속 
# 코드를 재사용 하기위해서
# Human이 부모 클래스이지만 Human 위에 object라는 부모클래스가 있다
# __str__을 Human에서 지정해주지 않았지만 print(kim)을 해보면 object가 출력된다.
# 모든 클래스는 object 클래스의 자식이다.

class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def intro(self):
        print(str(self.age) + "살" + self.name + "입니다,")

    def eat(self):
        print("식사를 합니다.")

    def __str__(self) -> str:
        return f'Human(name={self.name}, age={self.age})'
        # -> overeide
        
class Student(Human): # 상속 표현
    def __init__(self, name, age, stunum) :
        super().__init__(name, age)
        # 부모 코드를 이용해서 초기화 해줘야 함
        self.stunum = stunum
        
    def intro(self): # 부모가 정의한 메서드로 재정의 해야한다. -> override
        super().intro()
        print("학번: "+ str(self.stunum))

    def study(self):
        print("하늘천 따지 검을 현 누를 황")


# 선생님 : Teacher
# 데이터는 : 이름, 나이
# 기능 : 소개하기, 식사하기 ,가르치기
class Teacher(Human):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        
    def teach(self):
        print("수업을 합니다.")

def main():
    kim = Human("김상형", 29)        
    kim.intro()
    kim.eat()
    
    
    print()
    
    
    lee = Student('이승우', 45 , 930011)
    lee.intro()
    lee.eat()
    lee.study()
    
    print()
    
    print(kim)
    print(lee)

main()