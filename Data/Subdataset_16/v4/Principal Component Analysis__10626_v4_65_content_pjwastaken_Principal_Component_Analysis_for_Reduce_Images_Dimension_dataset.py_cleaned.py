import os
class class1:
    def fonk1(self, required_no):
        b1 = "ORL"
        b2 = os.path.join("b11", b1)
        self.b3 = []
        self.b4 = []
        self.b5 = []
        self.b6 = []
        self.b7 = []
        self.b8 = []
        self.b9 = []
        a1 = 0
        for person_name in os.listdir(b2):
            b10 = os.path.join(b2, person_name)
            if os.path.isdir(b10) and len(os.listdir(b10)) >= required_no:
                b11 = os.listdir(b10)
                for b13, img_name in enumerate(b11):
                    b12 = os.path.join(b10, img_name)
                    if b13 < required_no:
                        self.b3.append(b12)
                        self.b4.append(a1)
                        if len(self.b5) > a1:
                            self.b5[a1] += 1
                        else:
                            self.b5.append(1)
                        if b13 = = 0:
                            self.b9.append(person_name)
                    else:
                        self.b6.append(b12)
                        self.b7.append(a1)
                        if len(self.b8) > a1:
                            self.b8[a1] += 1
                        else:
                            self.b8.append(1)
                a1 += 1