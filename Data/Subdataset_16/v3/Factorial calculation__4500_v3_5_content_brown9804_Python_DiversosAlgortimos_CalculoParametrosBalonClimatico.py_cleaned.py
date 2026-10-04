def fonk1(time):
    return -0.48 * time**3 + 36 * time**2 - 760 * time + 4100
def fonk2(time):
    return -0.12 * time**4 + 12 * time**3 - 380 * time**2 + 4100 * time + 220
def fonk3(b1):
    return b1 * 3.6
def fonk4(b4, b5, b6):
    a1 = 0
    a2 = 0
    for time in range(b4, b5 + 1, b6):
        b1 = fonk1(time)
        b2 = fonk2(time)
        b3 = fonk3(b1)
        if b2 > a1:
            a1 = b2
            a2 = time
        print(f"{time:2}h   {b2:8.2f}m       {b3:6.2f}km/h")
    print(f"La altura máxima se alcanzó a las {a2} horas.")
    print(f"Esta altura máxima fue de {a1} metros.")
def fonk5():
    while True:
        try:
            b4 = int(input("Ingrese el tiempo inicial (en horas): "))
            b5 = int(input("Ingrese el tiempo final (en horas): "))
            b6 = int(input("Ingrese el incremento de horas: "))
            if 0 <= b4 < b5 <= 48:
                break
            else:
                print("Error: El tiempo inicial debe ser mayor o igual a cero y el tiempo final debe ser menor o igual a 48 horas.")
        except ValueError:
            print("Error: Por favor, ingrese valores enteros válidos.")
    fonk4(b4, b5, b6)
if b7 = = "__main__":
    fonk5()