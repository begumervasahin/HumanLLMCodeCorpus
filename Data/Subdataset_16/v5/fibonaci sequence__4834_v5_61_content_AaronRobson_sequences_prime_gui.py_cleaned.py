import threading
from time import sleep
import itertools
import printrewritable as pr
import prime
b1 = 'primelist.txt'
a1 = 0.042
b2 = pr.PrintRewritable()
class class1:
    def fonk1(self):
        self.b3 = []
        self.b4 = False
        self.b5 = prime.PrimeCollection()
    def fonk2(self):
        b6 = threading.Thread(target=self._prime_finder, name='PrimeThread')
        b7 = threading.Thread(target=self._display_thread, name='CheckerThread')
        self.b3 = [b6, b7]
    def fonk3(self):
        self.fonk5()
        self.b5 = prime.PrimeCollection()
    def fonk4(self):
        self.fonk5()
        self.fonk2()
        self.b4 = False
        for thread in self.b3:
            if not thread.is_alive():
                thread.fonk4()
    def fonk5(self):
        self.b4 = True
        for thread in self.b3:
            if thread.is_alive():
                thread.join()
    def fonk6(self, filepath):
        self.fonk5()
        self.fonk13(filepath, *self.b5.cache)
    def fonk7(self, filepath):
        self.fonk5()
        b8 = self.fonk14(filepath)
        self.b5 = prime.PrimeCollection(b8)
    @property
    def fonk8(self):
        return self.b5.last
    def fonk9(self):
        return not self.b4
    def fonk10(self):
        for _ in itertools.takewhile(self.is_continuing, self.b5):
            pass
    def fonk11(self):
        while self.fonk9():
            b2.print(self.last_prime, True)
            sleep(a1)
    def fonk12(self):
        return len(self.b5)
    def fonk13(self, filepath, *output_enumeration):
        with open(filepath, 'w') as file:
            for item in output_enumeration:
                file.write(f'{item}\n')
    def fonk14(self, filepath):
        with open(filepath, 'r') as file:
            b9 = (line.strip() for line in file.readlines())
            return [int(line) for line in b9 if line]
if b10 = = "__main__":
    print('Prime number finder:')
    b2.print('Loading...', True)
    b11 = class1()
    try:
        b11.fonk7(b1)
    except IOError:
        print('No b8 found, starting from scratch.')
    print('Hit Enter to finish and save.')
    b11.fonk4()
    input()
    b11.fonk5()
    print()
    print(f'{b11.last_prime} highest prime')
    print(f'{len(b11)} found')
    print(f'Attempting to save file to {b1!r}, this may take a while.')
    try:
        b11.fonk6(b1)
    except IOError:
        print('File failed to save.')
    else:
        print('File saved successfully.')