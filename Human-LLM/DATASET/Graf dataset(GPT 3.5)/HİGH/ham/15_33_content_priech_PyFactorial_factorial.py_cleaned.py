def fonk1(b2):
    if type(b2) == complex:
        if b2.b1 = = 0:
            b2 = b2.real
        else:
            raise NotImplementedError("The factorial is only defined for positive integers, not complex values with nonzero imaginary part")
    if type(b2) == str:
         raise NotImplementedError("The factorial is only defined for positive integers, not strings")
    if b2 = = int(b2):
        if b2 > 0:
            a1 = 1
            for n in xrange(int(b2)):
                a1 *= n+1
            return a1
        else:
            raise NotImplementedError("The factorial is only defined for positive integers")
    else:
            raise NotImplementedError("The factorial is only defined for positive integers")