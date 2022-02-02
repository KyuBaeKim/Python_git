def main():
    names = ['홍길동', '고길동', '둘리', '또치']
    search_name = input("검색 이름 : ")

    # 검색 이름이 포함된 모든 이름을 출력하세요.
    for name in names :
        # if name == search_name: --> 전체가 일치 하는지 검사
        # if name.fine(search_name) > -1 :
        # ?를 != 바꿔 써도 사용 가능
        
        if name.find(search_name) > -1:
            print(name)
    
main()