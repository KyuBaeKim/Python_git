def main():
    dic = {
        'boy':'소년', 
        'school':'학교',
        'book':'책'}
    dic['boy'] = '남자아이' # 기존 값 수정
    dic['girl'] = '소녀' # 새로운 엔트리 추가
    del dic['book'] # 기존 엔트리 제거
    
    print(dic)
    print()
    print(dic.keys())
    print(dic.values())
    print(dic.items())
    print()
    
    keylist = dic.keys()
    for key in keylist:
        print(key, dic[key])
        print()

        diclist = dic.items()
    for item in diclist :
        print(f"{item[0]} {item[1]}" )
        print()
        
    for key, value in diclist :
        print(f"{key} {value}")
        print()
main()
    