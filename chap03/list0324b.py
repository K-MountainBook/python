# 読み込んだ整数値が正であれば偶数／奇数の別を判定して表示（別解２）

n = int(input('正の整数値：'))

if n > 0:
    print('その値は正の{}です。'.format('奇数' if n % 2 else '偶数'))
else:
    print('正でない値が入力されました。')
