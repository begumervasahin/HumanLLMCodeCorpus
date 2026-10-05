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
        self.b3 = ()
        self.fonk3()
    def fonk2(self):
        b4 = threading.Thread(target=self._prime_finder)
        b4.setName('PrimeThread')
        b5 = threading.Thread(target=self._display_thread)
        b5.setName('CheckerThread')
        self.b3 = (b4, b5)
    def fonk3(self):
        self.fonk5()
        self.b6 = prime.PrimeCollection()
    def fonk4(self):
        self.fonk5()
        self.fonk2()
        self.b7 = False
        for t in self.b3:
            if not t.is_alive():
                t.fonk4()
    def fonk5(self):
        self.b7 = True
        for t in self.b3:
            if t.is_alive():
                t.join()
    def fonk6(self, filepath):
        self.fonk5()
        self.fonk13(filepath, *self.b6.cache)
    def fonk7(self, filepath):
        self.fonk5()
        b8 = self.fonk14(filepath)
        self.b6 = prime.PrimeCollection(b8)
    @property
    def fonk8(self):
        return self.b6.last
    def fonk9(self, *args):
        return not self.b7
    def fonk10(self):
        for prime_num in itertools.takewhile(self.is_continuing, self.b6):
            pass
    def fonk11(self):
        while self.fonk9():
            b2.print(self.last_prime, True)
            sleep(a1)
    def fonk12(self):
        return len(self.b6)
    def fonk13(self, filepath, *output_enumeration):
        with open(filepath, b9 = 'w') as f:
            f.writelines(f"{item}\n" for item in output_enumeration)
    def fonk14(self, filepath):
        with open(filepath, b9 = 'r') as f:
            return (int(line.strip()) for line in f if line.strip())
def fonk15():
    print('Prime number finder:')
    b2.print('Loading...', True)
    b10 = class1()
    try:
        b10.fonk7(b1)
    except IOError:
        print('No b8 found, starting from scratch.')
    print('Hit Enter to finish and save.')
    b10.fonk4()
    input()
    b10.fonk5()
    print()
    print(f"{b10.last_prime} highest prime")
    print(f"{len(b10)} found")
    print(f"Attempting to save file to {b1}, this may take a while.")
    try:
        b10.fonk6(b1)
    except IOError:
        print('File failed to save.')
    else:
        print('File saved successfully.')
if b11 = = "__main__":
    fonk15()