# 리스트
# 슬라이싱
def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 2 ~ 4자리까지 오른쪽 데이터로 변환
    nums[2:5] = [20, 30, 40] 
    print(nums)

    # 6,7자리를 삭제하고 오른쪽 데이터로 채운다.
    nums[6:8] = [60, 70, 80, 90]
    print(nums)
main()