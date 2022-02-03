# assert
# assert 조건, 메시지
# 조건이 True이면 통과,
# False이면 메시지를 가지는 예외 발생

def main():
    try:
        score = 128
        assert score <= 100, "점수는 100이하여야 합니다."
        print(score)
    except Exception as e:
        print(e)
main()