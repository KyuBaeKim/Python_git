# 텍스트 파일을읽어서 내용을 리턴하는 함수를 작성하세요.
# 매개변수 : 파일명
# 리턴값 : 파일 내용
def load(filename):
    try:
        # with ~ as ~ 를 사용하면 
        # 코드 블럭을 읽고 난후 자동으로 파일이 클로즈 된다. 
        with open(filename, 'rt', encoding="utf-8") as file:
            # 디폴트는 text 모드 이다.
            content = file.read()
            return content
    except:
        return ''
    
# 파일명과 내용을 전달받아
# 지정한 파일로 저장하는 함수를 작성하세요.

def save(filename, content) :
    with open(filename, 'wt', encoding="utf-8") as file:
    # encoding 을 통해 utf-8 로 문자코드를 처리할 수 있도록 한다.
    # 문자코드 UTF-8 사용
        file.write(content)    



def main():
    try:
        file_name = "live.txt"
        content = load(file_name)
        
        print(content)
        # 추가할 문자열을 입력 받아서,, 기존 문서 끝에 ㅊ추가하고 , 저장하세요.
        text = input("내용 :")
        content += text + '\n'
    
        save(file_name,content)
    except Exception as e :
        print(e)
main()