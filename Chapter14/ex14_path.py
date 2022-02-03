# path(경로) : 파일의 위치를 기술하는 문자열

def main():
     # 디렉토리 구분자
    # 윈도우: \ (\를 escape로 취급하기때문에 \\ 이거나 /(슬래시)로 구분자를 지정해준다.)
    # mac, linux
    # live.txt --> 현재 디렉토리에 있다.
    try : 
        f = open("c:/temp/abc/test2.txt", "rt", encoding="utf-8")   
        text = f.read()
        
        print(text)
    except FileNotFoundError :
        print("파일이 없습니다.")
    finally:
        f.close()
        
main()