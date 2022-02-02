def main() :
    scores = [70, 30, -10, 100, 160, 90]
    # 음수 또는 100초과 데이터를 제외한 합계를 구하시오.
    # 컴프리헨션을 이용해서
    scores = [n for n in scores if (n>=0) and (n<=100)]
    print(scores)

    # 합계를 구함
    print("총합 : ", sum(scores))

main()