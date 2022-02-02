# 분할
# splitlines
def main():
    trabler = '''강나루 건너서
밀밭 길을 

구름에 달 가듯이 
가는 나그네
'''

# 들여쓰기, 공백, \n들도 문자로 인식
    poet  = trabler.splitlines()
    for line in poet :
        print(line)
    print(poet)
main()