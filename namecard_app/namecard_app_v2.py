#  <NAME module>
#  NameCard: 데이터 클래스(모델 클래스)
#  name, phone, email, address
#  __repe__(), __str()__정의
#  NameCardBook: 모델 컬렉션 클래스
#  데이터 : 앱타이틀, NameCardBook, 파일명
#  기능: 
from namecard import NameCardBook
from baseapp import Application

class NameCardBookApp(Application):
    def __init__(self) -> None:
        super().__init__("명함 관리앱")
        self.book = NameCardBook()
        self.FILE_PATH = 'book.dat'
    
    
    def init(self):
        super().init() # 메뉴 구성
        # book.dat 로딩
        self.book.load(self.FILE_PATH)
        # print(self.book.book)
    
    def print_card_list(self, card_list, start = 0):
        
        print('-'*40)
        for ix, card in enumerate(card_list, start):
            print(f'{ix:3}  {card["name"]}  {card["phone"]} ')
        print('-'*40)
    
    def print_list(self):
        while True :
            # 페이지 단위로 출력
            
            page_num = int(input('페이지번호: '))
            
            if page_num == -1: # -1 or 0
                break # or return 
            # 해당 페이지를 출력
            page_obj = self.book.get_page(page_num)
            self.print_card_list(page_obj.page, page_obj.start)
            print(f'[{page_num}/{page_obj.total_page}] 총{page_obj.total_count}건')
        
    
    def add(self):
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        self.book.add(name, phone, email, address)
    
    def get_field(self, card, key, title):
        value = input(f'{title}:({card[key]}):')
        if value == '': # 입력 없이 엔터 친 경우
           # card[key] = value <-- 가능하지만 비권장
           value == card[key]
        return value           
       
        
    def update(self):
        name = input('수정할 이름: ')
        # name으로 검색해서 card의 참조 취득
        ix = self.book.find(name)
        if ix != -1:
            card = self.book.get(ix)
            # card = self.book.book[ix] ---> 기능은 하나 비권장
            name = self.get_field(card, 'name', '이름')
            phone = self.get_field(card, 'phone', '전화번호')
            email = self.get_field(card, 'email', 'email')
            address = self.get_field(card, 'address', '주소')
            self.book.update(ix, name, phone, email, address)
                
    
    def search(self):
        name = input("검색 이름: ")
        result = self.book.search(name)
        self.print_card_list(result)
        print(f'총 {len(result)}건')
    
    def remove(self):
        name = input('삭제할 이름:')
        ix = ix = self.book.find(name)
        if ix != -1:
            self.book.remove(ix)
            print(f'{name}을/를 삭제했습니다.')
        else:
            print(f'{name}은/는 존재하지 않습니다.')
            
            
    def exit(self):
        super().exit(lambda : self.book.save(self.FILE_PATH))
        
    
    
   

        
    def create_menu(self):
        self.menu.add_menu('목록', self.print_list) 
        self.menu.add_menu('추가', self.add)  
        self.menu.add_menu('수정', self.update)     
        self.menu.add_menu('검색', self.search)  
        self.menu.add_menu('삭제', self.remove)  
        self.menu.add_menu('종료', self.exit)
        
def main():
    app = NameCardBookApp()
    app.run()
main()    
   