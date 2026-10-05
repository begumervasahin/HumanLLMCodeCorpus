import rep
import operadores
import copy
def buscarSolucion(inicial, final, tipoBusqueda, verLista):
    estadoInicial = inicial.copy()
    estadoFinal = final.copy()
    if rep.mismoEstado(estadoInicial['estados'], estadoFinal['estados']):
        print('Estado Inicial es el estado Objetivo')
        quit()
    if len(estadoInicial['estados']) != len (estadoFinal['estados']):
        print('La cantidad de cubos de los estados es distinta, no es posible llegar a una soluciÃ³n')
        quit()
    cola = []
    visitados = []
    operadores = []
    cola.append(copy.deepcopy(estadoInicial))
    while True:
        if rep.mismoEstado(cola[0]['estados'], estadoFinal['estados']):
            return cola[0]
        cola = busqueda(cola, visitados, tipoBusqueda, verLista)
        if len(cola) == 0:
            break
    print('No se logrÃ³ encontrar soluciÃ³n')
    quit()
def busqueda(cola, visitados, tipoBusqueda, verLista):
    if len(cola) == 0:
        print('La busqueda no encontro soluciÃ³n')
        quit()
    largoQ = len(cola)
    largoV = len(visitados)
    visitados.append(copy.deepcopy(cola[0]))
    estadoActual = copy.deepcopy(cola[0])
    nodosEncontrados = []
    if verLista:
        print('------------------------')
        print('Q actual:')
        for estado in cola:
            print(estado['estadosAnteriores'][-1])
        print('------------------------')
    nCubos = len(estadoActual['estados'])
    for i in range(0, nCubos):
        estadoAux = copy.deepcopy(estadoActual)
        if estadoActual['estados'][i].toTableValid():
            operadores.toTable(estadoAux['estados'][i].nombre, estadoAux)
            nodosEncontrados.append(copy.deepcopy(estadoAux))
            estadoAux = copy.deepcopy(estadoActual)
        for j in range(0, nCubos):
            if estadoActual['estados'][i].tableToTowerValid(estadoActual['estados'][j]):
                operadores.tableToTower(estadoAux['estados'][i].nombre, estadoActual['estados'][j].nombre, estadoAux)
                nodosEncontrados.append(copy.deepcopy(estadoAux))
                estadoAux = copy.deepcopy(estadoActual)
            if estadoActual['estados'][i].towerToTowerValid(estadoActual['estados'][j]):
                operadores.towerToTower(estadoAux['estados'][i].nombre, estadoActual['estados'][j].nombre, estadoAux)
                nodosEncontrados.append(copy.deepcopy(estadoAux))
                estadoAux = copy.deepcopy(estadoActual)
    cola.pop(0)
    nuevos = copy.deepcopy(nodosEncontrados)
    nodosEncontrados = borrarDuplicados(visitados, nuevos)
    cola = borrarDuplicados(visitados, cola)
    if tipoBusqueda == 'bfs':
        cola = cola + nodosEncontrados
    else:
        cola = nodosEncontrados + cola
    largoN = len(nodosEncontrados)
    nodosEncontrados = []
    print('Largo Q: ' + str(largoQ) + ' - Largo Nodos Nuevos: ' + str(largoN) + ' - Largo Nodos Visitados: ' + str(largoV))
    return cola
def borrarDuplicados(visitados, nuevos):
    for dup in visitados:
        for nuevo in nuevos:
            if rep.mismoEstado(dup['estados'], nuevo['estados']):
                nuevos.remove(nuevo)
    return nuevos