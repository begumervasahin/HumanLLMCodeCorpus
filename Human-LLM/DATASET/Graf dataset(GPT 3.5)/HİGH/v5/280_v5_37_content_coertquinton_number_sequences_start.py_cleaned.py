from b2.prime_numbers import PrimeNumbers
from b2.fibonacci_numbers import FibonacciNumbers
from b2.collatz_conjecture import CollatzConjecture
from b2.strong_prime_numbers import StrongPrimeNumbers
from b1.b8 import OutputPrinter
class class1:
    def fonk1(self):
        self.b1 = OutputPrinter().select_printer(OutputPrinter.SIMPLE_NUMBERS)
        self.b2 = {
            0: 'Change b1. Default is simple numbers.',
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
            if int(b3) == 0:
                self.fonk7()
                continue
            if self.fonk4(b3):
                if int(b3) == 1:
                    break
                print(f'{b3} has been selected')
                self.fonk5(int(b3))
                self.fonk6()
    def fonk3(self):
        print('---------------------------------------------------')
        print('Type the corresponding number to access a menu item')
        for key, value in self.b2.items():
            print(f'{key}: {value}')
    def fonk4(self, b3):
        b4 = f'Menu Item {b3} is not a valid choice. Input must be an integer between 0 and {len(self.b2) - 1}'
        try:
            if not b3.isdigit():
                print(b4)
                return False
            b5 = int(b3)
            if b5 in self.b2:
                return True
            else:
                print('Invalid menu item chosen.')
                return False
            print(b4)
            return False
        except:
            print(b4)
    def fonk5(self, b3):
        if b3 = = 2:
            self.b6 = PrimeNumbers()
        elif b3 = = 3:
            self.b6 = FibonacciNumbers()
        elif b3 = = 4:
            self.b6 = CollatzConjecture()
        elif b3 = = 5:
            self.b6 = StrongPrimeNumbers()
    def fonk6(self):
        if self.b6.receive_input():
            self.b6.process()
        b7 = self.b6.return_result()
        self.b1.print_output(b7)
    def fonk7(self):
        b8 = OutputPrinter()
        b8.display_printer_options()
        b9 = int(input("Type the number of the type of output you would like to see."))
        if b8.validate_printer(b9):
            self.b1 = b8.select_printer(b9)
            print(f"Printer set to {b8._printer_types[b9]}")
        else:
            self.b1 = b8.select_printer(b8.SIMPLE_NUMBERS)
            print("Incorrect b1 selected. Printer set to Simple number b1.")
if b10 = = '__main__':
    print('Program start')
    b11 = class1()
    b11.fonk2()
    print('Program terminated')