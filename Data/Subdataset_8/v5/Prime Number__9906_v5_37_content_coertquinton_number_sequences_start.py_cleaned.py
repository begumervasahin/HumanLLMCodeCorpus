from tasks.prime_numbers import PrimeNumbers
from tasks.fibonacci_numbers import FibonacciNumbers
from tasks.collatz_conjecture import CollatzConjecture
from tasks.strong_prime_numbers import StrongPrimeNumbers
from printer.output_printer import OutputPrinter
class CommandLineInterface:
    def __init__(self):
        self.printer = OutputPrinter().select_printer(OutputPrinter.SIMPLE_NUMBERS)
        self.tasks = {
            0: 'Change printer. Default is simple numbers.',
            1: 'Exit',
            2: 'Print prime numbers',
            3: 'Print Fibonacci numbers',
            4: 'Print Collatz Conjecture',
            5: 'Print strong prime numbers',
        }
    def process_menu(self):
        while True:
            self.display_menu()
            menu_item = input('Type menu item number to start math operation: ')
            if int(menu_item) == 0:
                self.set_printer()
                continue
            if self.validate_menu_item(menu_item):
                if int(menu_item) == 1:
                    break
                print(f'{menu_item} has been selected')
                self.set_task(int(menu_item))
                self.process_task()
    def display_menu(self):
        print('---------------------------------------------------')
        print('Type the corresponding number to access a menu item')
        for key, value in self.tasks.items():
            print(f'{key}: {value}')
    def validate_menu_item(self, menu_item):
        error_message = f'Menu Item {menu_item} is not a valid choice. Input must be an integer between 0 and {len(self.tasks) - 1}'
        try:
            if not menu_item.isdigit():
                print(error_message)
                return False
            validated_item = int(menu_item)
            if validated_item in self.tasks:
                return True
            else:
                print('Invalid menu item chosen.')
                return False
            print(error_message)
            return False
        except:
            print(error_message)
    def set_task(self, menu_item):
        if menu_item == 2:
            self.task = PrimeNumbers()
        elif menu_item == 3:
            self.task = FibonacciNumbers()
        elif menu_item == 4:
            self.task = CollatzConjecture()
        elif menu_item == 5:
            self.task = StrongPrimeNumbers()
    def process_task(self):
        if self.task.receive_input():
            self.task.process()
        result = self.task.return_result()
        self.printer.print_output(result)
    def set_printer(self):
        output_printer = OutputPrinter()
        output_printer.display_printer_options()
        printer_type = int(input("Type the number of the type of output you would like to see."))
        if output_printer.validate_printer(printer_type):
            self.printer = output_printer.select_printer(printer_type)
            print(f"Printer set to {output_printer._printer_types[printer_type]}")
        else:
            self.printer = output_printer.select_printer(output_printer.SIMPLE_NUMBERS)
            print("Incorrect printer selected. Printer set to Simple number printer.")
if __name__ == '__main__':
    print('Program start')
    cmd = CommandLineInterface()
    cmd.process_menu()
    print('Program terminated')