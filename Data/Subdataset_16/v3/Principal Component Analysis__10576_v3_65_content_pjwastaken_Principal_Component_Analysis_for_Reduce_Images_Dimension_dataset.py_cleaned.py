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
        for person_name in os.listdir(b2):
            b10 = os.path.join(b2, person_name)
            if os.path.isdir(b10) and len(os.listdir(b10)) >= required_no:
                self.fonk2(b10, person_name, a1, required_no)
                a1 += 1
    def fonk2(self, b10, person_name, person_id, required_no):
        a2 = 0
        a3 = 0
        for b12, img_name in enumerate(os.listdir(b10)):
            b11 = os.path.join(b10, img_name)
            if b12 < required_no:
                self.b3.append(b11)
                self.b4.append(person_id)
                a2 += 1
                if b12 = = 0:
                    self.b9.append(person_name)
            else:
                self.b6.append(b11)
                self.b7.append(person_id)
                a3 += 1
        self.fonk3(a2, a3, person_id)
    def fonk3(self, a2, a3, person_id):
        self.fonk4(self.b5, a2, person_id)
        self.fonk4(self.b8, a3, person_id)
    def fonk4(self, count_list, count, person_id):
        if len(count_list) > person_id:
            count_list[person_id] += count
        else:
            count_list.append(count)
