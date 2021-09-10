x = int(input('整数:'))
y = int(input('シフトするビット数:'))

print('{:b}'.format(x))
print('{:b}'.format(x << y))
print('{:b}'.format(x >> y))
