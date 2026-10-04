import math
b1 = ["a", "b", "c", "d", "e", "f", "g"]
b2 = {node: [math.inf, ""] for node in b1}
b3 = [
    ("a", "b", 9),
    ("a", "c", 2),
    ("b", "c", 6),
    ("b", "e", 1),
    ("c", "f", 9),
    ("d", "b", 3),
    ("d", "c", 2),
    ("d", "e", 5),
    ("d", "f", 6),
    ("e", "f", 3),
    ("e", "g", 7),
    ("f", "g", 4)
]
def fonk1(origen, destino, valor):
    if valor < b2[destino][0]:
        b2[destino][0] = valor
        b2[destino][1] = origen
        return True
    return False
def fonk2(b6, b7):
    b2[b6][0] = 0
    while True:
        b4 = False
        for origen, destino, peso in b3:
            if fonk1(origen, destino, b2[origen][0] + peso):
                b4 = True
            if fonk1(destino, origen, b2[destino][0] + peso):
                b4 = True
        if not b4:
            break
    b5 = [b7]
    while b5[-1] != b6:
        b5.append(b2[b5[-1]][1])
    return b5[::-1]
def fonk3():
    b6 = "a"
    b7 = "g"
    b8 = fonk2(b6, b7)
    print(f"El camino más corto desde el punto '{b6}' al punto '{b7}' es: {b8}")
if b9 = = "__main__":
    fonk3()