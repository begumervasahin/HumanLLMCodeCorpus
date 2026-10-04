import time
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def prompt_for_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Solo introduzca números.')
            print('Inténtelo nuevamente.')
            time.sleep(1)
            clear_screen()
def get_number_of_elements():
    return prompt_for_number("Introduzca el número de elementos: ")
def get_elements(number_of_elements):
    elements_list = []
    for i in range(1, number_of_elements + 1):
        element = prompt_for_number(f'Elemento {i}: ')
        elements_list.append(element)
    return elements_list
def calculate_average(elements_list):
    total = sum(elements_list)
    average = total / len(elements_list)
    print('Promedio: ', average)
def main():
    clear_screen()
    number_of_elements = get_number_of_elements()
    elements_list = get_elements(number_of_elements)
    calculate_average(elements_list)
if __name__ == "__main__":
    main()