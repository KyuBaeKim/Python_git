# 문제
# 사용자로부터 이름을 입력받아
# 리스트에 이름이 있는지 여부를 판단하세요.
# 찾았으면 몇번쨰에 있는지 출력하고,
# 없다는 xxx는 목록에 없습니다. 출력

names = ['홍길동', '고길동', '둘리', '뚜치']

search_name = input("사용장의 이름을 입력하세요 : ")
search_result = False
count = 0
for s in names : # 순차 검색
    if s == search_name : # True
        search_result = True
        break
    count += 1
    
print('결과 : ', search_result)
if search_result :
    print(search_name, "은 ", count + 1, "번째에 있습니다", sep = "")
else : 
    print(search_name, "는 목록에 없습니다", sep="")