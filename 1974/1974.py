def sudoku(numbers):
    for i in range(0,9): # 가로행의 검증
        b = set(numbers[i]) # 가로행을 set으로 변환
        if len(b) != 9:  # 만약 가로형에 중복이 있었다면 set으로 변환했을땐 길이가 9보다 작을것 이므로 9가 아닌경우 0을 반환
            return 0
    
    for i in range(0,9): # 세로행의 검증
        c = [] 
        for j in range(0,9):
            c.append(numbers[j][i]) # 세로행을 따로 리스트로 만들어 주는과정
        d = set(c) 
        if len(d) != 9: # 세로행을 set으로 변환시킨 후 길이가 9가 아닐 때 0 을반환
            return 0

    i = 0 # 3x3형의 검증
    while i<10: # 3x3의 박스가 9개 있으므로 9번 반복하게 해준다
        for idx_x in range(0,9,3): # 0 3 6
            for idx_y in range(0,9,3): # 0 3 6
                e = []
                for j in range(0,3):
                    for k in range(0,3):
                        e.append(numbers[idx_x+j][idx_y+k])
                if len(set(e)) != 9: # 만든 리스트를 set으로 바꿧을때 길이가 9가 아니면 0을 반환하게 한다.
                    return 0
        i += 1

    return 1

T = int(input())
for t in range(1,11):
    list_sudoku = []
    for i in range(0,9):
        numbers = list(map(int, input().split()))
        list_sudoku.append(numbers)
    print(f'#{t} {sudoku(list_sudoku)}')