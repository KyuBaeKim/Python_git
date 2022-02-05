# 스택(stack)
#
# 클래스 설계 : 
# 1. 다루는 데이터가 무엇인가? (데이터 타입?, 단일/여러개냐...)
# --> list 관리
# 2. 그 데이터를 어떻게 처리(운영)하는가 ? 
# --> 저장, 삭제(꺼내기), 꺼내지 않고 top만 읽기, 비었는지 검사
#
# 이 과정을 추상화(Abstract)한다라고 한다. --> 클래스 설계

class Stack:
    def __init__(self) :
        self.data = []
        
    def push(self, value) :
        self.data.append(value)

    def pop(self):
        assert len(self.data) > 0, '스택이 비었습니다.'
        
        return self.data.pop()
    
    def read_top(self):
        assert len(self.data) > 0,  '스택이 비었습니다.'
        top = self.data[-1]
        # top = len(self.data) -1 --> 다른 언어라면 이 식 사용
        return top
    def is_empty(self): # is로 시작하는 함수는 return이 bool이다.
        return len(self.data) == 0
    
def main():
    stack = Stack()
    
    # stack = Stack -> 클래스 자체를 참조 하겠다.
    stack.push(10)
    stack.push("홍길동")
    stack.push(100)

    print(stack.read_top())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
main()
