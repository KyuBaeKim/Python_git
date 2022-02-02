from tkinter.font import names


def main() : 
    names = ['홍길동', '고길동', '둘리', '또치']

# names의 각 이름을 한 줄에 하나씩 출력하세요
# names의 각 이름을 '홍길동', '고길동', '둘리', '또치' 식으로 하나의 문자열로 만드세요.

    s = '\n'
    print(s.join(names))
    
    n = ','.join(names)
    print(n)
main()
    