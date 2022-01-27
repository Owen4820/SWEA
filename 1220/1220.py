def count_collide(x):
    list_d = []
    for i in range(0,100):
        list_ds = []
        for j in range(0,100):
            list_ds.append(x[j][i])
        list_d.append(list_ds)

    count = 0
    for list_x in list_d:
        while 0 in list_x:
            list_x.remove(0)
        for i in range(0,len(list_x) - 1):
            if list_x[i] == 1 and list_x[i+1] == 2:
                count+=1
    
    return count

for i in range(1, 11):
    n = int(input())
    list_x=[]
    for j in range(0,100):
        list_number = list(map(int,input().split()))
        list_x.append(list_number)
    count_num = count_collide(list_x)
    print(f'#{i} {count_num}')