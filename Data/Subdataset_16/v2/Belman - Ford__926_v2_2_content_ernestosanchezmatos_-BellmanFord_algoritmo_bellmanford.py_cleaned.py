import math
b1 = {
    "a": [math.inf, ""],
    "b": [math.inf, ""],
    "c": [math.inf, ""],
    "d": [math.inf, ""],
    "e": [math.inf, ""],
    "f": [math.inf, ""],
    "g": [math.inf, ""]
}
b2 = [
    ["a", "b", 9],
    ["a", "c", 2],
    ["b", "c", 6],
    ["b", "e", 1],
    ["c", "f", 9],
    ["d", "b", 3],
    ["d", "c", 2],
    ["d", "e", 5],
    ["d", "f", 6],
    ["e", "f", 3],
    ["e", "g", 7],
    ["f", "g", 4]
]
def fonk1(origen, destino, valor):
    if valor < b1[destino][0]:
        b1[destino][0] = valor
        b1[destino][1] = origen
        return True
    return False
def fonk2(b5, b6):
    b1[b5][0] = 0
    while True:
        b3 = False
        for origen, destino, peso in b2:
            if fonk1(origen, destino, b1[origen][0] + peso):
                b3 = False
            if fonk1(destino, origen, b1[destino][0] + peso):
                b3 = False
        if not b3:
            break
    b4 = [b6]
    while b4[-1] != b5:
        b4.append(b1[b4[-1]][1])
    return b4[::-1]
b5 = "a"
b6 = "g"
b7 = fonk2(b5, b6)
print(f"El camino más corto desde el punto '{b5}' al punto '{b6}' es: {b7}")