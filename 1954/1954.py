def snail(N):
    list_number = [] # 먼저 달팽이 숫자가 들어갈 리스트를 만들어준다.
    for x in range(0,N):
        list_number.append([1] * N) 

    i = 1 # 첫번째 칸에 1이 들어가므로 1을 넣어준다.
    cycle = (2*N-1)//4 + 1 # 가로,세로,가로,세로 총 4번 진행한것이 1 사이클이다. 예를들어 N이 4인경우 사이클이 최소 2번 돌아야 리스트가 다 채워진다.
    for set in range(0,cycle): # 사이클이 진행될 떄 마다 안으로 들어가는것을 표현해줘야 한다.
        for n in range(set,N-set): # 사이클에서 첫번째 가로로 진행(왼쪽 - > 오른쪽 방향)
            list_number[set][n] = i
            i +=1 # 진행할수록 숫자가 1씩 높아지므로 i+=1을 해준다.

        for n in range(1+set,N-set): # 사이클에서 첫번째 세로로 진행(위 -> 아래 방향)
            list_number[n][-1-set] = i
            i +=1

        for n in range(1+set,N-set): # 사이클에서 두번째 가로로 진행(오른쪽 -> 왼쪽 방향)
            list_number[N-1-set][-1-n] = i
            i +=1

        for n in range(1+set,N-1-set): # 사이클에서 두번째 세로로 진행(아래 -> 위 방향)
            list_number[-1-n][set] = i
            i +=1

    return list_number

T = int(input())
for tc in range(1,T+1):
    N=int(input())
    ans = snail(N)
    print(f'#{tc}')
    for i in range(0,N):
        print(*ans[i], sep=' ')