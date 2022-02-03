def main():
    try:
        f = open("live.txt", "rt", encoding="utf-8")
        # window는 cp949문자코드로 저장 --> 파이썬 문자코드 (UTF-8)로 인코딩 해줘야함
        text = f.read()
        lines = text.split('\n')
        for ix, line in enumerate(lines, 1):
            # enumerate를 통해 줄마다 순서를 나눈다.
            print(f'{ix}:{line}')
        print()
        print(text)
    except FileNotFoundError:
        print("파일이 없습니다.")
    finally:
        f.close()
main()