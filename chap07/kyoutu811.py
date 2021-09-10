import random


atari = [0,99]
nitou = [11 , 22 , 33 , 44 , 55 , 66 , 77 , 88]
santou = [5,10, 15,20,25, 30,35 ,40 ,45 ,50 ,60, 65,70,75,80,85 , 90 , 95]

list = []

for n in range(10):
    list.append(random.randint(1,99))

for i in range(10):
    for j in range(len(atari)):
        if list[i]==atari[j]:
            print('1等賞です。')
            break

    for k in range(len(nitou)):
        if list[i]== nitou[k]:
            print('2等賞です。')
            break

    for l in range(len(santou)):
        if list[i]== santou[l]:
            print('3等賞です。')
            break

    print('はずれ')