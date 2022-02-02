# .sort([reverse=True][key = 키에 적용할 함수]) 
def main():
    country = ['Korea', 'japan', 'CHINA', 'america']

    # list를 소문자로 만드는법 country = [ c.lower() for c in country]
        # print(country)
    
    country.sort(key = str.lower) 
    # str.lower   (o) 
    # str.lower() (x)
    # 소문자로 반환한 값을 이용해 평가를 하여라.
    
    print(country)
    country = ['South Korea', 'japan', 'CHINA', 'america']
    
    # 문자열의 길이가 긴 순으로 정렬하세요.
    country.sort(reverse=True, key = len)
    print(country)
main()
    
