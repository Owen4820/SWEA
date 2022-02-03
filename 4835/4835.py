def list_sum(list_number, N, M):
    list_sum = []
    for i in range(0,N-M+1):
        sum = 0
        for j in range(0,M):
            sum += list_number[i+j]
        list_sum.append(sum)

    return max(list_sum) - min(list_sum)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))
    result = list_sum(list_N, N, M)
    print(f'#{tc} {result}')
