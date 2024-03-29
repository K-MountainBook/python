# 行列の和を求める（行列／列数／値を読み込む）

print('行列の和を求めます。')
height = int(input('行数：'))
width = int(input('列数：'))

a = [None] * height
for i in range(height):
    a[i] = [None] * width
    for j in range(width):
        a[i][j] = int(input('a[{}][{}]：'.format(i, j)))

b = [None] * height
for i in range(height):
    b[i] = [None] * width
    for j in range(width):
        b[i][j] = int(input('b[{}][{}]：'.format(i, j)))

c = [None] * height
for i in range(height):
    c[i] = [None] * width
    for j in range(width):
        c[i][j] = a[i][j]+b[i][j]

for i in range(height):
    for j in range(width):
        print('c[{}][{}] = {}'.format(i, j, c[i][j]))
