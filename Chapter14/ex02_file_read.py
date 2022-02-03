# <읽기 작업> r
# 파일 x : Error --> 예외처리를 해주어야 한다. 
# 파일 o : 기존 파일 읽기

def main():
    try:
        f = open("live.txt", "rt", encoding="utf-8")
        # window는 cp949문자코드로 저장 --> 파이썬 문자코드 (UTF-8)로 인코딩 해줘야함
        text = f.read()
        print(text)
    except FileNotFoundError:
        print("파일이 없습니다.")
    finally:
        f.close()
main()
