# aはbで割り切れるか

a = int(input('整数a：'))
b = int(input('整数b：'))

c = b != 0 and a % b
print(c, end='…')

if c:
    print('aはbで割り切れません。')
else:
    print('bが0またはaがbで割り切れます。')
