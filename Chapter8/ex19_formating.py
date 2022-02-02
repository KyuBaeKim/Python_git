# 포맷팅
# 실수 flaot
def main():
    f1 = 12.3456
    print(f'f1의 값은 {f1}입니다.')

    result1 =f'{f1:.2f}'
    print(result1)

    year = 2022
    month = 1
    day = 6
    
    # 작성일 : 2022-01-06
    print(f'작성일: {year}-{month:02}-{day:02}')
main()