users = [
    {
     'name': '홍길동',
     'age': 20,
     '주소': '서울시'   
    },
    {
     'name': '고길동',
     'age': 40,
     '주소': '수원시'   
    },
    {
     'name': '둘리',
     'age': 9,
     '주소': '성남시'   
    }    
]

def main():
    for user in users:
        diclist = user.items()
        for a,b in diclist :
            print(f'{a} = {b}')
    print()
    for user in users:
        print(f"{user['name']}\t{user['age']}\t{user['주소']}")
main()