from file_utill import load_json, save_json


def main():
    
    # 리스트
    datas = [123, 45, 56, 99]

    # 사전
    data1 = {
        'boy':'소년', 
        'school':'학교',
        'book':'책'
    }
    save_json('data1.json',data1)
    content = load_json('data1.json')
    print(content)

main()