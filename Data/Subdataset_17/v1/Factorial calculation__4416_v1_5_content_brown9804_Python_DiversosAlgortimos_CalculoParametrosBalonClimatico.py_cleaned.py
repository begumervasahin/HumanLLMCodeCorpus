def velocidad(t):
    return -0.48 * (t ** 3) + 36 * (t ** 2) - 760 * t + 4100
def altitud(t):
    return -0.12 * t ** 4 + 12 * t ** 3 - 380 * t ** 2 + 4100 * t + 220
def velocidadconv(vel):
    return vel * 3.6
def proce(inicio, final, incremento):
    hmax = 0
    horahmx = 0
    for t in range(inicio, final + 1, incremento):
        vel = velocidad(t)
        alt = altitud(t)
        vel_kmh = velocidadconv(vel)
        if alt > hmax:
            hmax = alt
            horahmx = t
        print("{:2}h   {:8.2f}m       {:6.2f}km/h".format(t, alt, vel_kmh))
    print(f"La altura máxima se alcanzó a las {horahmx} horas.")
    print(f"Esta altura máxima fue de {hmax} metros.")
def main():
    timei = int(input("Ingrese el tiempo inicial para calcular la velocidad y la altitud para este globo climático: "))
    timef = int(input("Ingrese el tiempo final: "))
    incre = int(input("Ingrese el incremento de horas: "))
    while not (0 <= timei < timef <= 48):
        print("El tiempo inicial debe ser mayor o igual a cero y el tiempo final debe ser menor o igual a 48 horas.")
        timei = int(input("Ingrese el tiempo inicial para calcular la velocidad y la altitud para este globo climático: "))
        timef = int(input("Ingrese el tiempo final: "))
    proce(timei, timef, incre)
if __name__ == "__main__":
    main()