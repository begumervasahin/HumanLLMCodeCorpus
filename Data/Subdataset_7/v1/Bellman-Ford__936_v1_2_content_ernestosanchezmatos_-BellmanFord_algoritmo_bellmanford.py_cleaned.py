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
b3 = "a"
b4 = "g"
b1[b3][0] = 0
while True:
    b5 = True
    for i in b2:
        if fonk1(i[0], i[1], b1[i[0]][0] + i[2]):
            b5 = False
        if fonk1(i[1], i[0], b1[i[1]][0] + i[2]):
            b5 = False
    if b5:
        break
b6 = [b4]
while True:
    if b6[-1] == b3:
        break
    b6.append(b1[b6[-1]][1])
print("El b6 mas corto desde el punto '{}' y el punto '{}' es: {}".format(b3, b4, b6[::-1]))