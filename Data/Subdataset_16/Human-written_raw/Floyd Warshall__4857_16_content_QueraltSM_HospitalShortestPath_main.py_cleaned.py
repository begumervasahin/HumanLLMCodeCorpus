def fonk1(b4,dest,b5,distances):
    print str(b4)+" -> "+str(dest)
    b1 = ""
    for hospital in b5:
        b1 += hospital+" -> "
    print "\nShortest b5:\n", b1[:-3]
    print "Minimum b2 = "+str(distances[dest])+" km"
def fonk2(b10,b4,dest,b3 = [],distances={},predecessors={}):
    if b4 not in b10:
        raise TypeError('The root of the shortest b5 tree cannot be found')
    if dest not in b10:
        raise TypeError('The target of the shortest b5 cannot be found')
    if b4 = = dest:
        b5 = []
        b6 = dest
        while b6 != None:
            b5.append(b6)
            b6 = predecessors.get(b6,None)
        fonk1(b4,dest,b5,distances)
    else :
        if not b3:
            distances[b4]=0
        for neighbor in b10[b4] :
            if neighbor not in b3:
                b7 = distances[b4] + b10[b4][neighbor]
                if b7 < distances.get(neighbor,float('inf')):
                    distances[neighbor] = b7
                    predecessors[neighbor] = b4
        b3.append(b4)
        b8 = {}
        for k in b10:
            if k not in b3:
                b8[k] = distances.get(k,float('inf'))
        b9 = min(b8, key=b8.get)
        fonk2(b10,b9,dest,b3,distances,predecessors)
b10 = {
        'Hospital Universitario de Gran Canaria Doctor Negrin':
        {'Clinica Centro - Las Palmas': 2.5,
        'Clinica del Carmen':3.1,
        'Hospital Pediatrico Dr. Agustin Zubillaga': 1.3},
        'Clinica Centro - Las Palmas':
        {'Hospital Universitario de Gran Canaria Doctor Negrin': 2.5,
        'Hospital San Jose': 2,
        'Hospitales San Roque': 0.8,
        'Hospitales La Paloma': 3.7},
        'Hospital Pediatrico Dr. Agustin Zubillaga':
        {'Hospital Universitario de Gran Canaria Doctor Negrin': 1.3,
        'Hospitales La Paloma': 3.3},
        'Clinica del Carmen':
        {'Hospital Universitario de Gran Canaria Doctor Negrin': 3.1,
        'Hospital Vithas Santa Catalina': 1.2},
        'Hospital Vithas Santa Catalina':
        {'Clinica del Carmen':1.2,
        'Hospital La Paloma':0.25,
        'HPS - Hospital Perpetuo Socorro':4.1},
        'Hospital La Paloma':
        {'Hospital Pediatrico Dr. Agustin Zubillaga': 3.3,
        'Clinica Centro - Las Palmas': 3.7,
        'Hospital Vithas Santa Catalina': 0.25},
        'Hospitales San Roque':
        {'HPS - Hospital Perpetuo Socorro':1.7,
        'Clinica Centro - Las Palmas':0.8},
        'HPS - Hospital Perpetuo Socorro':
        {'Hospital San Jose':0.85,
        'Hospitales San Roque':1.7,
        'Hospital Vithas Santa Catalina':4.1},
        'Hospital San Jose':
        {'Clinica Centro - Las Palmas':2,
        'HPS - Hospital Perpetuo Socorro':0.85}}
fonk2(b10,'Hospital San Jose','Hospital Universitario de Gran Canaria Doctor Negrin')