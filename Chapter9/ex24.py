def main():
    # names = ['홍길동', '고길동', '둘리', '또치']
    # scores = [90, 80, 50, 30]
    scores = [
        ('홍길동', 90),
        ('고길동', 80),
        ('둘리', 50),
        ('또치', 30)
    ]
    
    for score in scores : # name, score = ('홍길동', 90)
        print(f"학생이름 : {score[0]}\n점수 : {score[1]}")
    print()
    for name, score in scores :
        print(f"학생명 : {name} 성적 : {score}")
main()