# 데이터를 표현하는 클래스 -> 데이터 클래스, 모델 클래스
class NameCard :
    def __init__(self, name, phone, email, address) :
        self.name = name
        self.phone = phone
        self.eamil = email
        self.address = address
        
    def __str__(self) :
        return f'<NmaeCard name : {self.name} phone : {self.phone} email : {self.email} address : {self.address}>' # overriding
    
    # represent
    def __repr__(self) -> str:
        return f'<NameCard name : {self.name}>'

def main():
    # card1 = NameCard('홍길동', '010-1111-1111', 'hong@naver.com', '서울시')
    # card2 = NameCard('고길동', '010-1221-1111', 'go@naver.com', '시흥시')
    # print(card1.name, card1.phone)
    # print(card1)
    # print(card2)

    # book = [card1, card2]
    # print(book)

    book = []
    for i in range(1,101):
        card = NameCard(f'홍길동{i:03}', f'010-1111-{i:04}', f'hong{i:05}@naver.com', '서울시')
        book.append(card)

    print(book)
main()
