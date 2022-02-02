# 컬렉션 관리
# filter(판정함수, 시퀀스) -> 시퀀스
# 시퀀스의 각 요소를 판정함수에 전달하여 True를 리턴하는 요소로만 구성된 새로운 시퀀스 리턴

from tabnanny import check


def flunks(s):
    return s < 60

score = [45, 89, 72, 53, 94]
for s in filter(flunks, score):
# 판정함수가 true이면 
    print(s)
    
def check_high_score(s):
    return s >= 90
high_scores = list(filter(check_high_score, score))
print(high_scores)

# filter 함수를 사용하지 말고 60점 미만 성적을 찾으세요.

result = []
for s in score : 
    if s < 60 :
        result.append(s)
print(result)
