# break문
# 반복문을 벗어 나게 한다.

score = [92, 86, 68, 120, 56]
for s in score :
    if(s < 0) or (s > 100) :
        break
    print(s)
print("성적 처리 끝")
