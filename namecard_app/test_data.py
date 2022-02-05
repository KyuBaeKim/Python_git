from namecard import NameCardBook
import random


def main():
    book = NameCardBook()

# 200개 데이터를 구성해 book.dat로 저장
    book.book = []
    addresses = ['서울시', '부산시', '대구시' , '광주시', '인천시', '성남시' ]
    for ix in range(1, 101):
        book.add(f'홍길동{ix:03}', f'010-1111-{ix:04}', f'hong{ix:03}@gmail.com', f'{random.choice(addresses)}')
    
    print(book.book)
    book.save('book.dat')
    
    # book.book을 orderby 변수의 값을 기준으로 정렬하세요.
    orderby = 'address'
    # 주소부분으로 정렬
    book.book.sort(key = lambda card : card[orderby])
    
    orderby = 'name'
    # 이름부분으로 정렬
    book.book.sort(key = lambda card : card[orderby])
    
    print(book.book)
main()