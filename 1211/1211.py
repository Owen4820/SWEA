for try_num in range (0,10):
    number = int(input())

    arr = []
    for i in range(0,100):
        arr.append(list(map(int,input().split())))
        arr[i].append(0)

    start_point = []
    for idx in range(0,100):
        if arr[0][idx] == 1:
            start_point.append(idx)

    min_count = 1000
    for i in start_point:
        sp = i
        j = 0
        count = 0
        while j < 100:
            if arr[j][sp-1] == 1:
                while arr[j][sp-1] == 1:
                    sp -= 1
                    count += 1
            elif arr[j][sp+1] == 1:
                while arr[j][sp+1] == 1:
                    sp += 1
                    count += 1
            j+=1

        if count < min_count:
            min_count = count
            min_point = i
    print(f'#{number} {min_point}')