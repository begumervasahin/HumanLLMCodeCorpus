def fizz_buzz_game():
    play_again = True
    print("¡Bienvenidos a FizzBuzz!")
    while play_again:
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
                print("Por favor, introduzca un número válido.")
        except ValueError:
            print("Por favor, introduzca solo números.")
        while True:
            choice = input("¿Desea jugar de nuevo? (S/N): ")[0].upper()
            if choice == "S":
                break
            elif choice == "N":
                play_again = False
                break
            else:
                print("Opción incorrecta. Por favor, elija S para jugar nuevamente o N para salir.")
if __name__ == "__main__":
    fizz_buzz_game()