from Grafo import Grafo
class AlgoritmoKruskal:
    def aplicar_kruskal(self, grafo):
        arbol = Grafo()
        nodos = grafo.getNombres()
        for nodo in nodos:
            arbol.ingresarNodo(nodo)
        aristas = grafo.getAristas()
        while aristas:
            arco_actual = aristas.pop(0)
            if not self.hay_ciclo(
                arbol,
                arco_actual,
                arbol.getNodo(arco_actual.getTerminal()),
                arco_actual.getTerminal()
            ):
                arbol.adicionarEnlace(arco_actual.getInicial(), arco_actual.getTerminal(), arco_actual.getPeso())
        return arbol
    def hay_ciclo(self, grafo, arco_verificar, terminal, origen):
        enlaces = terminal.getEnlaces()
        if not enlaces:
            return False
        if terminal.existeEnlace(arco_verificar.getInicial()) != -1:
            return True
        for enlace in enlaces:
            nodo_destino = enlace.getDestino()
            if nodo_destino != origen:
                if self.hay_ciclo(
                    grafo,
                    arco_verificar,
                    grafo.getNodo(nodo_destino),
                    terminal.getNombre()
                ):
                    return True
        return False