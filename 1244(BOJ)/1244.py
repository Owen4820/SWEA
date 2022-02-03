def switch(x): # 0이면 1로, 1이면 0으로 바꿔주는 함수
    if x == 0:
        return 1
    return 0


def man(x): # 남자가 스위치를 바꿔주는 함수
    y = x
    while x-1 < len(list_switch):
        list_switch[x-1] = switch(list_switch[x-1])
        x += y


def woman(x): # 여자가 스위치를 바꿔주는 함수
    i = 0
    while x-1+i < len(list_switch) and x-1-i >= 0: # 바꾸려는 스위치가 스위치의 범위를 벗어나지 않도록 제어해준다.
        if i == 0: # 제일먼저 부여받은 번호를 바꿔준다. 이 때 자기자신만 바꿔준다.
            list_switch[x-1] = switch(list_switch[x-1])
        elif list_switch[x-1+i] == list_switch[x-1-i]: # 부여받은 번호를 기준으로 앞뒤가 같을경우 그 두개의 스위치를 건들여준다.
            list_switch[x-1+i] = switch(list_switch[x-1+i])
            list_switch[x-1-i] = switch(list_switch[x-1-i])
        else: # 앞뒤가 다른경우 while문 탈출
            break
        i +=1


number_switch = int(input()) # 스위치의 갯수
list_switch = list(map(int, input().split())) # 스위치의 처음 상태
number_student = int(input()) # 학생의 수
for i in range(0, number_student): # 학생의 수 만큼 학생의 성별과 스위치 번호를 받는다.
    x,y = map(int, input().split())
    if x == 1: # 받은 학생의 성별이 남성이면 man 함수 실행
        man(y)
    elif x == 2: # 받은 학생의 성별이 여성이면 woman 함수 실행
        woman(y)

z = number_switch//20 +1 # 20개씩 끊어서 리스트로 나타내기 위한 함수
a = 0
for i in range(0,z):
    list_switch_real = []
    if i == z-1: # 마지막 차례일경우 20개가 아닌 스위치의 갯수를 20으로 나눴을 때 나머지 만큼만 출력
        for j in range(0, number_switch%20):
            list_switch_real.append(list_switch[a+j])
        print(*list_switch_real, sep=' ')
    else : # 처음부터 20개씩만 잘라서 출력
        for j in range(0,20):
            list_switch_real.append(list_switch[a+j])
        print(*list_switch_real, sep=' ')
        a += 20
