# .Readline : 한 줄씩 읽는다.

def main():
    f = open("live.txt", "rt", encoding="utf-8")

    text = ""
    lines = 1
    while True:
        row = f.readline() # 파일의 끝까지 다읽으면 none을 return 한다.
        if not row: break # ~row가 true이면 break
        text += str(lines) + " : " + row
        lines += 1
    f.close()
    print(text)
main()