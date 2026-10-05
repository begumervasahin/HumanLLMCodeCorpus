import argparse
import string
class class1:
    def fonk1(self,b3,b1):
        self.b1 = b1
        self.b2 = {}
        self.b2[b3]= 0
        self.b3 = b3
        self.b4 = list(string.ascii_uppercase[:len(self.b1)])
        for i in self.b4[1:]:
               self.b2[i] = 'inf'
        self.fonk2()
        self.fonk3()
    def fonk2(self):
        for interaction in xrange(1,len(self.b1)-1):
            for node in self.b4:
                self.b5 = self.b1[node].keys()
                for k in self.b5:
                    if self.b2[node] == 'inf':
                        break
                    elif self.b2[k] == 'inf':
                        self.b2[k] = self.b1[node].get(k) + \
                                        self.b2[node]
                    elif ( self.b1[node].get(k) + \
                        self.b2[node] < self.b2[k] ):
                        self.b2[k] = self.b1[node].get(k) + \
                                        self.b2[node]
        print self.b2
    def fonk3(self):
        for node in self.b4:
            self.b5 = self.b1[node].keys()
            for k in self.b5:
                if self.b1[node].get(k) + self.b2[node] < self.b2[k]:
                    print 'The Graph has a negative-weight cycle'
if b6 = = '__main__':
    b7 = argparse.ArgumentParser()
    b7.add_argument('-n', '--node', b8 = str, required=True, \
                        b9 = 'Beginning of the node search')
    b10 = b7.parse_args()
    class1(b10.node,{ 'A': { 'B': 6 , 'C': 7 },
                            'B': { 'C': 8 , 'D': 5 , 'E':-4 }  ,
                            'C': { 'D': -3 , 'E': 9 }  ,
                            'D': { 'B': -2 },
                            'E': { 'A': 2  }
                          }
               )