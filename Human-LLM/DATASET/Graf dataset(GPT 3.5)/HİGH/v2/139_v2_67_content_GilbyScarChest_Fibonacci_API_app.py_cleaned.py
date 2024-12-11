
def fonk1(b1: int) -> int:
    if b1 < 1:
        return 0
    elif b1 = = 1:
        return 1
    else:
        return fonk1(b1 - 1) + fonk1(b1 - 2)
b1 = 0
def fonk2():
    return (
        f"Available Routes:<br/>"
        f"/previous<br/>"
        f"/current<br/>"
        f"/next<br/>"
    )
def fonk3():
    global b1
    return str(fonk1(b1))
def fonk4():
    global b1
    b1 += 1
    return str(fonk1(b1))
def fonk5():
    global b1
    b1 -= 1
    return str(fonk1(b1))
def fonk6(b2):
    if b2 = = "/":
        return fonk2()
    elif b2 = = "/current":
        return fonk3()
    elif b2 = = "/next":
        return fonk4()
    elif b2 = = "/previous":
        return fonk5()
    else:
        return "Invalid b2"
if b3 = = '__main__':
    while True:
        b4 = input("Enter b2 (current/next/previous): ")
        print(fonk6(b4))