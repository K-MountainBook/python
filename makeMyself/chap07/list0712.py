# 人数と点数を読み込んで合計点・平均点を表示

print('合計点と平均点を求めます。')
print('endと入力で入力終了')

number = 0
tensu = []

while True:
    s = input('{}番の点数：'.format(number + 1))
    if s == 'end':
        break
    tensu.append(int(s))
    number += 1

total = sum(tensu)

print('合計は{}点です。'.format(total))
print('平均は{}点です。'.format(total / number))
