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
def set_valores(origen, destino, valor):
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
    for origen, destino, peso in caminos:
        if set_valores(origen, destino, valores[origen][0] + peso):
            cancel = False
        if set_valores(destino, origen, valores[destino][0] + peso):
            cancel = False
    if cancel:
        break
camino = [final]
while camino[-1] != inicio:
    camino.append(valores[camino[-1]][1])
print("El camino más corto desde el punto '{}' al punto '{}' es: {}".format(inicio, final, camino[::-1]))