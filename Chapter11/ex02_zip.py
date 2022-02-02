# 컬렉션 관리 함수
# zip : 지퍼를 예로 생각하면된다.
# 시퀀스의 길이가 다른 경우 짧은 시퀀스의 길이에 맞춘다.
# zip(시퀀스1, 시퀀스2) -> [(값1, 값2),...]

def main():
    dates = ['월', '화', '수', '목', '금', '토', '일']
    food = ['갈비탕','순대국', '칼국수','삼겹살']

    menu = zip(dates, food)
    for d, f in menu:
        print(f"{d}요일 메뉴 : {f}")

    # zip을 이용해 사전 만들기
    menu_dic = dict(zip(dates, food))
    print(menu_dic)
main()