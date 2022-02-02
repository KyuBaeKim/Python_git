# .index(n) : 지정한 값을 찾아 해당 요소의 인덱스를 리턴, 없으면 예외 발생
# count(n) : 지정한 값이 리스트에 몇 번 나오는지 계산하여 리턴
# .find('문자열') : find는 문자열을 찾아준다. 값 x 
# 값이 list에 있는지 판단하려면 in 연산자를 이용 --> 문자열 ppt에 있음

def main():
    score = [88, 95, 70, 100, 99, 88, 78, 50]
    perfect = score.index(100)
    print(f"만점 받은 학생은 {perfect+1}번 입니다.")
    
    penum = score.count(100)
    print(f"만점자 수는 {penum}명 입니다.")
main()