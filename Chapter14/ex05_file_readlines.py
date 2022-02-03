# .Readlines : 전체 라인 리스트 각 라인 끝에 개행 문자(\n)가 들어있음
def main():
    f = open("live.txt", "rt", encoding="utf-8")
    rows = f.readlines()
    print(rows)
    for row in rows:
        print(row, end="")
    f.close()
main()