print('左下直角三角形')

n = int(input('短辺:'))

for i in range(1, n+1):
    for _ in range(i):
        print('*', end='')
    print()
