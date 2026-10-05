from collections import defaultdict
from heapq import heappop, heappush
def dijkstra(grafo, inicio, final):
    diccionario = defaultdict(list)
    for nodo, nodo_sgte, peso in grafo:
        diccionario[nodo].append((peso,nodo_sgte))
    cola = [(0,inicio,())]
    visitado = set()
    while cola:
        (costo, parado, ruta) = heappop(cola)
        if parado not in visitado:
            visitado.add(parado)
            ruta = (parado, ruta)
            if parado == final: return (costo,ruta)
            for peso, parado_sgte in diccionario.get(parado,()):
                if parado_sgte not in visitado:
                    heappush(cola,(costo + peso, parado_sgte, ruta))
    return float("infinito")
if __name__ == "__main__":
    grafo = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11),
        ("G", "H", 5)
    ]
print(dijkstra(grafo,"A","H"))