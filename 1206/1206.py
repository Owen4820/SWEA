for k in range(1,11):
    list_len = int(input())
    list_gn = list(map(int,input().split()))

    count = 0
    for i in range (2,len(list_gn)-2):
        for j in range(1,list_gn[i]+1):
            if list_gn[i-1] < j and list_gn[i-2] < j and list_gn[i+1] < j and list_gn[i+2] < j:
                count +=1
    print(f'#{k} {count}')
