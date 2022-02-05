# 클래스
# 정보와 정보의 조작 함수(메서드)를 묶어서 관리
# 데이터 : 변수로 관리
# 기능 : 함수로 관리
# 데이터와 기능을 묶어서 관리 하는 것이 클래스이다.

# class 키워드로 정의 -> 사용하기 위해서는 instance를 생성한 후 사용
# instance : 사례 


# class Bank Account: (이와 같이 첫문자를 대문자로 쓴다 --> Pascal case라 칭함)

# def __init__(self, 변수) : python이 내부적으로 사용하는 함수, 변수
# 매직 매서드 : __init__ --> 파이썬의 내부적으로 쓰이는 함수

# 이름만 봐도 알아야 한다.
# Sound(song_path) --> Sound 클래스의 인스턴스를 생성 , __init__(self, song_path) 이 메서드를 가진다.

from re import A
from sklearn.metrics import balanced_accuracy_score


class Account :    # Account class 정의
    
    # self -> 인스턴스에 대한 참조변수 -> 자동으로 파이썬이 넣어줌
    # balance에 8000이 전달됨
    def __init__(self, balance) -> None:
        # 자동호출 메서드 __init__()
        # __init__은 클래스 명으로 함수 호출이 사용되었을 때 인스턴스가 생성되게 만든다.
        self.balance = balance
        # self -> 멤범변수(attribute)
        # balance : 잔액 -> 오른쪽 balance는 지역변수
    def deposit(self, money):
        self.balance += money
            
    def inquire(self):
        print(f"잔액은 {self.balance}원 입니다.")

def main():
    # 첫 번째 인스턴스
    account = Account(8000) # Account의 인스턴스 생성
    account.deposit(1000)
    account.inquire()
    
    # 두 번쨰 인스턴스
    shinhan = Account(8000)
    shinhan.deposit(1000)
    shinhan.inquire()
    
    # 세 번째 인스턴스
    nonghyup = Account(120000)
    nonghyup.inquire()
main()