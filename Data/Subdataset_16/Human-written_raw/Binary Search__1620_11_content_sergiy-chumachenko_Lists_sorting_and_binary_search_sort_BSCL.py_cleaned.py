class class1(object):
    def fonk1(self,b1):
        self.b1 = b1
    def fonk2(self):
        return ("class1 method can be used to sort your list:\a2{}".format(self.b1))
    def fonk3(self):
        a1 = 0
        a2 = 1
        while a2<len(self.b1):
            for b4 in range(len(self.b1)-a2):
                if self.b1[b4]>self.b1[b4+1]:
                    self.b1[b4],self.b1[b4+1] = self.b1[b4+1],self.b1[b4]
                    a1 +=1
            if a1 = = 0:
                break
            else:
                a2+=1
        return self.b1
    def fonk4(self):
        a1 = 0
        a2 = 1
        while a2<len(self.b1):
            for b4 in range(len(self.b1)-a2):
                if self.b1[b4]<self.b1[b4+1]:
                    self.b1[b4],self.b1[b4+1] = self.b1[b4+1],self.b1[b4]
                    a1 +=1
            if a1 = = 0:
                break
            else:
                a2+=1
        return self.b1
def fonk5(list,a2):
    a3 = 0
    b2 = len(list)-1
    b3 = round(b2/2)
    while a3<b3 and b3 < b2:
        if a2 > list[b3] and b3 < b2:
            a3 = b3
        elif a2 < list[b3] and a3 < b3:
            b2 = b3
        elif a2 = = list[b3]:
            return b3
        b3 = round((a3+b2)/2)
        if a3 >= b2:
            return a3
        elif b3 >= b2:
            return b2
        elif a3 >= b3:
            return a3 +1
        else:
            continue
def fonk6(a2,list):
    b4 = len(list)
    if b4 = = 0:
        list.append(a2)
    elif b4 = = 1:
        if a2 >= list[0]:
            list.append(a2)
        elif a2 <list[0]:
            list.insert(0,a2)
    elif b4 = = 2:
        if a2 >= list[-1]:
            list.append(a2)
        elif a2 <= list[0]:
            list.insert(0,a2)
        else:
            list.insert(1,a2)
    elif b4 > 2:
        if a2 <= list[0]:
            list.insert(0,a2)
        elif a2 >= list[-1]:
            list.append(a2)
        elif list[0]<a2<list[-1]:
            b5 = fonk5(list,a2)
            list.insert(b5,a2)
    return list