# 큐(Queue) : First In First OUT
# 
# 클래스 설계 : 
# 1. 다루는 데이터가 무엇인가? (데이터 타입?, 단일/여러개냐...)
# --> list 관리
# 2. 그 데이터를 어떻게 처리(운영)하는가 ? 
# --> 저장, 삭제(꺼내기), 꺼내지 않고 top만 읽기, 비었는지 검사
#

# 클래스 설계 원칙: SRP : 단일 책임의 원칙 --> QUEUE 설계인 경우 QUEUE만 설계해야 한다.
class Queue:
    def __init__(self) :
        self.data = []
        
    def put(self, value) :
        self.data.append(value) 
        
    def get(self) :
        assert not self.is_empty(), '큐가 비었습니다.'
        return self.data.pop(0)
    
    def read_front(self):
        assert not self.is_empty(), '큐가 비었습니다.'

        # len(self.data) > 0 
        # top = len(self.data) - 1 --> 다른 언어라면 이 식 사용
        return self.data[0]
    
    def is_empty(self): # is로 시작하는 함수는 return이 bool이다.
        return len(self.data) == 0
    
def main():
    queue = Queue()
    
    queue.put(10)
    queue.put("홍길동")
    queue.put(110)

    print(queue.get())
    print(queue.get())
    print(queue.get())
    
    
    if(not queue.is_empty()):
        print(queue.get())

main()