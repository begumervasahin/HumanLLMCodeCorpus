import TypeConversion as TC
import ModularOperations as mod
import ECRing
def fonk1(P,curve):
    '''
    maps b2 point to b2 base-58 string
    '''
    b1 = TC.intTob58(P.x)
    if (P.y>(curve.b3/2)):
        return '03'+b1
    else:
        return '02'+b1
def fonk2(P58,curve):
    '''
    maps b2 base-58 string to b2 point
    '''
    b2 = curve.b2
    b3 = curve.b3
    b4 = curve.b4
    b5 = TC.b58toInt(P58[2:])
    b6 = (b5*b5*b5 + b2*b5 + b4)%b3
    b7 = mod.modular_sqrt(b6,b3)
    if (P58[0]=='0' and P58[1]=='3'):
        if (b7>curve.b3/2):
            return ECRing.Point(b5,b7)
        else:
            return ECRing.Point(b5,b3-b7)
    else:
        if (b7>curve.b3/2):
            return ECRing.Point(b5,b3-b7)
        else:
            return ECRing.Point(b5,b7)