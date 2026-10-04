from FileAccess import FileAccess
class class1:
    def fonk1(self):
        self.a1 = 150
    def fonk2(self, doc, query):
        b1 = FileAccess()
        b2 = b1.get_stop_words()
        b3 = query.split()
        b4 = [word for word in b3 if word not in b2]
        b5 = set(b4)
        b6 = doc.split()
        b7 = set(b6)
        b8 = b5.b8(b7)
        b9 = [index for index, word in enumerate(b6) if word in b8]
        b10 = ""
        for i, word in enumerate(b6):
            if i in b9:
                b10 += f'"{word}" '
            else:
                b10 += word + ' '
        return b10.strip()
