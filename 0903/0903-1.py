# 昨日のおさらい
# 「数字を入力してください」と画面に表示しよう。文末に改行しない形式で表示すること
# ヒント：文末に改行を入れずに画面表示する→P32 List23
print("数字を入力してください", end='')

# input()を使ってキーボードから値を入力できるようにし、入力された値を変数numに代入しよう
# ヒント：input()→テキストP34
num = input()

# numの値をint型に変換しよう
# ヒント：P36型の変換／入力された値はすべてstr型。これをintに変換しよう
a = int(num)

# num ÷ 3の結果を変数 rslt に代入しよう
rslt = a / 3

# rslt の内容をprint で表示しよう
print(rslt)