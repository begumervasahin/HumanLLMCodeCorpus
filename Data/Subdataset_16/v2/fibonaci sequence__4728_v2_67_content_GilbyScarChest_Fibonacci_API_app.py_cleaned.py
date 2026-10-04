from flask import Flask
b1 = Flask(b3)
a1 = 0
def fonk1(b2: int) -> int:
    if b2 <= 0:
        return 0
    elif b2 = = 1:
        return 1
    else:
        return fonk1(b2 - 1) + fonk1(b2 - 2)
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
    return str(fonk1(a1))
@b1.route("/next")
def fonk4():
    global a1
    a1 += 1
    return str(fonk1(a1))
@b1.route("/previous")
def fonk5():
    global a1
    if a1 > 0:
        a1 -= 1
    return str(fonk1(a1))
if b3 = = "__main__":
    b1.run(b4 = True)