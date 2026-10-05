class Cerebro:
    def __init__(self, limite_memoria, taxa_limpeza):
        self.memoria = {}
        self.usos = {}
        self.limite_memoria = limite_memoria
        self.taxa_limpeza = taxa_limpeza
    def nova_memoria(self, nome, valor):
        nome = str(nome)
        valor = int(valor)
        if len(self.memoria) >= self.limite_memoria:
            self.limpar_memoria()
        self.memoria[nome] = valor
        self.usos[nome] = 1
    def get_lembranca(self, nome):
        if nome in self.memoria:
            self.usos[nome] += 1
            return self.memoria[nome]
        else:
            return -1
    def limpar_memoria(self):
        print("Chamada de limpeza")
        while len(self.memoria) > self.limite_memoria * self.taxa_limpeza:
            menor_registro = min(self.usos.items(), key=lambda x: x[1])
            self.memoria.pop(menor_registro[0])
            self.usos.pop(menor_registro[0])
cerebro = Cerebro(limite_memoria=100, taxa_limpeza=0.5)
cerebro.nova_memoria("A", 10)
cerebro.nova_memoria("B", 20)
print(cerebro.get_lembranca("A"))
print(cerebro.get_lembranca("C"))