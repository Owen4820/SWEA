def find_word(N,K,puzzle_list):
    count = 0
    ans_list = []

    puzzle_list.insert(0,[0]*N) # 먼저 puzzle_list의 위, 아래, 오른쪽, 옆에 0을 패딩해준다.
    puzzle_list.insert(N+1,[0]*N)
    for i in range(0,N+2):
        puzzle_list[i].insert(0,0)
        puzzle_list[i].insert(N+1,0)

    ans = [1] * K  # 찾고자 하는 리스트를 찾는다. 이 떄 또한 [1,1,1] 과 [1,1,1,1]을 구분하기 위해 양 옆에 0을 패딩해줘서 [0,1,1,1,0] , [0,1,1,1,1,0]으로 만들어준다.
    ans.insert(0,0)
    ans.insert(K+1,0)

    for i in range (1,N+1): # 먼저 가로로 진행한다.
        for j in range(0, N-K+1):
            for k in range(0,K+2):
                ans_list.append(puzzle_list[i][j+k]) # ans_list를 채워준다
            if ans_list == ans: # 만들어진 ans_list가 ans와 일치하면 count를 하나 늘려준다.
                count +=1
            ans_list = []
    
    for i in range (1,N+1): # 다음 세로로 진행한다.
        for j in range(0, N-K+1):
            for k in range(0,K+2):
                ans_list.append(puzzle_list[j+k][i]) # ans_list를 채워준다
            if ans_list == ans: # 만들어진 ans_list가 ans와 일치하면 count를 하나 늘려준다.
                count +=1
            ans_list = []


    return count

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    puzzle_lists = []
    for i in range(0,N):
        puzzle_list = list(map(int, input().split()))
        puzzle_lists.append(puzzle_list)

    print(f'#{tc} {find_word(N,K,puzzle_lists)}')
