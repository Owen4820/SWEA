def fly(N,M,list_fly):
    max_fly = 0
    fly = 0

    for i in range(0,N-M+1):
        for j in range(0,N-M+1):
            for k in range(0,M):
                for l in range(0,M):
                    fly += list_fly[i+k][j+l]
            if fly > max_fly:
                max_fly = fly
            fly = 0
    
    return max_fly

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    list_flys = []
    for i in range (0,N):
        list_fly = list(map(int, input().split()))
        list_flys.append(list_fly)

    print(f'#{tc} {fly(N,M,list_flys)}')

