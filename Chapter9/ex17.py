def main():
    names = [ '홍길동', '고길동','둘리','또치' ]
    
    scores = [90, 80, 50, 30]
    name = input("검색이름 : ")
    if name in names :
        loc = names.index(name)
        score = scores[loc]
        print(f"{name}의 성적은 {score}점 입니다.")
    else :
        print(f"{name}은 없는 학생입니다.")
main()