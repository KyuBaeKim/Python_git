# 최대값, 최솟값, 길이

def main():
    score = [88, 95, 70, 100, 99, 88, 78, 50]

    
    print(f"학생수는 {len(score)}명 입니다.")
    print(f"최고 점수는 {max(score)}점 입니다.")
    print(f"최소 점수는 {min(score)}점 입니다.")
    
    print()
    print(f"최고 점수를 받은 학생의 위치는 = {score.index(max(score))+1}번째 입니다.")
    print(f"최소 점수를 받은 학생의 위치는 = {score.index(min(score))+1}번째 입니다.")
main()