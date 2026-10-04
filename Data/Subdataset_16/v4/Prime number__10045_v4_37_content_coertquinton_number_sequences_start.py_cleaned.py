
from tasks.prime_numbers import PrimeNumbers
from tasks.fibonacci_numbers import FibonacciNumbers
from tasks.collatz_conjecture import CollatzConjecture
from tasks.strong_prime_numbers import StrongPrimeNumbers
from printer.b9 import OutputPrinter
class class1:
    def fonk1(self):
        self.b1 = OutputPrinter().select_printer(OutputPrinter.SIMPLE_NUMBERS)
        self.b2 = {
            0: 'Change printer. Default is simple numbers.',
            1: 'Exit',
            2: 'Print prime numbers',
            3: 'Print Fibonacci numbers',
            4: 'Print Collatz Conjecture',
            5: 'Print strong prime numbers',
        }
    def fonk2(self):
        while True:
            self.fonk3()
            b3 = input('Type menu item number to start math operation: ')
            if b3.isdigit() and int(b3) == 0:
                self.fonk7()
                continue
            if self.fonk4(b3):
                b3 = int(b3)
                if b3 = = 1:
                    break
                print(f'{b3} has been selected')
                self.fonk5(b3)
                self.fonk6()
    def fonk3(self):
        print('---------------------------------------------------')
        print('Type the corresponding number to access a menu item')
        for key, value in sorted(self.b2.items()):
            print(f'{key}: {value}')
    def fonk4(self, b3):
        try:
            b4 = int(b3)
            if b4 in self.b2:
                return True
            else:
                print(f'Invalid menu item chosen.')
                return False
        except ValueError:
            b5 = f'Menu Item {b3} is not a valid choice. Input must be an integer between 0 and {len(self.b2) - 1}'
            print(b5)
            return False
    def fonk5(self, b3):
        b6 = {
            2: PrimeNumbers,
            3: FibonacciNumbers,
            4: CollatzConjecture,
            5: StrongPrimeNumbers
        }
        self.b7 = b6.get(b3, lambda: None)()
    def fonk6(self):
        if self.b7 and self.b7.receive_input():
            self.b7.process()
            b8 = self.b7.return_result()
            self.b1.print_output(b8)
    def fonk7(self):
        b9 = OutputPrinter()
        b9.display_printer_options()
        b10 = input("Type the number of the type of output you would like to see: ")
        if b10.isdigit() and b9.validate_printer(int(b10)):
            self.b1 = b9.select_printer(int(b10))
            print(f"Printer set to {b9._printer_types[int(b10)]}")
        else:
            self.b1 = b9.select_printer(OutputPrinter.SIMPLE_NUMBERS)
            print("Incorrect printer selected. Printer set to Simple number printer.")
if b11 = = '__main__':
    print('Program start')
    b12 = class1()
    b12.fonk2()
    print('Program terminated')