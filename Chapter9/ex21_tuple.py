# 튜플 : 수정, 삭제 할 수 없음 --> 가로 생략 가능
# 데이터 한개 짜리는 ,를 꼭붙여줘야함
# (1) : tuple x 
# (1,) : tuple o

def main():
    score = 88, 95, 70, 100, 99
    print(score)

    score = 88,
    print(score)

    score = 88
    print(score)
main()