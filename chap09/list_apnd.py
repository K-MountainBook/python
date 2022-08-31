# ミュータブルなデフォルト引数の挙動を確認

def list_apnd(a, lst=[]):
    """呼び出されるたびにリストを連結して表示"""
    lst += a
    print(lst)

list_apnd([1])    # []    に[1]を追加。   lstのデフォルト値は[1]になる。
list_apnd([2])    # [1]   に[2]を追加。   lstのデフォルト値は[1, 2]になる。
list_apnd([3, 4]) # [1, 2]に[3, 4]を追加。lstのデフォルト値は[1, 2, 3, 4]になる。