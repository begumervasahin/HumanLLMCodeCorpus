import logging
import minesweeper as mns
import sys
from AEstrela import AEstrela
from BestFirst import BestFirst
class Game:
    def __init__(self, ia):
        logging.basicConfig(filename='minesweeperIa.log', level=logging.DEBUG,
                            format='%(levelname)s %(funcName)s => %(message)s')
        if ia == 1:
            self.__ia = AEstrela()
        elif ia == 2:
            self.__ia = BestFirst()
    def play_game(self, gridsize, numberofmines):
        currgrid = [[' ' for _ in range(gridsize)] for _ in range(gridsize)]
        grid = []
        flags = []
        win = True
        game = True
        cellAnt = None
        cell = self.__ia.jogadaInicial()
        cellAbrir = (cell.getX(), cell.getY())
        if not grid:
            grid, mines = mns.setupgrid(gridsize, cellAbrir, numberofmines)
        while game:
            cell = self.__ia.definirJogada(currgrid)
            if cell is None:
                print('Perdeu, a lista de abertos ficou vazia')
                win = False
                game = False
            else:
                cellAbrir = (cell.getX(), cell.getY())
                print(cellAbrir, cell.getData())
                if cell.getData() == 'F':
                    game = mns.jogar(cellAbrir, currgrid, grid, flags, mines, flag=True)
                else:
                    game = mns.jogar(cellAbrir, currgrid, grid, flags, mines)
                    cellAnt = cell
        return win
if len(sys.argv) > 1:
    ia = int(sys.argv[1])
    gridsize = int(sys.argv[2])
    numberofmines = int(sys.argv[3])
else:
    print('Algoritmos:\nA*:1\nBestFirst:2')
    ia = int(input('Selecione o Algoritmo(1 ou 2):'))
    gridsize = int(input('Selecione o tamanho do tabuleiro:'))
    numberofmines = int(input('Selecione o numero de bombas:'))
mine = Game(ia)
mine.play_game(gridsize, numberofmines)