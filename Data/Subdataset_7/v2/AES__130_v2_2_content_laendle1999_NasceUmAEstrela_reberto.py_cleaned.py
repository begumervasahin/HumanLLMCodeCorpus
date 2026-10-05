import logging
import sys
import minesweeper as mns
from AEstrela import AEstrela
from BestFirst import BestFirst
class class1:
    def fonk1(self, b3):
        logging.basicConfig(b1 = 'minesweeperIa.log', level=logging.DEBUG,
                            b2 = '%(levelname)s %(funcName)s => %(message)s')
        if b3 = = 1:
            self.b4 = AEstrela()
        elif b3 = = 2:
            self.b4 = BestFirst()
    def fonk2(self, b15, b16):
        b5 = [[' ' for _ in range(b15)] for _ in range(b15)]
        b6 = []
        b7 = []
        b8 = True
        b9 = True
        b10 = None
        b11 = self.b4.jogadaInicial()
        b12 = (b11.getX(), b11.getY())
        if not b6:
            b6, b13 = mns.setupgrid(b15, b12, b16)
        while b9:
            b14 = self.b4.definirJogada(b5)
            if b14 is None:
                print('Perdeu, a lista de abertos ficou vazia')
                b8 = False
                b9 = False
            else:
                b12 = (b14.getX(), b14.getY())
                print(b12, b14.getData())
                if b14.getData() == 'F':
                    b9 = mns.jogar(b12, b5, b6, b7, b13, flag=True)
                else:
                    b9 = mns.jogar(b12, b5, b6, b7, b13)
                    b10 = b14
        return b8
if len(sys.argv) > 1:
    b3 = int(sys.argv[1])
    b15 = int(sys.argv[2])
    b16 = int(sys.argv[3])
else:
    print('Algoritmos:\nA*:1\nBestFirst:2')
    b3 = int(input('Selecione o Algoritmo(1 ou 2):'))
    b15 = int(input('Selecione o tamanho do tabuleiro:'))
    b16 = int(input('Selecione o numero de bombas:'))
b17 = class1(b3)
b17.fonk2(b15, b16)