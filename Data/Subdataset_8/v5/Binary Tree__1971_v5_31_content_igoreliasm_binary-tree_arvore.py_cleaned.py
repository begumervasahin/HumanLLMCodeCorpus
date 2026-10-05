from no import No
class Arvore:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0
    def __setitem__(self, chave, valor):
        self.inserir(chave, valor)
    def __delitem__(self, chave):
        self.deletar(chave)
    def __len__(self):
        return self.tamanho
    def __getitem__(self, chave):
        return self.get(chave)
    def __contains__(self, chave):
        return bool(self._get(chave, self.raiz))
    def quantidade(self):
        return self.tamanho
    def inserir(self, chave, val):
        if self.raiz:
            self._inserir(chave, val, self.raiz)
        else:
            self.raiz = No(chave, val)
        self.tamanho += 1
    def _inserir(self, chave, val, noCorrente):
        if chave < noCorrente.chave:
            if noCorrente.temFilhoEsquerda():
                self._inserir(chave, val, noCorrente.esquerda)
            else:
                noCorrente.esquerda = No(chave, val, pai=noCorrente)
        else:
            if noCorrente.temFilhoDireita():
                self._inserir(chave, val, noCorrente.direita)
            else:
                noCorrente.direita = No(chave, val, pai=noCorrente)
    def get(self, chave):
        noCorrente = self._get(chave, self.raiz)
        return noCorrente.carga if noCorrente else None
    def _get(self, chave, noCorrente):
        while noCorrente:
            if chave == noCorrente.chave:
                return noCorrente
            elif chave < noCorrente.chave:
                noCorrente = noCorrente.esquerda
            else:
                noCorrente = noCorrente.direita
        return None
    def deletar(self, chave):
        noParaDeletar = self._get(chave, self.raiz)
        if not noParaDeletar:
            raise KeyError('Chave não encontrada na árvore atual')
        self.remover(noParaDeletar)
        self.tamanho -= 1
    def esvaziar(self):
        self.raiz = None
        self.tamanho = 0
        print("Sua árvore está vazia!")
    def buscarSucessor(self):
        if self.temFilhoDireita():
            return self.direita.chaveMinima()
        else:
            pai = self.pai
            while pai and self == pai.direita:
                self = pai
                pai = pai.pai
            return pai
    def chaveMinima(self):
        corrente = self
        while corrente.esquerda:
            corrente = corrente.esquerda
        return corrente
    def remover(self, noCorrente):
        if noCorrente.ehFolha():
            if noCorrente.pai:
                if noCorrente == noCorrente.pai.esquerda:
                    noCorrente.pai.esquerda = None
                else:
                    noCorrente.pai.direita = None
        elif noCorrente.temTodosFilhos():
            sucessor = noCorrente.buscarSucessor()
            sucessor.removerSucessor()
            noCorrente.chave = sucessor.chave
            noCorrente.carga = sucessor.carga
        else:
            filho = noCorrente.esquerda if noCorrente.temFilhoEsquerda() else noCorrente.direita
            if noCorrente.ehFilhoEsquerda():
                noCorrente.pai.esquerda = filho
            else:
                noCorrente.pai.direita = filho
            filho.pai = noCorrente.pai