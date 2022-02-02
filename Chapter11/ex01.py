# 컬렉션 관리 함수
# Enumerate
def main():
    race = ['저그', '테란', '프로토스']
    list(enumerate(race))
    # 순서를 매겨 주는 컬렉션 관리 함수
    
    score = [88, 95, 70, 100, 99 ]
    for no, s in enumerate(score, 1):
        # 1부터 시작하게 하기 위해 enumerate(리스트, 1)이라 함
        
        print(str(no)+"번 학생의 성적 : ", s)
main()