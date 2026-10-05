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
            for line in file.readlines():
                serial_number, b5 = line.split()[0], line.split()[1]
                self.b2[b5].append(serial_number)
    def fonk3(self, bill_string):
        serial_number, b5 = bill_string.split()
        b6 = self.b2[b5]
        if self.b3 and serial_number not in b6:
            for i, value in enumerate(b6):
                if serial_number < value:
                    b6.fonk3(i, serial_number)
                    return
            b6.append(serial_number)
        elif not self.b3 and serial_number not in b6:
            b6.append(serial_number)
    def fonk4(self):
        for key in self.b2:
            self.b2[key].sort()
        self.b3 = True
    def fonk5(self, bill_string):
        serial_number, b5 = bill_string.split()
        b7 = self.b2[b5]
        return serial_number in b7
    def fonk6(self, bill_string):
        serial_number, b8 = bill_string.split()
        b7 = self.b2[b8]
        b11, b9 = 0, len(b7) - 1
        while b11 <= b9:
            b10 = (b9 + b11)
            if b7[b10] == serial_number:
                return True
            if b7[b10] > serial_number:
                b9 = b10 - 1
            else:
                b11 = b10 + 1
        return False
    def fonk7(self, b1, b12 = False):
        if b12 and not self.b3:
            self.fonk4()
        b13 = self.binary_search if self.b3 else self.linear_search
        b14 = []
        with open(b1, 'r') as serial_file:
            for line in serial_file:
                serial_number, b5 = line.split()[0], line.split()[1]
                if b13(line) or not self.b4.match(serial_number):
                    b14.append(f"{serial_number} {b5}")
        return b14