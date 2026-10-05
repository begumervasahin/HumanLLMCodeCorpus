def fonk1(a, b):
    return "".join([chr(ord(x) ^ ord(y)) for x, y in zip(a, b)])
def fonk2(b1 = "Enter input: "):
    return input(b1)
def fonk3(data):
    print("Intercepted data:", data)
if b2 = = "__main__":
    b3 = fonk2()
    b4 = b3
    fonk3(b4)