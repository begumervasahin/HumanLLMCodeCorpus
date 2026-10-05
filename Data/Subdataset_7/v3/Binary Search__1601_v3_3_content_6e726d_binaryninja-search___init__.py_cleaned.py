
class class1:
    def fonk1(self, b1):
        self.b1 = b1
class class2:
    a1 = 1
class class3:
    def fonk2(self, b2):
        self.b2 = b2
    def fonk3(self, title, b11, plaintext):
        print("HTML Report Title:", title)
        print("HTML Report:", b11)
        print("Plaintext Report:", plaintext)
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
    b3 = [token.b1.strip() for token in instruction_token_list if isinstance(token, class1)]
    return " ".join(b3)
def fonk8(b13):
    if not isinstance(b13, str):
        raise TypeError('Immediate must be a string.')
    if b13.startswith("0x"):
        return int(b13, 16)
    else:
        return int(b13)
def fonk9(bv, b13):
    b6 = []
    for function_item in bv.b2:
        b7 = class5(function_item.b3)
        try:
            while True:
                (instruction, address) = b7.fonk6()
                for token in instruction:
                    if token.b8 = = class2.a1:
                        if token.b9 = = b13:
                            b10 = fonk7(instruction)
                            b6.append((address, function_item.b4, b10))
        except StopIteration:
            pass
    return b6
def fonk10(bv, b9, b6):
    b11 = "<!DOCTYPE b11>\n<b11>\n\t<body>\n\t\t<table>\n\t\t\t<tr>\n\t\t\t\t<th width=\"150\">Address</th>\n\t\t\t\t<th width=\"150\">class4</th>\n\t\t\t\t<th>Instruction</th>\n\t\t\t</tr>\n"
    for item in b6:
        b11 += "\t\t\t<tr>\n"
        b11 += "\t\t\t\t<td><pre>0x%016X</pre></td>\n" % item[0]
        b11 += "\t\t\t\t<td><pre>%s</pre></td>\n" % item[1]
        b11 += "\t\t\t\t<td><pre>%s</pre></td>\n" % item[2]
        b11 += "\t\t\t</tr>\n"
    b11 += "\t\t</table>\n\t</body>\n</b11>"
    bv.fonk3("Search b13 - 0x%X" % b9, b11, "")
def fonk11(bv):
    b12 = input('Value to search: ')
    b13 = fonk8(b12)
    b6 = fonk9(bv, b13)
    fonk10(bv, b13, b6)
b14 = [class1("mov"), class1("[0x1234]")]
b3 = [(b14, 0x1000)]
b15 = class4(b3, "sample_function")
b2 = [b15]
b16 = class3(b2)
fonk11(b16)