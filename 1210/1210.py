def find_arrive(x):
    for i in range(0,100):
        if x[-1][i] == 2:
            break
    return i
    
for i in range (1,11):
    num = int(input())
    arr = []
    for i in range(0,100):
        arr.append(list(map(int,input().split())))
        arr[i].append(0)

    x_point = find_arrive(arr)
    j = 99
    while j > 0:
        if arr[j][x_point-1] == 1:
            while arr[j][x_point-1] == 1:
                x_point -= 1
        elif arr[j][x_point+1] == 1:
            while arr[j][x_point+1] == 1:
                x_point += 1
        j = j - 1
    print(f'#{num} {x_point}')