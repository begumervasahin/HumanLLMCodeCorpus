import time
import os
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Por favor, introduzca solo números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            clear_screen()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    while True:
        try:
            num_elements = get_integer_input("Introduzca el número de elementos: ")
            break
        except KeyboardInterrupt:
            print('Operación cancelada.')
            return
    elements_list = [None] * num_elements
    for i in range(num_elements):
        while True:
            try:
                element = get_integer_input('Ingrese el valor del elemento {}: '.format(i + 1))
                elements_list[i] = element
                break
            except KeyboardInterrupt:
                print('Operación cancelada.')
                return
            except ValueError:
                print('Por favor, introduzca solo números.')
                print('Inténtelo nuevamente.')
                time.sleep(1)
                clear_screen()
    total_sum = sum(elements_list)
    average = total_sum / num_elements
    print('El promedio de los elementos es:', average)
if __name__ == "__main__":
    main()