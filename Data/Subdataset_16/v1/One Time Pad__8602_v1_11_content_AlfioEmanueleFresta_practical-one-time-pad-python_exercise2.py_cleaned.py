
def fonk1():
    return b'This is intercepted input.'
def fonk2(data):
    print(f'Intercepted Output: {data}')
def fonk3():
    b1 = fonk1()
    b2 = b1
    fonk2(b2)
if b3 = = "__main__":
    fonk3()