def fonk1():
    while True:
        print("¡Bienvenidos a FizzBuzz!")
        while True:
            try:
                b1 = int(input("Introduzca un número del 1 al 100: "))
                if 1 <= b1 <= 100:
                    break
                else:
                    print("Por favor, introduzca un número válido entre 1 y 100.")
            except ValueError:
                print("Por favor, introduzca solo números enteros.")
        for i in range(1, b1 + 1):
            if i % b2 = = 0 and i % b3 == 0:
                print("FizzBuzz")
            elif i % b2 = = 0:
                print("Fizz")
            elif i % b3 = = 0:
                print("Buzz")
            else:
                print(i)
        while True:
            b4 = input("¿Desea jugar de nuevo? (S/N): ").strip().upper()
            if b4 in ("S", "N"):
                break
            else:
                print("Opción incorrecta. Por favor, elija S para jugar nuevamente o N para salir.")
        if b4 = = "N":
            break
if b5 = = "__main__":
    fonk1()