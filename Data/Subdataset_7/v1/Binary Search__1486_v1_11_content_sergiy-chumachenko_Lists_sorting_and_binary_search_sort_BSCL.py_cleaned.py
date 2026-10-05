class class1(object):
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return "class1 method can be used to sort your list:\a2{}".format(self.b1)
    def fonk3(self):
        a1 = 0
        a2 = 1
        while a2 < len(self.b1):
            for b4 in range(len(self.b1) - a2):
                if self.b1[b4] > self.b1[b4 + 1]:
                    self.b1[b4], self.b1[b4 + 1] = self.b1[b4 + 1], self.b1[b4]
                    a1 += 1
            if a1 = = 0:
                break
            else:
                a2 += 1
        return self.b1
    def fonk4(self):
        a1 = 0
        a2 = 1
        while a2 < len(self.b1):
            for b4 in range(len(self.b1) - a2):
                if self.b1[b4] < self.b1[b4 + 1]:
                    self.b1[b4], self.b1[b4 + 1] = self.b1[b4 + 1], self.b1[b4]
                    a1 += 1
            if a1 = = 0:
                break
            else:
                a2 += 1
        return self.b1
def fonk5(lst, a2):
    a3 = 0
    b2 = len(lst) - 1
    b3 = round(b2 / 2)
    while a3 < b3 and b3 < b2:
        if a2 > lst[b3] and b3 < b2:
            a3 = b3
        elif a2 < lst[b3] and a3 < b3:
            b2 = b3
        elif a2 = = lst[b3]:
            return b3
        b3 = round((a3 + b2) / 2)
        if a3 >= b2:
            return a3
        elif b3 >= b2:
            return b2
        elif a3 >= b3:
            return a3 + 1
        else:
            continue
def fonk6(a2, lst):
    b4 = len(lst)
    if b4 = = 0:
        lst.append(a2)
    elif b4 = = 1:
        if a2 >= lst[0]:
            lst.append(a2)
        elif a2 < lst[0]:
            lst.insert(0, a2)
    elif b4 = = 2:
        if a2 >= lst[-1]:
            lst.append(a2)
        elif a2 <= lst[0]:
            lst.insert(0, a2)
        else:
            lst.insert(1, a2)
    elif b4 > 2:
        if a2 <= lst[0]:
            lst.insert(0, a2)
        elif a2 >= lst[-1]:
            lst.append(a2)
        elif lst[0] < a2 < lst[-1]:
            b5 = fonk5(lst, a2)
            lst.insert(b5, a2)
    return lst
b1 = [5, 2, 9, 1, 7]
b6 = class1(b1)
print(b6.fonk3())
print(b6.fonk4())
b7 = [1, 3, 5, 7, 9]
print(fonk6(4, b7))