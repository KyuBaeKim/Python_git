# .sort([reverse=True][key = 키에 적용할 함수]) 
# 리스트를 정력(디폴트는 오름차순), reverse=True로 오름차순/내림차순 선택

# .reverse() : 리스트의 순서를 역으로 바꿈

# sorted() : 지정한 시퀀스를 정렬하여 새로운 리스트로 리턴<함수형태> 

def main(): 
    score = [88, 95, 70, 100, 99]
    score.sort()
    print(score,"\n")
    
    # max(), min() 함수를 사용하지 않고
    # 최솟값 최댁밧을 구하시오
    
    # pop 이용
    
    last = score.pop()
    first = score.pop(0)

    print(f"최댓값 : {last}\n최솟값 : {first}\n")
    
    # 그냥 출력
    print(f"최댓값 : {score[0]}\n최솟값 : {score[-1]}\n")
    score.reverse()
    print(score)

main()