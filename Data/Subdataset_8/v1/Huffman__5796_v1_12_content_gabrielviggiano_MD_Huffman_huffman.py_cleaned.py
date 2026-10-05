import os
from collections import Counter
class No:
    def __init__(self, conteudo, frequencia, bin, esquerda, direita):
        self.conteudo = conteudo
        self.frequencia = frequencia
        self.bin = bin
        self.esquerda = esquerda
        self.direita = direita
    def __repr__(self):
        return repr((self.conteudo, self.frequencia, self.bin))
    def isLeaf(self):
        return self.esquerda is None and self.direita is None
class Lista_Nos:
    def __init__(self, lista):
        self.texto = lista
    def inserirRaiz(self, novo):
        self.raiz = [novo]
        return
    def insereElemento(self, novo):
        for i in self.raiz:
            if i.conteudo == novo.conteudo:
                i.frequencia += 1
                self.raiz = sorted(self.raiz, key=lambda no: no.frequencia)
                return
        self.raiz += [novo]
        self.raiz = sorted(self.raiz, key=lambda no: no.frequencia)
    def criarLista(self):
        for l in self.texto:
            if self.raiz == 0:
                self.inserirRaiz(No(l, 1, '', None, None))
            else:
                self.insereElemento(No(l, 1, '', None, None))
        return
    def printarLista(self):
        for elem in self.raiz:
            print(elem)
        return
    def criarArvore(self):
        self.criarLista()
        while len(self.raiz) > 1:
            novo = No("", self.raiz[0].frequencia + self.raiz[1].frequencia, '', self.raiz[0], self.raiz[1])
            del self.raiz[0]
            del self.raiz[0]
            self.raiz += [novo]
            self.raiz = sorted(self.raiz, key=lambda no: no.frequencia)
        return
class ArvoreHuffman:
    def codificador(self, no):
        if no is None:
            return
        if no.esquerda is not None:
            no.esquerda.bin = no.bin + '1'
            self.codificador(no.esquerda)
        if no.direita is not None:
            no.direita.bin = no.bin + '0'
            self.codificador(no.direita)
        return
    def caracterBinario(self, arvore, l):
        bin = ''
        if arvore.conteudo == l:
            bin = arvore.bin
        if arvore.esquerda is not None:
            bin = self.caracterBinario(arvore.esquerda, l)
        if bin == '':
            if arvore.direita is not None:
                bin = self.caracterBinario(arvore.direita, l)
        return bin
    def textoBinario(self, arvore, texto):
        resultado = ''
        for l in texto:
            resultado += self.caracterBinario(arvore, l)
        return resultado
    def decodificador(self, arvore2, textoBinario):
        arvore = arvore2
        resultado = ''
        for bin in textoBinario:
            if bin == '1':
                if arvore.esquerda is not None:
                    arvore = arvore.esquerda
                    if arvore.esquerda is None and arvore.direita is None:
                        resultado += (arvore.conteudo)
                        arvore = arvore2
            else:
                if arvore.direita is not None:
                    arvore = arvore.direita
                    if arvore.esquerda is None and arvore.direita is None:
                        resultado += (arvore.conteudo)
                        arvore = arvore2
        return resultado
    def tabelinha(self, no):
        if no is None:
            return
        if no.esquerda is not None:
            self.tabelinha(no.esquerda)
        if no.isLeaf():
            print(no)
        if no.direita is not None:
            self.tabelinha(no.direita)
        return
def carregar_frequencias(lista):
    frequencias = Counter(lista)
    return frequencias
def openFile(nome_arq):
    if not os.path.isfile(nome_arq):
        print("Arquivo não encontrado!")
        exit()
    else:
        with open(nome_arq, "r") as arquivo:
            texto = arquivo.read()
        return texto
def createFile(nome_arq, texto):
    try:
        file = open(nome_arq, 'w')
        file.write(texto)
        file.close()
    except IOError:
        raise print("Erro ao criar o arquivo!")
def main(args):
    print("PARA INICIAR O PROGRAMA, INSIRA O NOME DO ARQUIVO EM QUE A PALAVRA A SER COMPRIMIDA SE ENCONTRA")
    nome_arq = input("Nome: ")
    palavra = openFile(nome_arq)
    lista = list(openFile(nome_arq))
    huffman = ArvoreHuffman()
    lista_Nos = Lista_Nos(lista)
    lista_Nos.criarArvore()
    huffman.codificador(lista_Nos.raiz[0])
    print("--------------------- EXECUÇÃO DO CODIGO DE HUFFMAN ---------------------")
    print("Palavra inserida:", palavra)
    print("")
    print("Frequencia dos caracteres:")
    freqs = carregar_frequencias(lista)
    print(freqs)
    print("")
    print("Arvore criada com sucesso!")
    print("")
    print("Tabela de huffman:")
    huffman.tabelinha(lista_Nos.raiz[0])
    print("")
    codigo = huffman.textoBinario(lista_Nos.raiz[0], lista_Nos.texto)
    print("Palavra comprimida para binário:", codigo)
    print("")
    recodigo = huffman.decodificador(lista_Nos.raiz[0], huffman.textoBinario(lista_Nos.raiz[0], lista_Nos.texto))
    print("Palavra descomprimida:", recodigo)
    print("")
    createFile("resultado.txt", ("Palavra Inserida:" + palavra + "\n" +
                                 "Palavra Comprimida: " + codigo + "\n" +
                                 "Palavra Descomprimida: " + recodigo + "\n"
    ))
    print("Arquivo de saida gerado com sucesso!")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))