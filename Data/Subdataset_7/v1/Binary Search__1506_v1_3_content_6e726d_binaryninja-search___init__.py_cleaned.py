
class class1:
    def fonk1(self, b1):
        self.b1 = b1
class class2:
    a1 = 1
class class3:
    def fonk2(self, b2):
        self.b2 = b2
    def fonk3(self, title, b12, b13):
        print("HTML Report Title:", title)
        print("HTML Report:", b12)
        print("Plaintext Report:", b13)
class class4:
    def fonk4(self, b3, b4):
        self.b3 = b3
        self.b4 = b4
class class5:
    def fonk5(self, b3):
        self.b3 = b3
        self.a2 = 0
    def fonk6(self):
        if self.a2 < len(self.b3):
            b5 = self.b3[self.a2]
            self.a2 += 1
            return b5
        else:
            raise StopIteration
def fonk7(instruction_token_list):
    b6 = list()
    for instruction_token in instruction_token_list:
        if not isinstance(instruction_token, class1):
            raise TypeError('List must contain class1 objects only.')
        b6.append(instruction_token.b1.strip())
    return " ".join(b6)
def fonk8(b16):
    if not isinstance(b16, str):
        raise TypeError('Immediate must be a String object.')
    if b16.startswith("0x"):
        return int(b16, 16)
    else:
        return int(b16)
def fonk9(bv, b16):
    b7 = list()
    for function_item in bv.b2:
        b8 = class5(function_item.b3)
        try:
            while True:
                (instruction, address) = b8.fonk6()
                for token in instruction:
                    if token.b9 = = class2.a1:
                        if token.b10 = = b16:
                            b11 = fonk7(instruction)
                            b7.append((address, function_item.b4, b11))
        except StopIteration:
            pass
    return b7
def fonk10(bv, b10, b17):
    b12 = str()
    b13 = str()
    b12 += "<!DOCTYPE b12>\n"
    b12 += "<b12>\n\t<body>\n"
    b12 += "\t\t<table>\n"
    b12 += "\t\t\t<tr>\n"
    b12 += "\t\t\t\t<th b14 = \"150\">Address</th>\n"
    b12 += "\t\t\t\t<th b14 = \"150\">class4</th>\n"
    b12 += "\t\t\t\t<th>Instruction</th>\n"
    b12 += "\t\t\t</tr>\n"
    for item in b17:
        b12 += "\t\t\t<tr>\n"
        b12 += "\t\t\t\t<td><pre>0x%016X</pre></td>\n" % item[0]
        b12 += "\t\t\t\t<td><pre>%s</pre></td>\n" % item[1]
        b12 += "\t\t\t\t<td><pre>%s</pre></td>\n" % item[2]
        b12 += "\t\t\t</tr>\n"
    b12 += "\t\t</table>\n"
    b12 += "\t</body>\n</b12>"
    bv.fonk3("Search b16 - 0x%X" % b10, b12, b13)
def fonk11(bv):
    b15 = input('Value to search: ')
    b16 = fonk8(b15)
    b17 = fonk9(bv, b16)
    fonk10(bv, b16, b17)
b18 = [class1("mov"), class1("[0x1234]")]
b3 = [(b18, 0x1000)]
b19 = class4(b3, "sample_function")
b2 = [b19]
b20 = class3(b2)
fonk11(b20)