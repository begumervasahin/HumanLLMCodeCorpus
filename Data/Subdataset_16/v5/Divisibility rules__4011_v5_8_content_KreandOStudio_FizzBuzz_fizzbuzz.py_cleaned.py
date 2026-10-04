def fonk1():
    print("!!!Bienvenidos a FizzBuzz!!!")
    while True:
        b1 = fonk2()
        fonk3(b1)
        if not fonk4():
            break
def fonk2():
    while True:
        try:
            b1 = int(input("Introduzca un número del 1 al 100: "))
            if 1 <= b1 <= 100:
                return b1
            else:
                print("Por favor, introduzca un número válido!")
        except ValueError:
            print("Por favor, introduzca solo números.")
def fonk3(b1):
    for i in range(1, b1 + 1):
        if i % b2 = = 0 and i % b3 == 0:
            print("FizzBuzz")
        elif i % b2 = = 0:
            print("Fizz")
        elif i % b3 = = 0:
            print("Buzz")
        else:
            print(i)
def fonk4():
    while True:
        b4 = input("¿Desea jugar de nuevo? (S/N): ").strip().upper()
        if b4 = = "S":
            return True
        elif b4 = = "N":
            return False
        else:
            print("¡Opción incorrecta!")
if b5 = = '__main__':
    fonk1()