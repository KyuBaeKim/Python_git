def main():
    # 얕은 복사
    list0 = ['a', 'b']
    list1 = [list0, 1, 2]
    list2 = list1.copy() # 얕은복사
    
    list2[0][1] = 'c'
    # lsit0 참조 안에 list0 참조를 복사 했기 떄문에 list1과 list2의 결과가 같다
    list2[1] = 1000
    print(list1)
    print(list2)
main()