# 슬라이싱
# 데이터 삭제 없이 대입하는 방법
# nums[n:n] <= [begin,end]를 같게 해주면 된다.

# nums[n] : 인덱싱은 데이터를 삭제 하고 이중 리스트로 만든다.
def main():
    nums = [1, 2, 3, 4]
    nums[2:2] = [90, 91, 92]
    print(nums)

    nums[2] = [90, 91, 92]
    print(nums)
main()