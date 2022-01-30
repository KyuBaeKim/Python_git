#  조건부
age = int(input("나이를 입력하세요 : "))

if age < 20:
    print("="*20) # 들여쓰기를 통해 if에 종속됨을 의미한다.
    print("미성년자입니다.")
    print("="*20)