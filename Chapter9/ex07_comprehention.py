# 컴프리핸션
def main():
    nums = [n*2 for n in range(1,11)]
    for i in nums :
        print(i, end = ",")
    print()
    
    # 컴프리 핸션 x
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    for n in range(1,11) :
        nums.append(n)
        # (매서드 함수) append --> 리스트 끝에 추가하라.
    print(nums)
    
    print([n for n in range(1,11) if n % 3 ==0])
    # n 을 3으로 나누었을 때 나머지가 0인 것 만 추출
    # for n in range(1, 11) 부터 실행
    # if n % 3 == 0 실행
    # 제일 앞에 n으로 들어감
     

main()