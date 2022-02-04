def find_arrive(x): # 도착점의 idx값을 얻기 위한 함수이다.
    for i in range(0,100):
        if x[-1][i] == 2: # 사다리의 맨 아랫줄의 값들 중 2의 idx값을 구하였다.
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