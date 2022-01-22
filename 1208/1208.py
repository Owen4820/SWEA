def highest_floor(x):
    highest_floor = x[0]
    highest_idx = 0
    for idx in range(0,len(x)):
        if x[idx] > highest_floor:
            highest_floor = x[idx]
            highest_idx = idx
    return highest_idx , highest_floor


def lowest_floor(x):
    lowest_floor = x[0]
    lowest_idx = 0
    for idx in range(0,len(x)):
        if x[idx] < lowest_floor:
            lowest_floor = x[idx]
            lowest_idx = idx
    return lowest_idx , lowest_floor

for i in range(1,11):
    try_number = int(input())
    floor_list = list(map(int,input().split()))
    for j in range(0, try_number):
        high_idx, high_floor = highest_floor(floor_list)
        low_idx, low_floor = lowest_floor(floor_list)
        floor_list[high_idx] -= 1
        floor_list[low_idx] +=1
        high_idx, high_floor = highest_floor(floor_list)
        low_idx, low_floor = lowest_floor(floor_list)
        x = high_floor - low_floor

    print(f'#{i} {x}')