# 연습

def main():
    datas = [12, 34, 56, 78, 90]
    # 리스트를 data. txt 파일로 저장하세요.
    # 12,34,56,78,90
    
    # comprehention
    content = [str(n) for n in datas]
    print(content)

    # for문
    content = []
    for n in datas :
        content.append(str(n))
    print(content)

    # map핑
    content = list(map(str, datas))
    print(content)

    content = ','.join(content)
    print(content)

    try:
        with open('data.txt', 'wt') as file:
            file.write(content)
    except Exception as  e:
        print(e)

main()