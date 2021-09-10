# キーボードから入力された値が偶数なら「even」奇数なら「odd」と表示するプログラムを作成しよう

i = int(input())


if i == 0:
    print("ZERO");
elif i % 2 == 0:
    print("even")
elif i % 2 == 1:
    print("odd")
    