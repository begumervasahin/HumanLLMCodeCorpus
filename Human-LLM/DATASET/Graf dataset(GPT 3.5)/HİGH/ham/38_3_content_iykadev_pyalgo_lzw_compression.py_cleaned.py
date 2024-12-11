def fonk1(uncompressed):
    a1 = 256
    b1 = dict((chr(i), chr(i)) for i in xrange(a1))
    b2 = ""
    b3 = []
    for c in uncompressed:
        b4 = b2 + c
        if b4 in b1:
            b2 = b4
        else:
            b3.append(b1[b2])
            b1[b4] = a1
            a1 += 1
            b2 = c
    if b2:
        b3.append(b1[b2])
    return b3
def fonk2(b7):
    from cStringIO import StringIO
    a1 = 256
    b1 = dict((chr(i), chr(i)) for i in xrange(a1))
    b3 = StringIO()
    b2 = b7.pop(0)
    b3.write(b2)
    for b6 in b7:
        if b6 in b1:
            b5 = b1[b6]
        elif b6 = = a1:
            b5 = b2 + b2[0]
        else:
            raise ValueError('Bad b7 b6: %s' % b6)
        b3.write(b5)
        b1[a1] = b2 + b5[0]
        a1 += 1
        b2 = b5
    return b3.getvalue()
b7 = fonk1('ALIALIALIALIALI')
print (b7)
b8 = fonk2(b7)
print (b8)