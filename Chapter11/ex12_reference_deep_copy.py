import copy
def main():
    # 깊은 복사
    list0 = ['a', 'b']
    list1 = [list0, 1, 2]
    list2 = copy.deepcopy(list1)
    # 깊은 복사
    
    list2[0][1] = 'c'
    print(list1)
    print(list2)
main()