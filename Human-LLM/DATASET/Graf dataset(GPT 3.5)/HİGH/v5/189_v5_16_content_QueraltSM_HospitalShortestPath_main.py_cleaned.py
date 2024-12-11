def fonk1(source, destination, b7, b4):
    print(f"{source} -> {destination}")
    b1 = " -> ".join(b7)
    print("\nShortest b7:\n", b1)
    print(f"Minimum b2 = {b4[destination]} km")
def fonk2(b13, source, destination):
    if source not in b13:
        raise ValueError('Source node is not in the b13')
    if destination not in b13:
        raise ValueError('Destination node is not in the b13')
    b3 = []
    b4 = {source: 0}
    b5 = {}
    fonk3(b13, source, destination, b3, b4, b5)
    fonk4(source, destination, b4, b5)
def fonk3(b13, b6, destination, b3, b4, b5):
    if b6 = = destination:
        b7 = []
        b8 = destination
        while b8 is not None:
            b7.append(b8)
            b8 = b5.get(b8)
        return b7[::-1]
    b3.append(b6)
    for neighbor, weight in b13[b6].items():
        if neighbor not in b3:
            b9 = b4[b6] + weight
            if b9 < b4.get(neighbor, float('inf')):
                b4[neighbor] = b9
                b5[neighbor] = b6
    b10 = {k: b4.get(k, float('inf')) for k in b13 if k not in b3}
    b11 = min(b10, key=b10.get)
    return fonk3(b13, b11, destination, b3, b4, b5)
def fonk4(source, destination, b4, b5):
    b7 = []
    b8 = destination
    while b8 is not None:
        b7.append(b8)
        b8 = b5.get(b8)
    fonk1(source, destination, b7[::-1], b4)
if b12 = = "__main__":
    b13 = {
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
    fonk2(b13, 'Hospital San Jose', 'Hospital Universitario de Gran Canaria Doctor Negrin')