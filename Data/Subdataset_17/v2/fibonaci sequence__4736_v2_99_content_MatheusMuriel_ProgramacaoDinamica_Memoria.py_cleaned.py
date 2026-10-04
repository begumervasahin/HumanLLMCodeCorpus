class Cerebro:
    def __init__(self, limite, taxa_de_limpeza):
        self.memoria = {}
        self.usos = {}
        self.limite = limite
        self.taxa_de_limpeza = taxa_de_limpeza
    def nova_memoria(self, nome, valor):
        nome = str(nome)
        valor = int(valor)
        if len(self.memoria) >= self.limite:
            self.limpar_memoria(nome)
        self.memoria[nome] = valor
        self.usos[nome] = 1
    def get_lembranca(self, nome):
        if nome in self.memoria:
            self.usos[nome] += 1
            return self.memoria[nome]
        else:
            return -1
    def limpar_memoria(self, iteracao_atual):
        print("Chamada de limpeza na iteração", iteracao_atual)
        while len(self.memoria) > self.limite * self.taxa_de_limpeza:
            menor_registro = min(self.usos.items(), key=lambda x: x[1])
            self.memoria.pop(menor_registro[0])
            self.usos.pop(menor_registro[0])
if __name__ == "__main__":
    cerebro = Cerebro(limite=5, taxa_de_limpeza=0.7)
    cerebro.nova_memoria("1", 1)
    cerebro.nova_memoria("2", 1)
    cerebro.nova_memoria("3", 2)
    cerebro.nova_memoria("4", 3)
    cerebro.nova_memoria("5", 5)
    print(cerebro.get_lembranca("1"))
    cerebro.nova_memoria("6", 8)
    print(cerebro.get_lembranca("1"))
    print(cerebro.get_lembranca("6"))
