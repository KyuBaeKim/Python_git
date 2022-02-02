# append 매서드 함수
# insert 매서드 함수

# .append(값) : 리스트의 끝에 ㄱ밧을 추가
# .insert(위치, 값) : 지정한 위치에 값을 삽입
def main():
    nums = [1, 2, 3, 4]
    nums.append(5)
    print(nums,"")

    nums.insert(2, 99)
    print(nums)
main()