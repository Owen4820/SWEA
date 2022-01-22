T = int(input())
for i in range (1,T+1):
    number = int(input())
    scores = list(map(int,input().split()))
    max_count = 0
    for score in scores:
        count = 0
        for j in range(0,len(scores)):
            if score == scores[j]:
                count += 1
        if count > max_count:
            max_count = count
            max_count_score = score
        elif count == max_count:
            max_count_score = max(max_count_score, score) 
    print(f'#{number} {max_count_score}')

