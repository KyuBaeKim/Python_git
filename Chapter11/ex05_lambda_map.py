# 람다 함수 --> 다른 언어에서 많이 활용 ( java, 코틀린)
# 한줄로 구현가능한 함수를 매개 변수로 전달할때 사용
# 함수의 축약표현이다.
# lambda 인수 : 식

def increase(x): # --> lambda x : x+1과 같은뜻
    return x + 1

def main():
    lambda x : x + 1 #--> x + 1을 리턴해준다는 뜻
    score = [45, 89, 72, 53, 94]
    for s in filter(lambda x : x < 60, score ) :
        print(s)
    print()
    
    high_scores = list(filter(lambda x: x>=90, score))
    print(high_scores)
    print()
    
    for s in map(lambda x : x/2 , score):
        print(s, end=",")
main()