from Grafo import Grafo
class class1:
    def fonk1(self, grafo):
        b1 = Grafo()
        b2 = grafo.getNombres()
        for nodo in b2:
            b1.ingresarNodo(nodo)
        b3 = grafo.getAristas()
        while b3:
            b4 = b3.pop(0)
            if not self.fonk2(
                b1,
                b4,
                b1.getNodo(b4.getTerminal()),
                b4.getTerminal()
            ):
                b1.adicionarEnlace(b4.getInicial(), b4.getTerminal(), b4.getPeso())
        return b1
    def fonk2(self, grafo, arco_verificar, terminal, origen):
        b5 = terminal.getEnlaces()
        if not b5:
            return False
        if terminal.existeEnlace(arco_verificar.getInicial()) != -1:
            return True
        for enlace in b5:
            b6 = enlace.getDestino()
            if b6 != origen:
                if self.fonk2(
                    grafo,
                    arco_verificar,
                    grafo.getNodo(b6),
                    terminal.getNombre()
                ):
                    return True
        return False