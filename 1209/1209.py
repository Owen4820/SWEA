for k in range(0,10):
    number = int(input())
    arr = []
    for i in range(0,100):
        arr.append(list(map(int,input().split())))

    max_sum1 = max_sum2 = 0
    total1 = total2 = total_11to5 = total_1to7 = 0
    for i in range(0,100):
        total = sum(arr[i])
        if total1 > max_sum1:
            max_sum1 = total1
        total1 = 0

        for j in range(0,100):
            total2 = total2 + arr[i][j]
            if total2 > max_sum2:
                max_sum2 = total2
        total2 = 0

        total_11to5 += arr[i][i]

        total_1to7 += arr[i][99-i]

    max_sum = max(max_sum1, max_sum2, total_1to7, total_11to5)

    print(f'#{number} {max_sum}')
