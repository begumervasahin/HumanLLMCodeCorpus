def main():
    print("Bienvenido a la máquina de Atwood. Este sistema consiste en dos masas, m1 y m2,")
    print("conectadas por una cuerda inelástica y una polea ideal, ambas de masa despreciable.")
    m1 = float(input("Ingrese la masa del objeto 1 en kilogramos (el objeto más pesado): "))
    m2 = float(input("Ingrese la masa del objeto 2 en kilogramos: "))
    g = 9.81
    acceleration = (g * (m1 - m2)) / (m1 + m2)
    print("Recuerde que la aceleración debida a la gravedad es 9.81 m/s².")
    print(f"Con los datos proporcionados, la aceleración del sistema es: {acceleration:.2f} m/s²")
    tension_newtons = (g * (2 * m1 * m2)) / (m1 + m2)
    print(f"La tensión en la cuerda, en Newtons, es: {tension_newtons:.2f} N")
    tension_dynes = tension_newtons * 1e5
    print(f"La tensión en dinas es: {tension_dynes:.2f} dynas")
if __name__ == "__main__":
    main()