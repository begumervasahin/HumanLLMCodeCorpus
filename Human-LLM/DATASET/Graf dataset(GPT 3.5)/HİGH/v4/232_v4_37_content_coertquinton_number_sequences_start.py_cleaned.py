
from tasks.prime_numbers import PrimeNumbers
from tasks.fibonacci_numbers import FibonacciNumbers
from tasks.collatz_conjecture import CollatzConjecture
from tasks.strong_prime_numbers import StrongPrimeNumbers
from printer.b1 import OutputPrinter
class class1(object):
    def fonk1(self):
        b1 = OutputPrinter()
        self.b2 = b1.select_printer(b1.SIMPLE_NUMBERS)
        self.b3 = {
            0: 'Change printer. Default is simple numbers.',
            1: 'Exit',
            2: 'Print prime numbers',
            3: 'Print Fibonacci numbers',
            4: 'Print Collatz Conjecture',
            5: 'Print strong prime numbers',
        }
        sorted(self.b3.keys())
    def fonk2(self):
        while True:
            self.fonk3()
            b4 = raw_input('Type menu item number to start math operation: ')
            if int(b4) == 0:
                self.fonk7()
                continue
            if self.fonk4(b4):
                if int(b4) == 1:
                    break
                print(b4 + 'has been selected')
                self.fonk5(int(b4))
                self.fonk6()
    def fonk3(self):
        print('---------------------------------------------------')
        print('Type the corresponding number to access a menu item')
        for key, value in self.b3.iteritems():
            print(str(key) + ': ' + value)
    def fonk4(self, b4):
        b5 = 'Menu Item %s is not a valid choice. Input must be an integer between 0 and %s' % (b4,
                                                                                                            len(self.b3) - 1,
                                                                                                           )
        try:
            if not b4.isdigit():
                print(b5)
                return False
            b6 = int(b4)
            if b6 in self.b3:
                return True
            else:
                print('Invalid menu item chosen.')
                return False
            print(b5)
            return False
        except:
            print(b5)
    def fonk5(self, b4):
        if b4 = = 2:
            self.b7 = PrimeNumbers()
        if b4 = = 3:
            self.b7 = FibonacciNumbers()
        if b4 = = 4:
            self.b7 = CollatzConjecture()
        if b4 = = 5:
            self.b7 = StrongPrimeNumbers()
    def fonk6(self):
        if self.b7.receive_input():
            self.b7.process()
        b8 = self.b7.return_result()
        self.b2.print_output(b8)
    def fonk7(self):
        b1 = OutputPrinter()
        b1.display_printer_options()
        b9 = int(raw_input("Type the number of the type of output you would like to see."))
        if b1.validate_printer(b9):
            self.b2 = b1.select_printer(b9)
            print("Printer set to %s" % b1._printer_types[b9])
        else:
            self.b2 = b1.select_printer(b1.SIMPLE_NUMBERS)
            print("Incorrect printer selected. Printer set to Simple number printer.")
if b10 = = '__main__':
    print('Program start')
    b11 = class1()
    b11.fonk2()
    print('Program terminated')