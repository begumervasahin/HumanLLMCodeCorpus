def fonk1() -> bytes:
    return b'This is intercepted input.'
def fonk2(data: bytes) -> None:
    print(f'Intercepted Output: {data}')
def fonk3() -> None:
    b1 = fonk1()
    b2 = b1
    fonk2(b2)
if b3 = = "__main__":
    fonk3()