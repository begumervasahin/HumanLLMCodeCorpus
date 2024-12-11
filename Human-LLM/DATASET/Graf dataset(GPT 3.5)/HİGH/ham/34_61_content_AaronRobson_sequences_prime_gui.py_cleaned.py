import threading
from time import sleep
import printrewritable as pr
import prime
import itertools
b1 = 'primelist.txt'
a1 = 0.042
def fonk1(b2):
    b2 = str(b2)
    return '%s thread %r.' % (b2, threading.current_thread().name)
b3 = pr.PrintRewritable()
class class1():
    def fonk2(self, *args):
        self.b4 = ()
        self.fonk4(*args)
    def fonk3(self):
        b5 = threading.Thread(target=self._prime_finder)
        b5.setName('PrimeThread')
        b6 = threading.Thread(target=self._display_thread)
        b6.setName('CheckerThread')
        self.b4 = (b5, b6)
    def fonk4(self):
        self.fonk6()
        self.b7 = prime.PrimeCollection()
    def fonk5(self):
        self.fonk6()
        self.fonk3()
        self.b8 = False
        for t in self.b4:
            if not t.is_alive():
                t.fonk5()
    def fonk6(self):
        self.b8 = True
        for t in self.b4:
            if t.is_alive():
                t.join()
    def fonk7(self, filepath):
        self.fonk6()
        self.fonk14(filepath, *self.b7.cache)
    def fonk8(self, filepath):
        self.fonk6()
        b9 = self.fonk15(filepath)
        self.b7 = prime.PrimeCollection(b9)
    def fonk9(self):
        return self.b7.last
    b10 = property(_last_prime)
    def fonk10(self, *a):
        return not self.b8
    def fonk11(self):
        for prime_num in itertools.takewhile(self.is_continuing, self.b7):
            pass
    def fonk12(self):
        '''Check queue for messages, if queue has something in it,
        will check it again and again until it does not as which point:
        it will wait for a bit and try again.
        '''
        while self.fonk10():
            b3.print(self.b10, True)
            sleep(a1)
    def fonk13(self):
        return len(self.b7)
    def fonk14(self, filepath, *output_enumeration):
        with open(filepath, b11 = 'w') as f:
            for item in output_enumeration:
                f.write('%s\n' % item)
    def fonk15(self, filepath):
        with open(filepath, b11 = 'r') as f:
            b12 = (line.strip() for line in f.readlines())
            return (int(line) for line in b12 if line)
if b13 = = "__main__":
    print('Prime number finder:')
    b3.print('Loading...', True)
    b14 = class1()
    try:
        b14.fonk8(b1)
    except IOError:
        print('No b9 found, starting from stratch.')
    print('Hit Enter to finish and save.')
    b14.fonk5()
    input()
    b14.fonk6()
    print()
    print('%d highest prime' % (b14.b10))
    print('%d found' % (len(b14)))
    print('Attempting to save file to %r, this may take a while.' % (b1))
    try:
        b14.fonk7(b1)
    except IOError:
        print('File failed to save.')
    else:
        print('File saved successfully.')