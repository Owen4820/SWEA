n = 152
x = '0 3 0 1 1 3 2 10 3 10 4 13 4 11 5 14 6 8 7 13 7 15 8 16 8 11 9 13 9 17 10 14 10 20 11 17 12 14 12 15 13 18 14 16 14 25 15 22 15 17 16 17 16 27 17 26 18 19 18 28 19 28 20 27 20 30 21 25 21 32 22 29 22 24 23 30 24 34 24 32 25 31 25 36 26 28 26 35 27 32 27 37 28 33 28 31 29 37 30 36 30 38 31 40 31 33 32 36 32 38 33 41 33 40 34 35 34 42 35 36 36 44 36 47 37 41 37 46 38 40 38 47 39 41 39 47 40 42 40 46 41 49 42 49 42 48 43 51 43 45 44 48 44 47 45 55 45 56 46 52 46 57 47 53 47 55 48 53 49 55 50 56 50 52 51 59 52 57 53 59 53 63 54 58 55 61 56 65 57 66 57 60 58 66 58 68 59 69 59 61 60 61 61 66 62 65 63 72 63 69 64 71 65 74 65 75 66 69 66 75 67 77 67 71 68 75 68 70 69 76 69 71 70 76 71 76 71 77 72 82 72 80 73 80 73 83 74 76 74 77 75 81 76 86 77 78 77 84 78 85 79 84 79 88 80 86 80 91 81 90 82 89 83 84 83 89 84 94 84 91 85 93 85 92 86 95 87 90 87 95 88 96 88 93 89 95 90 96 94 97 94 96 96 97 '
def tuple_list(x,n):
    list_x = x.split()
    list_tuple = []
    idx = 0
    for i in range(0,n):
        list_tuple.append((int(list_x[idx]), int(list_x[idx+1])))
        idx += 2
    
    return list_tuple
list_tuple = tuple_list(x,n)

def find_route(x):
    list_stop_previous = []
    for char in x:
        if char [0] == 0:
            list_stop_previous.append(char[1])
    
    j = 1
    while j < 100:
        list_stop = []
        for char in x:
            if char[0] in list_stop_previous:
                list_stop.append(char[1])
        list_stop_previous = list_stop
        if 99 in list_stop:
            return 1
        elif list_stop == []:
            return 0

for i in range(1,11):
    t, n = map(int,input().split())
    num = input()
    num_tuple = tuple_list(num,n)
    print(f'#{t} {find_route(num_tuple)}')
