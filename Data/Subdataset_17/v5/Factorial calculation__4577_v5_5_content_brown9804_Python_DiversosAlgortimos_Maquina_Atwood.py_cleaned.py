def main():
    print("Bienvenido a la máquina de Atwood.")
    print("Este sistema consta de dos masas, m1 y m2, conectadas por una cuerda inelástica")
    print("y una polea ideal, ambas de masa despreciable.")
    m1 = float(input("Ingrese la masa del objeto 1 en kilogramos (el objeto más pesado): "))
    m2 = float(input("Ingrese la masa del objeto 2 en kilogramos: "))
    g = 9.81
    acceleration = (g * (m1 - m2)) / (m1 + m2)
    print("\nLa aceleración debida a la gravedad es 9.81 m/s².")
    print(f"La aceleración del sistema es: {acceleration:.2f} m/s²")
    tension_newtons = (g * (m1 - m2)) / (m1 + m2)
    print(f"La tensión en la cuerda es: {tension_newtons:.2f} N")
    tension_dynes = tension_newtons * 1e5
    print(f"La tensión en dinas es: {tension_dynes:.2f} dynas")
if __name__ == "__main__":
    main()