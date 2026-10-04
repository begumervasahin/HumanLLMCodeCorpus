def fonk1(b8, b10, b9, b4):
    print(f"{b8} -> {b10}")
    b1 = " -> ".join(b9[::-1])
    print("\nShortest b9:\n", b1)
    print(f"Minimum b2 = {b4[b10]} km")
def fonk2(b11, b8, b10):
    b3 = []
    b4 = {}
    b5 = {}
    if b8 not in b11:
        raise ValueError('The root of the shortest b9 tree cannot be found')
    if b10 not in b11:
        raise ValueError('The target of the shortest b9 cannot be found')
    b4[b8] = 0
    while b8:
        for neighbor, distance in b11[b8].items():
            if neighbor not in b3:
                b6 = b4[b8] + distance
                if b6 < b4.get(neighbor, float('inf')):
                    b4[neighbor] = b6
                    b5[neighbor] = b8
        b3.append(b8)
        b7 = {node: b4.get(node, float('inf')) for node in b11 if node not in b3}
        b8 = min(b7, key=b7.get, default=None)
    if b10 in b4:
        b9 = []
        while b10 is not None:
            b9.append(b10)
            b10 = b5.get(b10)
        fonk1(b9[-1], b9[0], b9, b4)
    else:
        print(f"No b9 found from {b9[-1]} to {b9[0]}")
b11 = {
    'Hospital Universitario de Gran Canaria Doctor Negrin': {
        'Clinica Centro - Las Palmas': 2.5,
        'Clinica del Carmen': 3.1,
        'Hospital Pediatrico Dr. Agustin Zubillaga': 1.3
    },
    'Clinica Centro - Las Palmas': {
        'Hospital Universitario de Gran Canaria Doctor Negrin': 2.5,
        'Hospital San Jose': 2,
        'Hospitales San Roque': 0.8,
        'Hospitales La Paloma': 3.7
    },
    'Hospital Pediatrico Dr. Agustin Zubillaga': {
        'Hospital Universitario de Gran Canaria Doctor Negrin': 1.3,
        'Hospitales La Paloma': 3.3
    },
    'Clinica del Carmen': {
        'Hospital Universitario de Gran Canaria Doctor Negrin': 3.1,
        'Hospital Vithas Santa Catalina': 1.2
    },
    'Hospital Vithas Santa Catalina': {
        'Clinica del Carmen': 1.2,
        'Hospital La Paloma': 0.25,
        'HPS - Hospital Perpetuo Socorro': 4.1
    },
    'Hospital La Paloma': {
        'Hospital Pediatrico Dr. Agustin Zubillaga': 3.3,
        'Clinica Centro - Las Palmas': 3.7,
        'Hospital Vithas Santa Catalina': 0.25
    },
    'Hospitales San Roque': {
        'HPS - Hospital Perpetuo Socorro': 1.7,
        'Clinica Centro - Las Palmas': 0.8
    },
    'HPS - Hospital Perpetuo Socorro': {
        'Hospital San Jose': 0.85,
        'Hospitales San Roque': 1.7,
        'Hospital Vithas Santa Catalina': 4.1
    },
    'Hospital San Jose': {
        'Clinica Centro - Las Palmas': 2,
        'HPS - Hospital Perpetuo Socorro': 0.85
    }
}
fonk2(b11, 'Hospital San Jose', 'Hospital Universitario de Gran Canaria Doctor Negrin')