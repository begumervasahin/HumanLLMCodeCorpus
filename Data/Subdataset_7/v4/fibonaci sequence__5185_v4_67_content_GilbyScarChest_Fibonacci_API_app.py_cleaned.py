from flask import Flask
b1 = Flask(b2)
a1 = 0
def fonk1(a1: int) -> int:
    if a1 < 1:
        return 0
    elif a1 = = 1:
        return 1
    else:
        return fonk1(a1 - 1) + fonk1(a1 - 2)
@b1.route("/")
def fonk2():
    return (
        "Available Routes:<br/>"
        "/previous<br/>"
        "/current<br/>"
        "/next<br/>"
    )
@b1.route("/current")
def fonk3():
    global a1
    return str(fonk1(a1))
@b1.route("/next")
def fonk4():
    global a1
    a1 += 1
    return str(fonk1(a1))
@b1.route("/previous")
def fonk5():
    global a1
    a1 -= 1
    return str(fonk1(a1))
if b2 = = '__main__':
    b1.run()