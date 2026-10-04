def fonk1():
    print("Bienvenido a la máquina de Atwood, consiste en dos masas b1 y b2, conectadas por una cuerda inelástica de masa despreciable con una polea ideal de masa despreciable")
    b1 = float(input("Digite la masa del objeto 1 en kilogramos, considere que este objeto es el más pesado: "))
    b2 = float(input("Digite la masa del objeto 2 en kilogramos: "))
    a1 = 9.81
    b3 = (a1 * (b1 - b2)) / (b1 + b2)
    print("Recuerde que la gravedad es 9.81 m/s^2")
    print(f"Considerando los datos anteriores, la aceleración es equivalente a: {b3:.2f} m/s^2")
    b4 = (a1 * 2 * (b1 * b2)) / (b1 + b2)
    print(f"La tensión de la cuerda en Newtons es: {b4:.2f} N")
    b5 = (a1 * 0.01 * 2 * (b1 * b2) * 0.001) / ((b1 + b2) * 0.001)
    print(f"La tensión en dinas es: {b5:.2f} dyn")
if b6 = = "__main__":
    fonk1()