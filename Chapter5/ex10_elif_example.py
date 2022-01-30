# 키보드로 성적을 입력
# 성적의 구간에 따라 학점 출력
# 90 ~ 100 : A 학점
# 80 ~ 89 : B 학점
# 70 ~ 79 : C 학점
# 60 ~ 69 : D 학점
# 60미만 : F 학점

grade = int(input("점수를 입력 하세요:"))

if 90 <= grade <= 100 :
    print('A학점')
elif 80 <= grade <= 89 :
    print('B학점')
elif 70 <= grade <= 79 :
    print('C학점')
elif 60 <= grade <= 69 :
    print('D학점')
else :
    print('F학점')    