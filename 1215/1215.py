x = int(input())
arr = []
for i in range(0,8):
    arr.append(str(input()))

count = 0
for i in range(0,8):
    for j in range(0, 9-x):
        y = str()
        y_reverse = str()
        for k in range(0,x):
            y = y + arr[i][j+k]
            y_reverse = arr[i][j+k] + y_reverse
        if y == y_reverse:
            count += 1

    for j in range(0,9-x):
        z = str()
        z_reverse = str()
        for k in range(0,x):
            z = z + arr[j+k][i]
            z_reverse = arr[j+k][i] + z_reverse
        if z == z_reverse:
            count +=1

print(count)