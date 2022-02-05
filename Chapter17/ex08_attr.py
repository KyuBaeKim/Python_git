from dataclasses import dataclass

@dataclass
class NameCard:
    name : str
    phone : str = ''
    email : str = ''
    address : str = ''
    
    
    def print(self):
        print(self.name)

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)

def main():
    card = NameCard('홍길동', '010-1111-1111')
    print(card)

    name = getattr(card, 'name')
    # getattr(card, 'name') = get atribute --> name = card.name 
    print(name) 
    
    setattr(card, 'email', 'hong@naver.com') # 값을 설정할떄
    # setattr(card, 'email', 'hong@naver.com') --> card.email = 'hong@naver.com
    print(card)
    
    func = getattr(card, 'print')
    func()
    
    key = 'name'
    value = getattr(card, key)
    print(value)
    print(key, card[key]) #__getitem__(self, key) 호출됨
    
    key = 'address'
    value = '서울시'
    setattr(card, key, value)
    card[key] = '수원시' #__setitem__(self, key, value) 호출됨
    print(card)
    
    
    
    
    
    
    card[key] = '서울시'
    # 사전에 쓰기 하라는 의미 이기 때문에 에러가 남
    # 하지만 __getitem__(self, key)
    
    
main()