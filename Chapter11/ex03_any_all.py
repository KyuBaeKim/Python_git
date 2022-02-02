# any(), all()
# any -> 시퀀스에 하나라도 있으면 True 리턴
# all -> 시퀀스에 모든 요소가 True이면 True 리턴

def main():
    adult = [True, False, True, False]
    print(any(adult))
    print(all(adult))
main()