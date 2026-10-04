def fonk1(t):
    return -0.48 * (t ** 3) + 36 * (t ** 2) - 760 * t + 4100
def fonk2(t):
    return -0.12 * t ** 4 + 12 * t ** 3 - 380 * t ** 2 + 4100 * t + 220
def fonk3(b1):
    return b1 * 3.6
def fonk4(inicio, final, incremento):
    a1 = 0
    a2 = 0
    for t in range(inicio, final + 1, incremento):
        b1 = fonk1(t)
        b2 = fonk2(t)
        b3 = fonk3(b1)
        if b2 > a1:
            a1 = b2
            a2 = t
        print("{:2}h   {:8.2f}m       {:6.2f}km/h".format(t, b2, b3))
    print(f"La altura máxima se alcanzó a las {a2} horas.")
    print(f"Esta altura máxima fue de {a1} metros.")
def fonk5():
    b4 = int(input("Ingrese el tiempo inicial para calcular la velocidad y la altitud para este globo climático: "))
    b5 = int(input("Ingrese el tiempo final: "))
    b6 = int(input("Ingrese el incremento de horas: "))
    while not (0 <= b4 < b5 <= 48):
        print("El tiempo inicial debe ser mayor o igual a cero y el tiempo final debe ser menor o igual a 48 horas.")
        b4 = int(input("Ingrese el tiempo inicial para calcular la velocidad y la altitud para este globo climático: "))
        b5 = int(input("Ingrese el tiempo final: "))
    fonk4(b4, b5, b6)
if b7 = = "__main__":
    fonk5()