"""アノテーション"""


def puts(n: int, s: str) -> None:
    """n個のうんたら

    仮引数：
        n -- 
        s --
    返却値：
        None

    """
    for _ in range(n):
        print(s, end='')


print(puts.__doc__)

print(puts.__annotations__)
