import copy
def buscar_solucion(inicial, final, tipo_busqueda, ver_lista):
    estado_inicial = copy.deepcopy(inicial)
    estado_final = copy.deepcopy(final)
    if mismo_estado(estado_inicial['estados'], estado_final['estados']):
        print('Estado Inicial es el estado Objetivo')
        quit()
    if len(estado_inicial['estados']) != len(estado_final['estados']):
        print('La cantidad de cubos de los estados es distinta, no es posible llegar a una solución')
        quit()
    cola = [copy.deepcopy(estado_inicial)]
    visitados = []
    while True:
        if mismo_estado(cola[0]['estados'], estado_final['estados']):
            return cola[0]
        cola = busqueda(cola, visitados, tipo_busqueda, ver_lista)
        if len(cola) == 0:
            break
    print('No se logró encontrar solución')
    quit()
def busqueda(cola, visitados, tipo_busqueda, ver_lista):
    if len(cola) == 0:
        print('La búsqueda no encontró solución')
        quit()
    largo_q = len(cola)
    largo_v = len(visitados)
    visitados.append(copy.deepcopy(cola[0]))
    estado_actual = copy.deepcopy(cola[0])
    nodos_encontrados = []
    if ver_lista:
        print('------------------------')
        print('Q actual:')
        for estado in cola:
            print(estado['estadosAnteriores'][-1])
        print('------------------------')
    n_cubos = len(estado_actual['estados'])
    for i in range(n_cubos):
        estado_aux = copy.deepcopy(estado_actual)
        if estado_actual['estados'][i].toTableValid():
            operadores.toTable(estado_aux['estados'][i].nombre, estado_aux)
            nodos_encontrados.append(copy.deepcopy(estado_aux))
            estado_aux = copy.deepcopy(estado_actual)
        for j in range(n_cubos):
            if estado_actual['estados'][i].tableToTowerValid(estado_actual['estados'][j]):
                operadores.tableToTower(estado_aux['estados'][i].nombre, estado_actual['estados'][j].nombre, estado_aux)
                nodos_encontrados.append(copy.deepcopy(estado_aux))
                estado_aux = copy.deepcopy(estado_actual)
            if estado_actual['estados'][i].towerToTowerValid(estado_actual['estados'][j]):
                operadores.towerToTower(estado_aux['estados'][i].nombre, estado_actual['estados'][j].nombre, estado_aux)
                nodos_encontrados.append(copy.deepcopy(estado_aux))
                estado_aux = copy.deepcopy(estado_actual)
    cola.pop(0)
    nuevos = copy.deepcopy(nodos_encontrados)
    nodos_encontrados = borrar_duplicados(visitados, nuevos)
    cola = borrar_duplicados(visitados, cola)
    if tipo_busqueda == 'bfs':
        cola += nodos_encontrados
    else:
        cola = nodos_encontrados + cola
    largo_n = len(nodos_encontrados)
    nodos_encontrados = []
    print('Largo Q: ' + str(largo_q) + ' - Largo Nodos Nuevos: ' + str(largo_n) + ' - Largo Nodos Visitados: ' + str(largo_v))
    return cola
def borrar_duplicados(visitados, nuevos):
    return [nuevo for nuevo in nuevos if not any(mismo_estado(dup['estados'], nuevo['estados']) for dup in visitados)]