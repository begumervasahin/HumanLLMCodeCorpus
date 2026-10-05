import re
class class1:
    def fonk1(self, b1 = ""):
        self.b2 = {"5": [], "10": [], "20": [], "50": [], "100": []}
        self.b3 = b1 == ''
        if not self.b3:
            self.fonk2(b1)
        self.b4 = re.compile(r'^[A-M][A-L](?!00000000)\d{8}(?![OZ])[A-Z]$')
    def fonk2(self, b1):
        with open(b1, 'r') as file:
            for line in file:
                serial_number, b5 = line.split()
                self.b2[b5].append(serial_number)
    def fonk3(self, bill_string):
        serial_number, b5 = bill_string.split()
        b6 = self.b2[b5]
        if self.b3 and serial_number not in b6:
            self.fonk4(serial_number, b6)
        elif not self.b3 and serial_number not in b6:
            b6.append(serial_number)
    def fonk4(self, serial_number, b6):
        for i, value in enumerate(b6):
            if serial_number < value:
                b6.fonk3(i, serial_number)
                return
        b6.append(serial_number)
    def fonk5(self):
        for key in self.b2:
            self.b2[key].sort()
        self.b3 = True
    def fonk6(self, bill_string):
        serial_number, b5 = bill_string.split()
        return serial_number in self.b2[b5]
    def fonk7(self, bill_string):
        serial_number, b5 = bill_string.split()
        b7 = self.b2[b5]
        b10, b8 = 0, len(b7) - 1
        while b10 <= b8:
            b9 = (b8 + b10)
            if b7[b9] == serial_number:
                return True
            elif b7[b9] > serial_number:
                b8 = b9 - 1
            else:
                b10 = b9 + 1
        return False
    def fonk8(self, b1, b11 = False):
        if b11 and not self.b3:
            self.fonk5()
        b12 = self.binary_search if self.b3 else self.linear_search
        b13 = []
        with open(b1, 'r') as file:
            for line in file:
                serial_number, b5 = line.split()
                b14 = f"{serial_number} {b5}"
                if b12(line) or not self.b4.match(serial_number):
                    b13.append(b14)
        return b13
b15 = class1("your_watchlist_file.txt")
b15.fonk3("ABC12345678 20")
b15.fonk3("DEF98765432 10")
b15.fonk3("GHI87654321 5")
print(b15.fonk8("bill_file.txt", b11 = True))