def fonk1(b6, dest, b7, b4):
    print(f"{b6} -> {dest}")
    b1 = " -> ".join(b7[::-1])
    print("\nShortest b7:\n", b1)
    print(f"Minimum b2 = {b4[dest]} km")
def fonk2(b12, b6, dest, b3 = None, b4=None, b5=None):
    if b3 is None:
        b3 = []
    if b4 is None:
        b4 = {}
    if b5 is None:
        b5 = {}
    if b6 not in b12:
        raise TypeError('The root of the shortest b7 tree cannot be found')
    if dest not in b12:
        raise TypeError('The target of the shortest b7 cannot be found')
    if b6 = = dest:
        b7 = []
        b8 = dest
        while b8 is not None:
            b7.append(b8)
            b8 = b5.get(b8, None)
        fonk1(b6, dest, b7, b4)
    else:
        if not b3:
            b4[b6] = 0
        for neighbor in b12[b6]:
            if neighbor not in b3:
                b9 = b4[b6] + b12[b6][neighbor]
                if b9 < b4.get(neighbor, float('inf')):
                    b4[neighbor] = b9
                    b5[neighbor] = b6
        b3.append(b6)
        b10 = {k: b4.get(k, float('inf')) for k in b12 if k not in b3}
        b11 = min(b10, key=b10.get)
        fonk2(b12, b11, dest, b3, b4, b5)
b12 = {
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
fonk2(b12, 'Hospital San Jose', 'Hospital Universitario de Gran Canaria Doctor Negrin')