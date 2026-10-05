def fizz_buzz_game():
    play_game = True
    print("¡Bienvenidos a FizzBuzz!")
    while play_game:
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
                print("Por favor, introduzca un número válido entre 1 y 100.")
        except ValueError:
            print("Por favor, introduzca solo números enteros.")
        play_again = input("¿Desea jugar de nuevo? (S/N): ")[0].upper()
        if play_again == "N":
            play_game = False
        elif play_again != "S":
            print("Opción incorrecta. Por favor, elija S para jugar nuevamente o N para salir.")
if __name__ == "__main__":
    fizz_buzz_game()