def fonk1():
    print("!!!Bienvenidos a FizzBuzz!!!")
    b1 = True
    while b1:
        b2 = fonk2()
        fonk3(b2)
        b1 = fonk4()
def fonk2():
    while True:
        try:
            b2 = int(input("Introduzca un número del 1 al 100: "))
            if 1 <= b2 <= 100:
                return b2
            else:
                print("Por favor, introduzca un número válido!")
        except ValueError:
            print("Por favor, introduzca solo números.")
def fonk3(b2):
    for i in range(1, b2 + 1):
        if i % b3 = = 0 and i % b4 == 0:
            print("FizzBuzz")
        elif i % b3 = = 0:
            print("Fizz")
        elif i % b4 = = 0:
            print("Buzz")
        else:
            print(i)
def fonk4():
    while True:
        b5 = input("¿Desea jugar de nuevo? (S/N): ").strip().upper()
        if b5 = = "S":
            return True
        elif b5 = = "N":
            return False
        else:
            print("¡Opción incorrecta!")
if b6 = = '__main__':
    fonk1()