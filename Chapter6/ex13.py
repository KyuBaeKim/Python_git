print("3 + 4 =  ?")
while True :
    a = int(input("정답을 입력하시오 = "))
    if a == 7 :
        break
print("참 잘했어요")

# 문제
# 사용자로부터 이름을 입력받아
# 리스트에 이름이 있는지 여부를 판단하세요.
# 찾았으면 몇번째 있는지 출력하고,
# 없다면 xxx는 목록에 없습니다. 출력

names = ['홍길동', '고길동', '둘리', '뚜치']
while True:
    search_name = input("사용자의 이름을 입력하세요 : ")
    if search_name == 'exit' :
        break
    search_result = False
    count = 0 # 순차 검색
    for s in names : # True
        if s == search_name:
            search_result = True
            break
        count += 1

print('결과 : ', search_result)
if search_result:
    print(search_name," 은 ", count+1,"번쨰에 있습니다.",sep ="")
else :
    print(search_name, "는 목록에 없습니다.",sep ="")

    
