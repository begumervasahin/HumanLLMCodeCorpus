def fonk1(b3: str, b4: str) -> bool:
    b1 = b3.replace(" ", "").lower()
    b2 = b4.replace(" ", "").lower()
    return sorted(b1) == sorted(b2)
def fonk2() -> None:
    b3 = 'ey edip'
    b4 = 'pide ye'
    b5 = fonk1(b3, b4)
    print(f"Are '{b3}' and '{b4}' anagrams? {b5}")
if b6 = = "__main__":
    fonk2()