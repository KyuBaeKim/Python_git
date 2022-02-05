# 클래스 메서드
class Car:
    count = 0
    
    def __init__(self, name) -> None:
        self.name = name
        Car.count += 1
        
        
    @classmethod
    def outcount(cls):
        print(cls.count)

pride = Car("프라이드")
korando = Car("콜란도")
Car.outcount()