# a mode
# 기존에 파일이 존재하는 경우 파일의 끝에 내용을 추가
# w mode
# 기존에 파일이 존재하는 경우 내용을 모두 지우고 다시 작성

def main():
    f = open("live.txt", "at", encoding="utf-8")
    f.write("\n\n푸쉬킨 형님의 말씀")
    f.close()
main()