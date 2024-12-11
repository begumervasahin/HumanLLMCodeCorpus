import copy
def fonk1(inicial, final, b12, ver_lista):
    b1 = copy.deepcopy(inicial)
    b2 = copy.deepcopy(final)
    if mismo_estado(b1['estados'], b2['estados']):
        print('Estado Inicial es el estado Objetivo')
        quit()
    if len(b1['estados']) != len(b2['estados']):
        print('La cantidad de cubos de los estados es distinta, no es posible llegar a una solución')
        quit()
    b3 = [copy.deepcopy(b1)]
    b4 = []
    while True:
        if mismo_estado(b3[0]['estados'], b2['estados']):
            return b3[0]
        b3 = fonk2(b3, b4, b12, ver_lista)
        if len(b3) == 0:
            break
    print('No se logró encontrar solución')
    quit()
def fonk2(b3, b4, b12, ver_lista):
    if len(b3) == 0:
        print('La búsqueda no encontró solución')
        quit()
    b5 = len(b3)
    b6 = len(b4)
    b4.append(copy.deepcopy(b3[0]))
    b7 = copy.deepcopy(b3[0])
    b8 = []
    if ver_lista:
        print('------------------------')
        print('Q actual:')
        for estado in b3:
            print(estado['estadosAnteriores'][-1])
        print('------------------------')
    b9 = len(b7['estados'])
    for i in range(b9):
        b10 = copy.deepcopy(b7)
        if b7['estados'][i].toTableValid():
            operadores.toTable(b10['estados'][i].nombre, b10)
            b8.append(copy.deepcopy(b10))
            b10 = copy.deepcopy(b7)
        for j in range(b9):
            if b7['estados'][i].tableToTowerValid(b7['estados'][j]):
                operadores.tableToTower(b10['estados'][i].nombre, b7['estados'][j].nombre, b10)
                b8.append(copy.deepcopy(b10))
                b10 = copy.deepcopy(b7)
            if b7['estados'][i].towerToTowerValid(b7['estados'][j]):
                operadores.towerToTower(b10['estados'][i].nombre, b7['estados'][j].nombre, b10)
                b8.append(copy.deepcopy(b10))
                b10 = copy.deepcopy(b7)
    b3.pop(0)
    b11 = copy.deepcopy(b8)
    b8 = fonk3(b4, b11)
    b3 = fonk3(b4, b3)
    if b12 = = 'bfs':
        b3 += b8
    else:
        b3 = b8 + b3
    b13 = len(b8)
    b8 = []
    print('Largo Q: ' + str(b5) + ' - Largo Nodos Nuevos: ' + str(b13) + ' - Largo Nodos Visitados: ' + str(b6))
    return b3
def fonk3(b4, b11):
    return [nuevo for nuevo in b11 if not any(mismo_estado(dup['estados'], nuevo['estados']) for dup in b4)]