# dic의 인덱싱은 dic['키'] 형태로 반환하면 된다,

def main():
    dic = {  'boy': '소년',  'school': '학교', 'book': '책' }
    
    print(dic.get('boy'))
    print(dic.get('girl'))
    print(dic.get('girl','사전에 없는 단어입니다.'))

    dic = {  'boy': '소년',  'school': '학교', 'book': '책' }
    if 'student' in dic :
        print("사전에 있는 단어입니다.")
    
    else:
        print("이 단어는 사전에 없습니다.")
main()
