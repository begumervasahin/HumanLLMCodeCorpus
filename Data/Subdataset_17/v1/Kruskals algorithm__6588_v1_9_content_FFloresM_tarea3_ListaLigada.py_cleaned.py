class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.sig = None
    def get_dato(self):
        return self.dato
    def get_sig(self):
        return self.sig
    def set_dato(self, newdato):
        self.dato = newdato
    def set_sig(self, newsig):
        self.sig = newsig
class ListaLigada:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def agregar(self, item):
        temp = Nodo(item)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            self.tail.set_sig(temp)
            self.tail = temp
    def size(self):
        actual = self.head
        count = 0
        while actual is not None:
            count += 1
            actual = actual.get_sig()
        return count
    def buscar(self, item):
        actual = self.head
        found = False
        while actual is not None and not found:
            if actual.get_dato() == item:
                found = True
            else:
                actual = actual.get_sig()
        return found
    def eliminar(self, item):
        actual = self.head
        prev = None
        found = False
        while actual is not None and not found:
            if actual.get_dato() == item:
                found = True
            else:
                prev = actual
                actual = actual.get_sig()
        if found:
            if prev is None:
                self.head = actual.get_sig()
            else:
                prev.set_sig(actual.get_sig())
            if actual == self.tail:
                self.tail = prev
    def mostrar(self):
        actual = self.head
        while actual is not None:
            print(actual.get_dato(), end='')
            actual = actual.get_sig()
            if actual is not None:
                print(" -> ", end="")
        print()
if __name__ == "__main__":
    lista = ListaLigada()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.mostrar()
    print("Size:", lista.size())
    print("Buscar 2:", lista.buscar(2))
    print("Buscar 5:", lista.buscar(5))
    lista.eliminar(2)
    lista.mostrar()
