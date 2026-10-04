def play_fizzbuzz():
    print("!!!Bienvenidos a FizzBuzz!!!")
    while True:
        number = get_valid_number()
        play_round(number)
        if not ask_to_play_again():
            break
def get_valid_number():
    while True:
        try:
            number = int(input("Introduzca un número del 1 al 100: "))
            if 1 <= number <= 100:
                return number
            else:
                print("Por favor, introduzca un número válido!")
        except ValueError:
            print("Por favor, introduzca solo números.")
def play_round(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
def ask_to_play_again():
    while True:
        response = input("¿Desea jugar de nuevo? (S/N): ").strip().upper()
        if response == "S":
            return True
        elif response == "N":
            return False
        else:
            print("¡Opción incorrecta!")
if __name__ == '__main__':
    play_fizzbuzz()