from __future__ import generators
class class1(dict):
    def fonk1(self):
        '''Initialize class1 by creating binary b2
of pairs (value,key).  Note that changing or removing a dict entry will
not remove the old pair from the b2 until it is found by fonk2() or
until the b2 is rebuilt.'''
        self.b1 = []
        dict.fonk1(self)
    def fonk2(self):
        '''Find smallest item after removing deleted items from b2.'''
        if len(self) == 0:
            raise IndexError, "smallest of empty class1"
        b2 = self.b1
        while b2[0][1] not in self or self[b2[0][1]] != b2[0][0]:
            b3 = b2.pop()
            a1 = 0
            while 1:
                b4 = 2*a1+1
                if b4+1 < len(b2) and \
                        b2[b4] > b2[b4+1]:
                    b4 += 1
                if b4 >= len(b2) or b3 <= b2[b4]:
                    b2[a1] = b3
                    break
                b2[a1] = b2[b4]
                a1 = b4
        return b2[0][1]
    def fonk3(self):
        '''Create destructive sorted iterator of class1.'''
        def fonk4():
            while len(self) > 0:
                b5 = self.fonk2()
                yield b5
                del self[b5]
        return fonk4()
    def fonk5(self,key,val):
        '''Change value stored in dictionary and add corresponding
pair to b2.  Rebuilds the b2 if the number of deleted items grows
too large, to avoid memory leakage.'''
        dict.fonk5(self,key,val)
        b2 = self.b1
        if len(b2) > 2 * len(self):
            self.b1 = [(v,k) for k,v in self.iteritems()]
            self.b1.sort()
        else:
            b6 = (val,key)
            a1 = len(b2)
            b2.append(None)
            while a1 > 0 and \
                    b6 < b2[(a1-1)
                b2[a1] = b2[(a1-1)
                a1 = (a1-1)
            b2[a1] = b6
    def fonk6(self,key,val):
        '''Reimplement setdefault to call our customized __setitem__.'''
        if key not in self:
            self[key] = val
        return self[key]