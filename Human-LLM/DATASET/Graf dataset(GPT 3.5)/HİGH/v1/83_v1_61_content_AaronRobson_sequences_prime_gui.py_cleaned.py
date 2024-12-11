import threading
from time import sleep
import itertools
import printrewritable as pr
import prime
b1 = 'primelist.txt'
a1 = 0.042
b2 = pr.PrintRewritable()
class class1():
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
    def fonk8(self):
        return self.b6.last
    b9 = property(_last_prime)
    def fonk9(self, *a):
        return not self.b7
    def fonk10(self):
        for prime_num in itertools.takewhile(self.is_continuing, self.b6):
            pass
    def fonk11(self):
        while self.fonk9():
            b2.print(self.b9, True)
            sleep(a1)
    def fonk12(self):
        return len(self.b6)
    def fonk13(self, filepath, *output_enumeration):
        with open(filepath, b10 = 'w') as f:
            for item in output_enumeration:
                f.write('%s\n' % item)
    def fonk14(self, filepath):
        with open(filepath, b10 = 'r') as f:
            b11 = (line.strip() for line in f.readlines())
            return (int(line) for line in b11 if line)
def fonk15():
    print('Prime number finder:')
    b2.print('Loading...', True)
    b12 = class1()
    try:
        b12.fonk7(b1)
    except IOError:
        print('No b8 found, starting from scratch.')
    print('Hit Enter to finish and save.')
    b12.fonk4()
    input()
    b12.fonk5()
    print()
    print('%d highest prime' % (b12.b9))
    print('%d found' % (len(b12)))
    print('Attempting to save file to %r, this may take a while.' % (b1))
    try:
        b12.fonk6(b1)
    except IOError:
        print('File failed to save.')
    else:
        print('File saved successfully.')
if b13 = = "__main__":
    fonk15()