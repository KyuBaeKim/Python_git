# 명함 관리 프로그램
# 관리할 명함 정보 : 이름, 전화번호, email, 주소 ==> 연락처(주소록) 관리

# 시작할때 고려사항
# 1. 데이터를 어떻게 표현하고 관리할것인가?
#    한 사람의 정보 --> 사전
#    여러명의 정보 --> 리스트
# 2. 어떤 기능을 제공할 것인가?
#    목록(검색), 추가, 수정, 삭제
#    CRUD 연산(Create, Read, Update, Delete)
#    즐겨찾기, 그룹핑, 파일저장, 파일 로딩, ... 종료
import sys
import random 
from file_util import save_json, load_json
books = [] 
FILE_NAME = "books.json" # 대문자는 상수처럼 쓰겠다는 의미

def create_card(name, phone, email, address): 
    return {
        "name" : name,
        "phone" : phone,
        "email" : email,
        "address" : address
    }

def init(): # 초기화 함수 
    # for ix in range(1, 101):
    #     card = create_card(f'홍길동{ix:03}', f'010-1111-{ix:04}', f'hong{ix:05}@gmail.com', '서울시')
    #     books.append(card)
    # random.shuffle(books) # 이름으로 정렬하세요.
    # books.sort(key = lambda card : card["name"]) # 람다함수로 key에 지정
    # # sort는 내림차순으로 정렬
    
    global books
    books = load_json(FILE_NAME)

def print_menu():
    print()
    print('='*35)
    print('목록  검색  추가  삭제  수정  종료')
    print('='*35)

def print_card_list(card_list):
    print('-'*40)
    for ix, card in enumerate(card_list):
        print(f'{ix:03}  {card["name"]}  {card["phone"]} ...')
    print('-'*40)
    print(f'총: {len(books)}명')    
    print()
    

# 목록 메뉴 실행 함수    
def print_list():
    print("목록보기")
    # 인덱스도 같이 출력되게 합니다.
    # 0 홍길동 001 010-1111-0001
    print_card_list(books)
   
  

# 검색 메뉴 실행 함수
def search():
    keyword = input("검색 이름: ")
    # 검색하고, 출력
    
    #    result = []
    #    for card in books :
    #        if keyword in card["name"] :
    #            result.append(card)
    
    # 람다함수를 이용한 filter  
    result = list(filter(lambda card: keyword in card["name"] , books))
    
    # result 리스트 출력
    print_card_list(result)
    
# 종료 메뉴 실행 함수
def exit():
    answer = input("종료 하시겠습니까?(Y/N) : ")
    if (answer == 'y') or (answer == 'Y') : 
    # answer.lower() == 'y'
    # answer in ['y', 'Y']
        save_json(FILE_NAME, books)
        sys.exit(0)
        pass 

# 추가 메뉴 실행 함수
def add_card():
    name = input("이름: ")
    phone = input("전화번호: ")
    email = input("email: ")
    address = input("주소: ")
    
    
    card = create_card(name, phone, email, address)
    books.append(card)
    books.sort(key = lambda card : card["name"])   

def find(name):
    # 찾았으면 인덱스 리턴
    # 없으면 -1 리턴
    for ix, card in enumerate(books):
        if card['name'] == name :
            return ix
    
    return -1 # for문을 다 돌았다는 의미 ---> 더 탐색할 데이터가 없다.
    # 중간에 return ix로 린터하기 때문에 굳이 else를 추가 할 필요 x
     
     
def delete_card():
    name = input("삭제할 이름 : ")
    ix = find(name)
    if ix != -1 :
        books.pop(ix)
        print(f'{name} 항목을 삭제했습니다.' )
    else :
        print(f'{name} 항목이 없습니다.' )
     # 특정 인덱스에 데이터 삭제
    # del books[ix]

def update_card():
    # 이름입력 받기
    # 인덱스 찾기
    # 있으면 ... 업데이트
    #   기존 데이터 보여줌 이름(홍길동001):
    #   변경이 없으면 그냥 엔터
    #   변경할거면 입력 해서 수정처리
    # 없으면... 없음 출력
    name = input("수정할 이름: ")
    ix = find(name)
    if ix != -1:
       card = books[ix]
       name = input(f'이름({card["name"]}):')
       if name != '': # 입력 없이 엔터 친 경우
           card['name'] = name
       
       phone = input(f'전화번호({card["phone"]}):')
       if phone != '': # 입력 없이 엔터 친 경우
           card['phone'] = phone
       
       email = input(f'이메일({card["email"]}):')
       if email != '': # 입력 없이 엔터 친 경우
           card['email'] = email 
       
       address = input(f'주소({card["address"]}):')
       if address != '': # 입력 없이 엔터 친 경우
           card['address'] = address  
        
       print(f'{name} 항목을 수정했습니다.')
    else :
        print(f'{name} 항목이 없습니다.' )
    
    
    
def main():
    
    init()
    
    while True :
        
        # 메뉴 출력
        print_menu()
        
        # 사용자가 메뉴를 입력
        menu_item = input('선택> ')
        
        # 입력한 메뉴를 실행/결과 출력
        if menu_item == '목록' : 
            print_list()
        elif menu_item == '검색' : 
            search()
        elif menu_item == '추가' : 
            add_card()
        elif menu_item == '삭제' :
            delete_card()
        elif menu_item == '수정' :
            update_card()    
        elif menu_item == '종료' : 
            exit()
        else :
            print('잘못 입력한 메뉴입니다.')
            
   
main()
