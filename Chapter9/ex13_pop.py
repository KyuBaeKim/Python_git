# 삭제
# .pop() : 리스트릐 끝 요소를 삭제하고 삭제한 요소를 리턴
# .pop(인데스) : 지정한 인덱스의 끝 요소를 삭제하고 삭제한 요소를 리턴

def main():
    score = [88, 95, 70, 100, 99]
    print(score.pop())
    print(score.pop())
    print(score.pop(1))
    print(score)
main()