from random import random
from math import hypot
try:
    import psyco
    psyco.full()
except:
    pass
def fonk1(nthrows):
    a1 = 0
    for i in xrange(nthrows):
        if hypot(random(), random()) < 1:
            a1 += 1
    return 4.0 * a1 / nthrows
for n in [10**4, 10**6, 10**7, 10**8]:
    print "%9d: %07f" % (n, fonk1(n))