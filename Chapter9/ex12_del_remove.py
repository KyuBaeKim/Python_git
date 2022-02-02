# 삭제
# .remove : 리스트에서 값을 찾아 첫번쨰 해당 요소를 제거 (하나만 제거)
# del(리스트[인덱스]) : 지정한 인데스의 요소를 제거
# [시작:끝] = [] <= 지정한 범위의 요소를 제거

def main():
    score = [88, 95, 70, 100, 99, 88, 100, 78, 50]
    score.remove(100) # 첫번째 100만 삭제
    print(score)

    del(score[2]) # 인덱스가 2인 것을 삭제한다.
    print(score)
    
    score[1:4] = []
    print(score)
main()