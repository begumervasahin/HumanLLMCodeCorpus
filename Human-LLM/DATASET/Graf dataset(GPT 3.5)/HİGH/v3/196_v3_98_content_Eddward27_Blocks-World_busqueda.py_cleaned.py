import copy
def fonk1(b1, state2):
    return b1 = = state2
def fonk2(inicial, final, b13, ver_lista):
    b2 = copy.deepcopy(inicial)
    b3 = copy.deepcopy(final)
    if fonk1(b2['estados'], b3['estados']):
        print('Estado Inicial es el estado Objetivo')
        quit()
    if len(b2['estados']) != len(b3['estados']):
        print('La cantidad de cubos de los estados es distinta, no es posible llegar a una solución')
        quit()
    b4 = [copy.deepcopy(b2)]
    b5 = []
    while b4:
        if fonk1(b4[0]['estados'], b3['estados']):
            return b4[0]
        b4 = fonk3(b4, b5, b13, ver_lista)
    print('No se logró encontrar solución')
    quit()
def fonk3(b4, b5, b13, ver_lista):
    if not b4:
        print('La búsqueda no encontró solución')
        quit()
    b6 = len(b4)
    b7 = len(b5)
    b8 = copy.deepcopy(b4[0])
    b5.append(copy.deepcopy(b8))
    b4.pop(0)
    b9 = []
    if ver_lista:
        print('------------------------')
        print('Q actual:')
        for estado in b4:
            print(estado['estadosAnteriores'][-1])
        print('------------------------')
    b10 = len(b8['estados'])
    for i in range(b10):
        b11 = copy.deepcopy(b8)
        if b8['estados'][i].toTableValid():
            operadores.toTable(b11['estados'][i].nombre, b11)
            b9.append(copy.deepcopy(b11))
            b11 = copy.deepcopy(b8)
        for j in range(b10):
            if b8['estados'][i].tableToTowerValid(b8['estados'][j]):
                operadores.tableToTower(b11['estados'][i].nombre, b8['estados'][j].nombre, b11)
                b9.append(copy.deepcopy(b11))
                b11 = copy.deepcopy(b8)
            if b8['estados'][i].towerToTowerValid(b8['estados'][j]):
                operadores.towerToTower(b11['estados'][i].nombre, b8['estados'][j].nombre, b11)
                b9.append(copy.deepcopy(b11))
                b11 = copy.deepcopy(b8)
    b12 = copy.deepcopy(b9)
    b9 = fonk4(b5, b12)
    b4 = fonk4(b5, b4)
    if b13 = = 'bfs':
        b4 += b9
    else:
        b4 = b9 + b4
    b14 = len(b9)
    b9 = []
    print('Largo Q: ' + str(b6) + ' - Largo Nodos Nuevos: ' + str(b14) + ' - Largo Nodos Visitados: ' + str(b7))
    return b4
def fonk4(b5, b12):
    return [nuevo for nuevo in b12 if not any(fonk1(dup['estados'], nuevo['estados']) for dup in b5)]