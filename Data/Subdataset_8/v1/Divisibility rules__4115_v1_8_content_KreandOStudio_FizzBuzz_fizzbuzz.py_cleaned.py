fizzbuzz = True
print("!!!Bienvenidos a FizzBuzz!!!")
while fizzbuzz:
    try:
        num = int(input("Introduzca un número del 1 al 100: "))
        if 1 <= num <= 100:
            for i in range(1, num + 1):
                if i % 3 == 0 and i % 5 == 0:
                    print("FizzBuzz")
                elif i % 3 == 0:
                    print("Fizz")
                elif i % 5 == 0:
                    print("Buzz")
                else:
                    print(i)
        else:
            print("Por favor, introduzca un número válido!")
    except ValueError:
        print("Por favor, introduzca solo números.")
    pregunta = input("¿Desea jugar de nuevo? (S/N): ")[0].upper()
    if pregunta == "N":
        fizzbuzz = False
    elif pregunta != "S":
        print("Opción incorrecta!")