# data,txt 파일을 읽어서
# data = [12,34,56,8,90] 리스트로 복원

def main():
    try:
        with open("data.txt", "rt") as file:
            content = file.read()
            print(content)
        
        datas = content.split(',')  # split을 이용하여 ,를 기준으로 나눈다.
        print(datas)

        datas = list(map(int,datas))
        print(datas)
    except Exception as e:
        print(e)

main()