'''
Created on 19 Jul 2016
@author: Quinton
'''
from tasks.prime_numbers import PrimeNumbers
from tasks.fibonacci_numbers import FibonacciNumbers
from tasks.collatz_conjecture import CollatzConjecture
from tasks.strong_prime_numbers import StrongPrimeNumbers
from printer.output_printer import OutputPrinter
class CommandLine(object):
    def __init__(self):
        op = OutputPrinter()
        self._printer = op.select_printer(op.SIMPLE_NUMBERS)
        self._tasks = {
                0: 'Change printer.  Default is simple numbers.',
                1: 'Exit',
                2: 'Print prime numbers',
                3: 'Print Fibonacci numbers',
                4: 'Print Collatz Conjecture',
                5: 'Print strong prime numbers',
            }
        sorted(self._tasks.keys())
    def process_menu(self):
        '''
        '''
        while True:
            self.display_menu()
            menu_item = raw_input('Type menu item number to start math operation: ')
            if int(menu_item) == 0:
                self.set_printer()
                continue
            if self.validate_menu_item(menu_item):
                if int(menu_item) == 1:
                    break
                print menu_item + 'has been selected'
                self.set_task(int(menu_item))
                self.process_task()
    def display_menu(self):
        print '---------------------------------------------------'
        print 'Type the corresponding number to access a menu item'
        for key, value in self._tasks.iteritems():
            print str(key) + ': ' + value
    def validate_menu_item(self, menu_item):
        error_message = 'Menu Item %s is not a valid choice.  Input must be an integer between 0 and %s' % (menu_item,
                                                                                                       len(self._tasks) - 1,
                                                                                                       )
        try:
            if not menu_item.isdigit():
                print error_message
                return False
            validated_item = int(menu_item)
            if self._tasks.has_key(validated_item):
                return True
            else:
                print 'Invalid menu item chosen.'
                return False
            print error_message
            return False
        except:
            print error_message
    def set_task(self, menu_item):
        if menu_item == 2:
            self._task = PrimeNumbers()
        if menu_item == 3:
            self._task = FibonacciNumbers()
        if menu_item == 4:
            self._task = CollatzConjecture()
        if menu_item == 5:
            self._task = StrongPrimeNumbers()
    def process_task(self):
        if self._task.receive_input():
            self._task.process()
        result = self._task.return_result()
        self._printer.print_output(result)
    def set_printer(self):
        output_printer = OutputPrinter()
        output_printer.display_printer_options()
        printer_type = int(raw_input("Type the number of the type of output you would like to see."))
        if output_printer.validate_printer(printer_type):
            self._printer = output_printer.select_printer(printer_type)
            print "Printer set to %s" % output_printer._printer_types[printer_type]
        else:
            self._printer = output_printer.select_printer(output_printer.SIMPLE_NUMBERS)
            print "Incorrect printer selected.  Printer set to Simple number printer."
if __name__ == '__main__':
    print 'Program start'
    cmd = CommandLine()
    cmd.process_menu()
    print 'Program terminated'