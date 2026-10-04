
from tasks.prime_numbers import PrimeNumbers
from tasks.fibonacci_numbers import FibonacciNumbers
from tasks.collatz_conjecture import CollatzConjecture
from tasks.strong_prime_numbers import StrongPrimeNumbers
from printer.output_printer import OutputPrinter
class CommandLine:
    def __init__(self):
        self._printer = OutputPrinter().select_printer(OutputPrinter.SIMPLE_NUMBERS)
        self._tasks = {
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
            if menu_item.isdigit() and int(menu_item) == 0:
                self.set_printer()
                continue
            if self.validate_menu_item(menu_item):
                menu_item = int(menu_item)
                if menu_item == 1:
                    break
                print(f'{menu_item} has been selected')
                self.set_task(menu_item)
                self.process_task()
    def display_menu(self):
        print('---------------------------------------------------')
        print('Type the corresponding number to access a menu item')
        for key, value in sorted(self._tasks.items()):
            print(f'{key}: {value}')
    def validate_menu_item(self, menu_item):
        try:
            validated_item = int(menu_item)
            if validated_item in self._tasks:
                return True
            else:
                print(f'Invalid menu item chosen.')
                return False
        except ValueError:
            error_message = f'Menu Item {menu_item} is not a valid choice. Input must be an integer between 0 and {len(self._tasks) - 1}'
            print(error_message)
            return False
    def set_task(self, menu_item):
        tasks_map = {
            2: PrimeNumbers,
            3: FibonacciNumbers,
            4: CollatzConjecture,
            5: StrongPrimeNumbers
        }
        self._task = tasks_map.get(menu_item, lambda: None)()
    def process_task(self):
        if self._task and self._task.receive_input():
            self._task.process()
            result = self._task.return_result()
            self._printer.print_output(result)
    def set_printer(self):
        output_printer = OutputPrinter()
        output_printer.display_printer_options()
        printer_type = input("Type the number of the type of output you would like to see: ")
        if printer_type.isdigit() and output_printer.validate_printer(int(printer_type)):
            self._printer = output_printer.select_printer(int(printer_type))
            print(f"Printer set to {output_printer._printer_types[int(printer_type)]}")
        else:
            self._printer = output_printer.select_printer(OutputPrinter.SIMPLE_NUMBERS)
            print("Incorrect printer selected. Printer set to Simple number printer.")
if __name__ == '__main__':
    print('Program start')
    cmd = CommandLine()
    cmd.process_menu()
    print('Program terminated')