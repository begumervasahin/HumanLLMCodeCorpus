from AEstrela import AEstrela
from BestFirst import BestFirst
import logging
import minesweeper as mns
import sys
class class1:
    def fonk1(self):
        logging.basicConfig(b1 = 'minesweeperIa.log', level=logging.DEBUG,
                            b2 = '%(levelname)s %(funcName)s => %(message)s')
        self.b3 = self.fonk2()
    def fonk2(self):
        b4 = self.fonk3()
        if b4 = = 1:
            return AEstrela()
        elif b4 = = 2:
            return BestFirst()
    def fonk3(self):
        if len(sys.argv) > 1:
            return int(sys.argv[1])
        else:
            print('Algoritmos:\nA*:1\nBestFirst:2')
            return int(input('Selecione o Algoritmo(1 ou 2):'))
    def fonk4(self):
        b16, b5 = self.fonk5()
        b6 = [[' ' for _ in range(b16)] for _ in range(b16)]
        b7 = []
        b8 = []
        b9 = None
        b10 = True
        b11 = True
        b12 = self.b3.jogadaInicial()
        b13 = (b12.getX(), b12.getY())
        if not b7:
            b7, b14 = mns.setupgrid(b16, b13, b5)
        while b11:
            b15 = self.b3.definirJogada(b6)
            if b15 is None:
                print('Perdeu, a lista de abertos ficou vazia')
                b10 = False
                b11 = False
            else:
                b13 = (b15.getX(), b15.getY())
                print(b13, b15.getData())
                if b15.getData() == 'F':
                    b11 = mns.jogar(b13, b6, b7, b8, b14, flag=True)
                else:
                    b11 = mns.jogar(b13, b6, b7, b8, b14)
                    b9 = b15
        return b10
    def fonk5(self):
        if len(sys.argv) > 3:
            return int(sys.argv[2]), int(sys.argv[3])
        else:
            b16 = int(input('Selecione o tamanho do tabuleiro:'))
            b5 = int(input('Selecione o numero de bombas:'))
            return b16, b5
b17 = class1()
b17.fonk4()