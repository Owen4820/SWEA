def func1(x,y):
    if y == 1:
        return x
    else :
        return x * func1(x,y-1)

for i in range(1,11):
    num = int(input())
    x, y = map(int,input().split())
    print(f'#{num} {func1(x,y)}')