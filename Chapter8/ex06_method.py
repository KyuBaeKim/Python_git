# 메서드


def main():
    s = "python programing"
    # len() --> 길이 출력 <함수>
    print(len(s))
    
    # .find(str) --> str(문자열)을 찾아 인덱스를 반환 , 없으면 -1 
    print(s.find('o'))
    
    # 뒤에서 str 문자열을 찾아 인데스 봔한, 없으면 -1 반환
    print(s.rfind('o'))
    
    # .index(str) <- find()와 동일, 없으면 예외 발생
    # try exception 이용해서 응용할 수 있다.
    print(s.index('r'))
    
    # str 문자열이 몇번 등장하는지 리턴
    print(s.count('n'))

main()