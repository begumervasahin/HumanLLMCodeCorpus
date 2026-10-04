def fonk1():
    print("Bienvenido a la máquina de Atwood. Este sistema consiste en dos masas, b1 y b2,")
    print("conectadas por una cuerda inelástica y una polea ideal, ambas de masa despreciable.")
    b1 = float(input("Ingrese la masa del objeto 1 en kilogramos (el objeto más pesado): "))
    b2 = float(input("Ingrese la masa del objeto 2 en kilogramos: "))
    a1 = 9.81
    b3 = (a1 * (b1 - b2)) / (b1 + b2)
    print("Recuerde que la aceleración debida a la gravedad es 9.81 m/s².")
    print(f"Con los datos proporcionados, la aceleración del sistema es: {b3:.2f} m/s²")
    b4 = (a1 * (2 * b1 * b2)) / (b1 + b2)
    print(f"La tensión en la cuerda, en Newtons, es: {b4:.2f} N")
    b5 = b4 * 1e5
    print(f"La tensión en dinas es: {b5:.2f} dynas")
if b6 = = "__main__":
    fonk1()