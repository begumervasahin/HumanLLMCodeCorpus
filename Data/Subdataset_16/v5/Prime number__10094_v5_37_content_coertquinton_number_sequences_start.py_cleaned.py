
from tasks.prime_numbers import PrimeNumbers
from tasks.fibonacci_numbers import FibonacciNumbers
from tasks.collatz_conjecture import CollatzConjecture
from tasks.strong_prime_numbers import StrongPrimeNumbers
from printer.b7 import OutputPrinter
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
        print('Type the corresponding number to access a menu item:')
        for key, value in sorted(self.b2.items()):
            print(f'{key}: {value}')
    def fonk4(self, b3):
        if not b3.isdigit():
            print(f'Invalid input: {b3}. Please enter a number.')
            return False
        b3 = int(b3)
        if b3 in self.b2:
            return True
        print(f'Invalid menu item: {b3}. Please select a valid menu item.')
        return False
    def fonk5(self, b3):
        b4 = {
            2: PrimeNumbers,
            3: FibonacciNumbers,
            4: CollatzConjecture,
            5: StrongPrimeNumbers
        }
        self.b5 = b4.get(b3, lambda: None)()
    def fonk6(self):
        if self.b5 and self.b5.receive_input():
            self.b5.process()
            b6 = self.b5.return_result()
            self.b1.print_output(b6)
    def fonk7(self):
        b7 = OutputPrinter()
        b7.display_printer_options()
        b8 = input("Type the number of the type of output you would like to see: ")
        if b8.isdigit() and b7.validate_printer(int(b8)):
            self.b1 = b7.select_printer(int(b8))
            print(f"Printer set to {b7._printer_types[int(b8)]}")
        else:
            self.b1 = b7.select_printer(OutputPrinter.SIMPLE_NUMBERS)
            print("Invalid printer selection. Printer set to Simple number printer.")
if b9 = = '__main__':
    print('Program start')
    b10 = class1()
    b10.fonk2()
    print('Program terminated')