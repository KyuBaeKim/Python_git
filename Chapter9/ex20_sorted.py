def main():
    score = [88, 75, 0, 100, 99]
    sorted_score = sorted(score)
    
    print(score)
    print(sorted_score, "\n")

    score1 = [88, 95, 70, 100, 99]
    sorted_score1 = sorted(score, reverse = True)
    print(score1)
    print(sorted_score1)
main()