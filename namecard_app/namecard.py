# 필요한 클래스

#  <NAME module>
#  NameCard: 데이터 클래스(모델 클래스)
#  name, phone, email, address
#  __repe__(), __str()__정의
#  NameCardBook: 모델 컬렉션 클래스

#  <MAIN module>
#  Application: 운영 클래스

# class NameCard:
#     def __init__(self, name, phone, email, address) -> None:
#         self.name = name
#         self.phone = phone
#         self.email = email
#         self.address = address
        
#     def __repr__(self):
#         return f'NameCard(name={self.name})'
    
#     def __str__(self):
#         return f'NameCard(name={self.name}, phone={self.phone}, email={self.email}, address={self.address})'

from ctypes import addressof
from dataclasses import dataclass
import file_util 
from re import S
from turtle import st
import os
import random
import math
from paging import Paginator

@dataclass
class NameCard:
    name: str
    phone: str = '' # 디폴트 값을 비어있는 문자열로 출력한다.
    email: str = ''
    address: str = ''
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)
    

        
    
    
# json 모듈: 파이썬 표준 모듈만 지원 --> class를 지원 하지 않는다.
    
# NameCardBook 클래스 srp = 단일 책임의 원칙 
# NameCard 모델 클래스의 콜렉션 역할
# 데이터: NameCard 목록
# 기능: 추가, 수정, 삭제, 검색    (파일 관리) 로딩, 저장 --> CRUD

class NameCardBook:
    def __init__(self) -> None:
        self.book = []
    
    # 페이지 목록 추출    
    def get_page(self, page_num, count_per_page = 10):
        page_obj = Paginator(self.book, page_num, count_per_page)
        return page_obj
        
    def add(self, name, phone, email, address) :
        card = NameCard(name, phone, email, address)
        self.book.append(card)
        self.book.sort(key = lambda card : card.name) 
        
        
    def update(self, ix, name, phone, email, address):
         card = self.book[ix]
         card.name = name
         card.phone = phone
         card.email = email
         card.address = address
        
    
    def remove(self, ix): # delete 예약어가 많아서 충돌 가능성이 있다.
        # ix = self.find(name)
        
        if ix != -1 :
            self.book.pop(ix)
            
    
    def search(self, name): # 포함으로 검색해서, 리스트 리턴 
        result = list(filter(lambda card: name in card.name , self.book))
        return result 
    
    def find(self, name): # 완전일치 검색, 인덱스 리턴
        for ix, card in enumerate(self.book):
            if card.name == name :
                return ix
    
        return -1
    def get(self, ix) :
        return self.book[ix]
    
    def load(self, file_path):
        # 로드 할때 파일의 존재 여부를 검사 해야한다.
        if os.path.exists(file_path) : # 파일이 존재하는경우
            self.book = file_util.load(file_path)
            # print(self.book)
        else: # 초기에 파일이 없는경우 
            print(file_path,'파일 없음')
            self.book = []
        
    def save(self, file_path):
        file_util.save(file_path, self.book)
        
    
if __name__ == "__main__" : # 모듈 테스트
    card = NameCard('홍길동', '010-1111-1111', 'hong@naver.com', '서울시')
    print(card)
    print([card])
    
    book = NameCardBook()
    
    print()
    
    print("추가 테스트")
    book.add('홍길동1', '010-1111-0001', 'hong1@naver.com', '서울시')
    book.add('홍길동2', '010-1111-0002', 'hong2@naver.com', '서울시')
    book.add('홍길동3', '010-1111-0003', 'hong3@naver.com', '서울시')
    print(book.book)
    
    print("검색 테스트")
    result = book.search('길동')
    print(result)
    result = book.search('동1')
    print(result)
    
    print()
    
    print("find 검색 테스트")
    ix = book.find("홍길동2")
    print(ix)
    ix = book.find("홍길동3")
    print(ix)
    
    print()
    
    print("삭제 테스트")
    book.remove(0)
    print(book.book)
    
    print()
    
    # print("저장 테스트")
    # book.save('book.dat')
    
    # print("로드 테스트")
    # book.load('test.dat')
    # print(book.book)
    # book.load('book.dat')
    # print(book.book)
    
    # # 200개 데이터를 구성해 book.dat로 저장
    # book.book = []
    # addresses = ['서울시', '부산시', '대구시' , '광주시', '인천시', '성남시' ]
    # for ix in range(1, 201):
    #     book.add(f'홍길동{ix:03}', f'010-1111-{ix:04}', f'hong{ix:03}@gmail.com', f'{random.choice(addresses)}')
    # print(book.book)
    # book.save('book.dat')
    
    