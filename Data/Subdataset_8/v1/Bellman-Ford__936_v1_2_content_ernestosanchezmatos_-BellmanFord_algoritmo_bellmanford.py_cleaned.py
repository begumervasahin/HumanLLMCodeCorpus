import math
valores = {
    "a": [math.inf, ""],
    "b": [math.inf, ""],
    "c": [math.inf, ""],
    "d": [math.inf, ""],
    "e": [math.inf, ""],
    "f": [math.inf, ""],
    "g": [math.inf, ""]
}
caminos = [
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
def setValores(origen, destino, valor):
    if valor < valores[destino][0]:
        valores[destino][0] = valor
        valores[destino][1] = origen
        return True
    return False
inicio = "a"
final = "g"
valores[inicio][0] = 0
while True:
    cancel = True
    for i in caminos:
        if setValores(i[0], i[1], valores[i[0]][0] + i[2]):
            cancel = False
        if setValores(i[1], i[0], valores[i[1]][0] + i[2]):
            cancel = False
    if cancel:
        break
camino = [final]
while True:
    if camino[-1] == inicio:
        break
    camino.append(valores[camino[-1]][1])
print("El camino mas corto desde el punto '{}' y el punto '{}' es: {}".format(inicio, final, camino[::-1]))