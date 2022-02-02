# 리스트 결합
# extend를 통해 list1 + list2 형태로 사용가능
def main() : 
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]

    list1.extend(list2)
    print(list1)
main()