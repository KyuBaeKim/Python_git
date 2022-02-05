# 연산자 메소드
# __eq__

class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        

    def __eq__(self, other) : # 연산자가 override = 연산을 재정의 한다.
        return self.name == other.name and self.age == other.age
        
def main():
    kim = Human("김상형", 29)
    sang = Human("김상형", 29)
    moon = Human("문종민", 44)
    
    print(kim == sang) 
    print(kim == moon)
main()