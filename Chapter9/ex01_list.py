# 리스트 name = [a, b, c]
def cal_sum(scores) :
    total = 0
    for s in scores :
        total += s
    return total

def print_score(subject,scores):
    total = cal_sum(scores)
    print(subject)
    print(f"총점 : {total}")
    print(f"평균 : {total/len(scores):.2f}\n")
    
def main():
    eng_scores = [88, 95, 70, 100, 99]
    kor_scores = [98, 56, 30, 63, 77]

    print_score('영어',eng_scores)
    print_score('국어',kor_scores)
    
main()