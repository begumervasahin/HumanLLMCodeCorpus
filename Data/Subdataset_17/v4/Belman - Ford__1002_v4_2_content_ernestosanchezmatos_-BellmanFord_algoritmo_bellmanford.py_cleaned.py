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
def find_shortest_path(inicio, final):
    valores[inicio][0] = 0
    while True:
        updated = False
        for origen, destino, peso in caminos:
            if set_valores(origen, destino, valores[origen][0] + peso):
                updated = True
            if set_valores(destino, origen, valores[destino][0] + peso):
                updated = True
        if not updated:
            break
    path = [final]
    while path[-1] != inicio:
        path.append(valores[path[-1]][1])
    return path[::-1]
inicio = "a"
final = "g"
shortest_path = find_shortest_path(inicio, final)
print(f"El camino más corto desde el punto '{inicio}' al punto '{final}' es: {shortest_path}")