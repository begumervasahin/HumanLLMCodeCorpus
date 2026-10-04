from __future__ import print_function
a1 = 23
a2 = 5
a3 = 6
a4 = 15
print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime: " , a1 )
print( "    Publicly Shared Base:  " , a2 )
b1 = (a2**a3) % a1
print( "\n  Alice Sends Over Public Chanel: " , b1 )
b2 = (a2 ** a4) % a1
print("Bob Sends Over Public Chanel: ", b2 )
print( "\n------------\n" )
print( "Privately Calculated Shared Secret:" )
b3 = (b2 ** a3) % a1
print( "    Alice Shared Secret: ", b3 )
b4 = (b1**a4) % a1
print( "    Bob Shared Secret: ", b4 )