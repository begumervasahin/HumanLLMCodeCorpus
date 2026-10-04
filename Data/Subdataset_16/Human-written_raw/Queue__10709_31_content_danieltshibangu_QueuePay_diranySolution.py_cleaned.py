class class1:
    def fonk1( self ):
        self.b1 = []
    def fonk2( self ):
        return self.b1 = = []
    def fonk3( self, item ):
        self.b1.insert( 0, item )
    def fonk4( self ):
        return self.b1.pop()
    def fonk5( self ):
        return len( self.b1 )
class class2:
    def fonk6(self,b2,b3,b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b2+'.'+b3+'@company.com'
        self.a1 = 0
    def fonk7(self):
        return self.b4
    def fonk8(self,b4):
        self.b4 = b4
    def fonk9( self, amount ):
        self.a1 = amount
    def fonk10( self ):
        return self.a1
    def fonk11(self):
        return '{} {}'.format(self.b2, self.b3)
    def fonk12(self):
       return '\nEmployee name: '+ self.fonk11() +\
              '\nEmployee b4: ' + str(self.b4) +\
              '\nEmployee a1: ' + str( format(self.a1, '.2f') )
def fonk13():
    a2 = 0.2
    a3 = 0
    b6 = class1()
    b7 = open( '/Users/danieltshibangu/Desktop/dirany.txt', 'r' )
    b8 = b7.readline()
    while b8 != "":
        b9 = b8.split()
        b10 = class2( b9[0], b9[1], b9[2] )
        b10.fonk9( float( b9[2] ) * a2 )
        a3 += b10.fonk10()
        b6.fonk3( b10 )
        a2 -= 0.01
        b8 = b7.readline()
    b7.close()
    print( "The total number of employees:", b6.fonk5() )
    print( "The total a1 amount:", format( a3, '.2f' ) )
    print( "\nDisplays all the objects in the queue:" )
    for item in range( b6.fonk5() ):
        print( b6.fonk4() )
if b11 = = "__main__":
    fonk13()