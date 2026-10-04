def fonk1(b3):
    b1 = sorted(((x,y) for x in range(b3) for y in range(b3)),
                    b2 = lambda (x,y): (x+y, -y if (x+y) % 2 else y) )
    return {index: b3 for b3,index in enumerate(b1)}
def fonk2(myarray):
    b3 = int(len(myarray)** 0.5 +0.5)
    for x in range(b3):
        for y in range(b3):
                print "%2i" % myarray[(x,y)],
        print
fonk2(fonk1(6))