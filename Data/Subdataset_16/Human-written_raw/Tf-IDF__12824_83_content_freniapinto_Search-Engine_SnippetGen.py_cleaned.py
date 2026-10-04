from FileAccess import FileAccess
class class1:
    def fonk1(self):
        self.a1 = 150
        return
    def fonk2(self, doc, b3):
        b1 = FileAccess()
        b2 = b1.get_stop_words()
        b3 = b3.split()
        b4 = b3
        b5 = " ".join(b4)
        b6 = b5.split()
        b7 = doc.split()
        b8 = list(set(b7).intersection(b6))
        b9 = []
        for each in b8:
            if each in b8:
                b10 = b7.index(each)
                b9.append(b10)
            else:
                continue
        b11 = ''
        a2 = 0
        for each in b7:
            if a2 in b9:
                b12 = '"'+each+'" '
                b11 += b12
            else:
                b11 += each + ' '
            a2 += 1
        return b11