# 리스트의 사본
# 시퀀스.copy() -> 시퀀스 복사본
# 주소가 아닌 값을 복사 할때 쓰임
def main():
    list1 = [1, 2,3 ]
    list2 = list1

    print(list1 == list2)
    list2[2] = 100
    print(list1)
    print(list2)
    
    print("-"*30)
    print(list1 == list2)
    list1 = [1, 2, 3]
    list2 = list1.copy()
   
    print("-"*30)
    print(list1 == list2)
    list2[1] = 100
    print(list1)
    print(list2)

    print("-"*30)
    print(list1 == list2)
main()
