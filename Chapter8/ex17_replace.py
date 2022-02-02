# .replace(기존문자열, 바꿀무자열) 대체
def main() : 
    s = "독도는 일본땅. 대마도도 일본땅"
    print(s)
    print(s.replace('일본', '한국'))

    # 중간에 있는 모든 공백을 제거하시오
    # --> "독도는 일본땅.대마도도 일본땅"
    s1 = s.replace(' ', '')
    s1 = s1.replace('.','')
    print(s1)

main()