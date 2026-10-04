from Grafo import Grafo
class AlgoritmoKruskal:
    def aplicar_kruskal(self, grafo):
        arbol = Grafo()
        nodos = grafo.getNombres()
        for nodo in nodos:
            arbol.ingresarNodo(nodo)
        aristas = grafo.getAristas()
        aristas.sort(key=lambda arco: arco.getPeso())
        for arco in aristas:
            nodo_inicial = arbol.getNodo(arco.getInicial())
            nodo_terminal = arbol.getNodo(arco.getTerminal())
            if not self.hay_ciclo(arbol, arco, nodo_terminal, nodo_inicial.getNombre()):
                arbol.adicionarEnlace(nodo_inicial.getNombre(), nodo_terminal.getNombre(), arco.getPeso())
        return arbol
    def hay_ciclo(self, grafo, arco_verificar, terminal, origen):
        enlaces = terminal.getEnlaces()
        if not enlaces:
            return False
        if terminal.existeEnlace(origen) != -1:
            return True
        for enlace in enlaces:
            nodo_destino = enlace.getDestino()
            if nodo_destino != origen:
                if self.hay_ciclo(grafo, arco_verificar, grafo.getNodo(nodo_destino), terminal.getNombre()):
                    return True
        return False
if __name__ == "__main__":
    grafo = Grafo()
    algoritmo_kruskal = AlgoritmoKruskal()
    mst = algoritmo_kruskal.aplicar_kruskal(grafo)
    print("Minimum Spanning Tree:", mst)