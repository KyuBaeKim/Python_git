# 정적 메서드
# 인스턴스가 없기 때문에 - > 밑과 같은 예를 보면 staticmethod는 self.name에 접근할수 없다
class Car :
    @staticmethod
    def hello():
        print("오늘도 안전 운행 합시다.")
        
    count = 0
    
    def __init__(self, name) -> None:
        self.name = name
        Car.count += 1
        
    @classmethod
    def outcount(cls):
        print(cls.count)

Car.hello()