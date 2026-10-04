import time
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_number_of_elements():
    while True:
        try:
            number_of_elements = int(input("Introduzca el número de elementos: "))
            return number_of_elements
        except ValueError:
            print('Solo introduzca números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            clear_screen()
def get_elements(number_of_elements):
    elements_list = [None] * number_of_elements
    while True:
        try:
            for i in range(number_of_elements):
                element = int(input('Elemento {}: '.format(i + 1)))
                elements_list[i] = element
            return elements_list
        except ValueError:
            print('Solo introduzca números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            clear_screen()
def calculate_average(elements_list):
    total = sum(elements_list)
    average = total / len(elements_list)
    print('Promedio: ', average)
def main():
    number_of_elements = get_number_of_elements()
    elements_list = get_elements(number_of_elements)
    calculate_average(elements_list)
if __name__ == "__main__":
    main()