# 正の整数値を0までカウントダウン

print('カウントダウンします。')
n = int(input('正の整数値：'))

while n >= 0:
    print(n, end=' ')
    n -= 1           # nから1を引く
print()
