def find_arrive(x): # 도착점의 idx값을 얻기 위한 함수이다.
    for i in range(0,100):
        if x[-1][i] == 2: # 사다리의 맨 아랫줄의 값들 중 2의 idx값을 구하였다.
            break
    return i

def find_start(ladder):
    arrive_idx = find_arrive(ladder) # 먼저 도착점의 idx값을 구해주었다.
    j = 99 # 100층을 올라야 하니 j = 99로 설정하고 0이 되면 while문을 탈출하게 해주었다.
    while j > 0:
        if ladder[j][arrive_idx-1] == 1: # 현재 위치에서 왼쪽이 1이라면 왼쪽으로 건너야 하니 arrive_idx를 1 빼주었다.
            while ladder[j][arrive_idx-1] == 1:
                arrive_idx -= 1
        elif ladder[j][arrive_idx+1] == 1: # 현재 위치에서 오른쪽이 1이라면 오른쪽으로 건너야 하니 arrive_idx를 1 더해주었다.
            while ladder[j][arrive_idx+1] == 1:
                arrive_idx += 1
        j = j - 1 # 1층 상승
    
    return arrive_idx


for tc in range(0,10):
    num = int(input())
    arr = []
    for i in range(0,100):
        arr.append(list(map(int,input().split())))
        arr[i].append(0) # 만약 현재 idx가 0에서 왼쪽을 바라볼떄 idx=99를 바라볼수도 있으니 idx=100에 0을 패딩해주었다.
    
    print(f'#{num} {find_start(arr)}')