import rep
import b5
import copy
def fonk1(inicial, final, b13, verLista):
    b1 = inicial.copy()
    b2 = final.copy()
    if rep.mismoEstado(b1['estados'], b2['estados']):
        print('Estado Inicial es el estado Objetivo')
        quit()
    if len(b1['estados']) != len (b2['estados']):
        print('La cantidad de cubos de los estados es distinta, no es posible llegar a una soluciÃ³n')
        quit()
    b3 = []
    b4 = []
    b5 = []
    b3.append(copy.deepcopy(b1))
    while True:
        if rep.mismoEstado(b3[0]['estados'], b2['estados']):
            return b3[0]
        b3 = fonk2(b3, b4, b13, verLista)
        if len(b3) == 0:
            break
    print('No se logrÃ³ encontrar soluciÃ³n')
    quit()
def fonk2(b3, b4, b13, verLista):
    if len(b3) == 0:
        print('La busqueda no encontro soluciÃ³n')
        quit()
    b6 = len(b3)
    b7 = len(b4)
    b4.append(copy.deepcopy(b3[0]))
    b8 = copy.deepcopy(b3[0])
    b9 = []
    if verLista:
        print('------------------------')
        print('Q actual:')
        for estado in b3:
            print(estado['estadosAnteriores'][-1])
        print('------------------------')
    b10 = len(b8['estados'])
    for i in range(0, b10):
        b11 = copy.deepcopy(b8)
        if b8['estados'][i].toTableValid():
            b5.toTable(b11['estados'][i].nombre, b11)
            b9.append(copy.deepcopy(b11))
            b11 = copy.deepcopy(b8)
        for j in range(0, b10):
            if b8['estados'][i].tableToTowerValid(b8['estados'][j]):
                b5.tableToTower(b11['estados'][i].nombre, b8['estados'][j].nombre, b11)
                b9.append(copy.deepcopy(b11))
                b11 = copy.deepcopy(b8)
            if b8['estados'][i].towerToTowerValid(b8['estados'][j]):
                b5.towerToTower(b11['estados'][i].nombre, b8['estados'][j].nombre, b11)
                b9.append(copy.deepcopy(b11))
                b11 = copy.deepcopy(b8)
    b3.pop(0)
    b12 = copy.deepcopy(b9)
    b9 = fonk3(b4, b12)
    b3 = fonk3(b4, b3)
    if b13 = = 'bfs':
        b3 = b3 + b9
    else:
        b3 = b9 + b3
    b14 = len(b9)
    b9 = []
    print('Largo Q: ' + str(b6) + ' - Largo Nodos Nuevos: ' + str(b14) + ' - Largo Nodos Visitados: ' + str(b7))
    return b3
def fonk3(b4, b12):
    for dup in b4:
        for nuevo in b12:
            if rep.mismoEstado(dup['estados'], nuevo['estados']):
                b12.remove(nuevo)
    return b12