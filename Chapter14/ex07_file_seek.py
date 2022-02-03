# seek(위치, 기준) --> 위치 = byte단위 
# 기준 0 : 파일의 처음 위치
#      1 : 현지 위치
#      2 : 파일의 끝 위피
def main():
    f = open("live.txt", "rt", encoding="utf-8")
    f.seek(12, 0) (12, 0) # 12 바이트가 문자 중간 위치에 있으므로
    text = f.read() # 예외 발생
    f.close()
    print(text)
main()