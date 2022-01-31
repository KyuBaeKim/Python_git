# continue
# continue를 이용할 경우 루프를 다시 돌게 된다.
# filtering 기능을 한다.

score = [92, 86, 68, -1, 56]
for score in score :
    if score == -1:
        continue # s가 -1 이면 다음 score list 부터 다시 루프를 돈다.
    print(score)
print('성적 처리 끝')

# 올바른 데이터 (0 <= score <= 100)
# 합계와 평균을 구하세요.
scores = [92, 86, 68, -1, 56, -30, 90, 140, 90]
total = 0
count = 0
for score in scores :
    if (score < 0) or (score > 100):
        continue
    else :
        total += score
        count += 1
average = total/count
print("총합 =", total)
print("평균 = ", round(average, 2))