def fonk1():
    print("Bienvenido a la máquina de Atwood.")
    print("Este sistema consta de dos masas, b1 y b2, conectadas por una cuerda inelástica")
    print("y una polea ideal, ambas de masa despreciable.")
    b1 = float(input("Ingrese la masa del objeto 1 en kilogramos (el objeto más pesado): "))
    b2 = float(input("Ingrese la masa del objeto 2 en kilogramos: "))
    a1 = 9.81
    b3 = (a1 * (b1 - b2)) / (b1 + b2)
    print("\nLa aceleración debida a la gravedad es 9.81 m/s².")
    print(f"La aceleración del sistema es: {b3:.2f} m/s²")
    b4 = (a1 * (b1 - b2)) / (b1 + b2)
    print(f"La tensión en la cuerda es: {b4:.2f} N")
    b5 = b4 * 1e5
    print(f"La tensión en dinas es: {b5:.2f} dynas")
if b6 = = "__main__":
    fonk1()