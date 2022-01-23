for try_num in range(0,10):
    num = int(input())
    y = str(input())
    x = str(input())

    count = 0
    for i in range(0, len(x)-len(y)+1):
        x_y = str()
        for j in range(0,len(y)):
            x_y += x[i+j]
        if x_y == y:
            count+=1

    print(f'#{num} {count}')
