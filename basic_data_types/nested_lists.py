if __name__ == '__main__':
    grades = [[input(), float(input())] for _ in range(int(input()))]

    second_highest_score = list(sorted({x[1] for x in grades}, reverse=True))[-2]
    results = sorted([x[0] for x in grades if x[1] == second_highest_score])
    for n in results:
        print(n)
    #print(score_list)
    #rev_srt = sorted(grades, key=lambda x: x[1], reverse=True)
    #sec_lower_grade = rev_srt[]
    #print(rev_srt)
