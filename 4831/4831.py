def list_cango(list_c, go_c, N):
    for i in range(0,len(list_c)-1):
        if list_c[i] + go_c < list_c[i+1]:
            print("범위아웃")
            return 0

    count = 0
    pos = 0
    while True:
        if pos >= N:
            break
        pos = pos + go_c
        while pos not in list_c:
            pos -=1
        count += 1
    count -= 1
    return count



T = int(input())
for tc in range(0,T):
    K, N, M = map(int, input().split())
    list_c = list(map(int, input().split()))
    list_c.insert(0,0)
    list_c.insert(M+1,N)
    count_c = list_cango(list_c, K, N)
    print(f'#{tc+1} {count_c}')