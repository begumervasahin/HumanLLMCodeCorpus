import threading
from time import sleep
import itertools
class class1:
    def fonk1(self, message, b1 = False):
        fonk1(message, b2 = '\r' if b1 else '\n')
class class2:
    def fonk2(self, b3 = None):
        self.b4 = b3 or []
        self.a1 = 2
    @property
    def fonk3(self):
        return self.b4[-1] if self.b4 else None
    def fonk4(self):
        return self
    def fonk5(self):
        while not self.fonk6(self.a1):
            self.a1 += 1
        self.b4.append(self.a1)
        b5 = self.a1
        self.a1 += 1
        return b5
    @staticmethod
    def fonk6(n):
        if n < 2:
            return False
        for b6 in range(2, int(n**0.5) + 1):
            if n % b6 = = 0:
                return False
        return True
b7 = class1()
a2 = 0.042
b8 = 'primelist.txt'
class class3:
    def fonk7(self):
        self.b9 = []
        self.b10 = class2()
        self.b11 = False
    def fonk8(self):
        b12 = threading.Thread(target=self._prime_finder, name='PrimeThread')
        b13 = threading.Thread(target=self._display_thread, name='CheckerThread')
        self.b9 = [b12, b13]
    def fonk9(self):
        self.fonk11()
        self.b10 = class2()
    def fonk10(self):
        self.fonk11()
        self.fonk8()
        self.b11 = False
        for thread in self.b9:
            if not thread.is_alive():
                thread.fonk10()
    def fonk11(self):
        self.b11 = True
        for thread in self.b9:
            if thread.is_alive():
                thread.join()
    def fonk12(self, filepath):
        self.fonk11()
        self.fonk19(filepath, *self.b10.b4)
    def fonk13(self, filepath):
        self.fonk11()
        b14 = self.fonk20(filepath)
        self.b10 = class2(b14)
    @property
    def fonk14(self):
        return self.b10.last
    def fonk15(self):
        return not self.b11
    def fonk16(self):
        for _ in itertools.takewhile(self.is_continuing, self.b10):
            pass
    def fonk17(self):
        while self.fonk15():
            b7.fonk1(self.last_prime, True)
            sleep(a2)
    def fonk18(self):
        return len(self.b10.b4)
    def fonk19(self, filepath, *output_enumeration):
        with open(filepath, b15 = 'w') as file:
            for item in output_enumeration:
                file.write(f'{item}\n')
    def fonk20(self, filepath):
        with open(filepath, b15 = 'r') as file:
            b16 = (line.strip() for line in file.readlines())
            return [int(line) for line in b16 if line]
if b17 = = "__main__":
    fonk1('Prime number finder:')
    b7.fonk1('Loading...', True)
    b18 = class3()
    try:
        b18.fonk13(b8)
    except IOError:
        fonk1('No b14 found, starting from scratch.')
    fonk1('Hit Enter to finish and save.')
    b18.fonk10()
    input()
    b18.fonk11()
    fonk1()
    fonk1(f'{b18.last_prime} highest b5')
    fonk1(f'{len(b18)} found')
    fonk1(f'Attempting to save file to {b8!r}, this may take a while.')
    try:
        b18.fonk12(b8)
    except IOError:
        fonk1('File failed to save.')
    else:
        fonk1('File saved successfully.')