from Grafo import Grafo
class class1():
    def fonk1(self, grafo):
        b1 = Grafo()
        b2 = grafo.getNombres()
        for n in b2:
            b1.ingresarNodo(n)
        b3 = grafo.getAristas()
        while b3:
            b4 = b3[0]
            if (self.fonk2(b1,
                              b4,
                              b1.getNodo(b4.getTerminal()),
                              b4.getTerminal()) == False):
                b1.adicionarEnlace(b4.getInicial(), b4.getTerminal(), b4.getPeso())
            del b3[0]
        return b1
    def fonk2(self, g, aVerificar, terminal,  m):
        b5 = terminal.getEnlaces()
        if len(b5) == 0:
            return False
        if terminal.existeEnlace(aVerificar.getInicial()) != -1:
            return True
        for n in b5:
            b6 = n
            if b6.getDestino() != m:
                if self.fonk2(g,
                                aVerificar,
                                g.getNodo(b6.getDestino()),
                                terminal.getNombre()):
                    return True
        return False