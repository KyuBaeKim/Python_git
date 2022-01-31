# 리스트에 성적 데이터가 있음
# 평균을 구하세요.
# 최소 성적을 구하세요.

scores = [34, 78, 90, 35, 100, 88] # 컬렉션은 복수형으로 많이준다.

total = 0
num = -1 
min_score = 101
max_score = 0
for score in scores :
    total += score
    num += 1 
    if score < min_score :
        min_score = score
    if score > max_score :
        max_score = score
print("평균 = ", round(total/len(scores), 1))
print("최고 성적 = ", max_score)
print("최소 성적 = ", min_score)
