from Grafo import Grafo
class class1:
    def fonk1(self, b10):
        b1 = Grafo()
        b2 = b10.getNombres()
        for nodo in b2:
            b1.ingresarNodo(nodo)
        b3 = b10.getAristas()
        b3.sort(b4 = lambda arco: arco.getPeso())
        for arco in b3:
            b5 = b1.getNodo(arco.getInicial())
            b6 = b1.getNodo(arco.getTerminal())
            if not self.fonk2(b1, arco, b6, b5.getNombre()):
                b1.adicionarEnlace(b5.getNombre(), b6.getNombre(), arco.getPeso())
        return b1
    def fonk2(self, b10, arco_verificar, terminal, origen):
        b7 = terminal.getEnlaces()
        if not b7:
            return False
        if terminal.existeEnlace(origen) != -1:
            return True
        for enlace in b7:
            b8 = enlace.getDestino()
            if b8 != origen:
                if self.fonk2(b10, arco_verificar, b10.getNodo(b8), terminal.getNombre()):
                    return True
        return False
if b9 = = "__main__":
    b10 = Grafo()
    b11 = class1()
    b12 = b11.fonk1(b10)
    print("Minimum Spanning Tree:", b12)