# 読み込んだ回数だけ挨拶する（カウントは0から）

n = int(input('挨拶は何回：'))

for i in range(n):  # [0,1,2,3,....n-1]
    print('No.', i, '：こんにちは。')
