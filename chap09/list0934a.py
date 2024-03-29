"""乗算表を表示（その２）"""

upper = int(input('1から何まで：'))

def multiplication_table() -> bool:
    """1～nまでの乗算表を表示"""
    if    1 <= upper <=  3: w = 2
    elif  4 <= upper <=  9: w = 3
    elif 10 <= upper <= 31: w = 4
    else                  : return False

    f = '{{:{}d}}'.format(w)
    print('-' * upper * w)
    for i in range(1, upper + 1):
        for j in range(1, upper + 1):
            print(f.format(i * j), end='')
        print()
    print('-' * upper * w)
    return True

multiplication_table()
