for testnum in range(0,10):
    num = int(input())
    arr = []
    for i in range(0,100):
        arr.append(str(input()))

    x_max = 0
    for x in range (1,100):
        for i in range(0,100):
            for j in range(0, 101-x):
                y = str()
                y_reverse = str()
                for k in range(0,x):
                    y = y + arr[i][j+k]
                    y_reverse = arr[i][j+k] + y_reverse
                if y == y_reverse:
                    x_max = x
                    break


            for j in range(0,101-x):
                z = str()
                z_reverse = str()
                for k in range(0,x):
                    z = z + arr[j+k][i]
                    z_reverse = arr[j+k][i] + z_reverse
                if z == z_reverse:
                    x_max = x
                    break

    print(f'#{num} {x_max}')