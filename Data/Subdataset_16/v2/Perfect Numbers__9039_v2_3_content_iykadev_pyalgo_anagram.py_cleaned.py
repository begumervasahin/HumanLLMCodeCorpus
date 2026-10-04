def fonk1(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    b1 = list(s2)
    for char in s1:
        if char in b1:
            b1.remove(char)
        else:
            return False
    return True
def fonk2() -> None:
    print(fonk1('ey edip', 'pide ye'))
if b2 = = "__main__":
    fonk2()