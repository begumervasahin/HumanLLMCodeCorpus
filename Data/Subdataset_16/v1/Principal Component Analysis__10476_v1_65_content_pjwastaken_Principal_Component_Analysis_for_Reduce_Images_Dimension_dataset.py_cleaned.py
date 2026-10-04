import os
class class1:
    def fonk1(self, required_no):
        b1 = "ORL"
        b2 = os.path.join("images", b1)
        self.b3 = []
        self.b4 = []
        self.b5 = []
        self.b6 = []
        self.b7 = []
        self.b8 = []
        self.b9 = []
        a1 = 0
        for name in os.listdir(b2):
            b10 = os.path.join(b2, name)
            if os.path.isdir(b10):
                if len(os.listdir(b10)) >= required_no:
                    a2 = 0
                    for img_name in os.listdir(b10):
                        b11 = os.path.join(b10, img_name)
                        if a2 < required_no:
                            self.b3.append(b11)
                            self.b4.append(a1)
                            if len(self.b5) > a1:
                                self.b5[a1] += 1
                            else:
                                self.b5.append(1)
                            if a2 = = 0:
                                self.b9.append(name)
                        else:
                            self.b6.append(b11)
                            self.b7.append(a1)
                            if len(self.b8) > a1:
                                self.b8[a1] += 1
                            else:
                                self.b8.append(1)
                        a2 += 1
                    a1 += 1
