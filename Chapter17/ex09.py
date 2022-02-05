# Context Manager 객체
#  __enter__(self): with로 객체를 만들어서 as에 배정할 때 호출,( 리턴값이 as 변수에 대입
#  __Exit__(self, type, value, tb): with 코드 블럭을 벗어날때 호출
# 클린업 작업할때 많이 씀 --> 라즈베리 파이 할 때 다룰 객체


# with open(파일명, 모드) as f:  
#     pass

class Myobject:
    def __init__(self) -> None:
        pass
    
    def __enter__(self):
        print('with 코드 블럭에 진입합니다.')
        print('초기화 작업 수행')
        return self
        
    def __exit__(self, type, value, tb):
        print('with 코드 블럭을 벗어납니다')
        print('클린업 정리 작업 수행')
        
        
def main():
    with Myobject() as obj: # enter에서 return 되는 객체가 obj 배정
        input('마치려면 enter')
        
    print('작업 완료')
main()