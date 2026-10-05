def fizz_buzz_game():
    while True:
        print("¡Bienvenidos a FizzBuzz!")
        while True:
            try:
                num = int(input("Introduzca un número del 1 al 100: "))
                if 1 <= num <= 100:
                    break
                else:
                    print("Por favor, introduzca un número válido entre 1 y 100.")
            except ValueError:
                print("Por favor, introduzca solo números enteros.")
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
        while True:
            play_again = input("¿Desea jugar de nuevo? (S/N): ").strip().upper()
            if play_again in ("S", "N"):
                break
            else:
                print("Opción incorrecta. Por favor, elija S para jugar nuevamente o N para salir.")
        if play_again == "N":
            break
if __name__ == "__main__":
    fizz_buzz_game()