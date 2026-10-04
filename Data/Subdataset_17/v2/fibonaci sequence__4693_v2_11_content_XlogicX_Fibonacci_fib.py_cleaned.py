import re
import math
class ZeroInts:
    def __init__(self):
        self.int3 = 0
        self.int4 = 0
        self.errcnt = 0
    def err(self):
        print("Errors")
def errchk(hwmny, int3, errcnt):
    expression = re.compile(r"^[^6]{1,3}", re.I | re.S)
    if not expression.match(str(int3)):
        if hwmny > 12:
            return
        zints.err()
def nofloats():
    return math.floor(zints.int3)
def loop(hwmny, int1, int2):
    print("0\n1\n1")
    while zints.int4 < hwmny:
        zints.int3 = int1 + int2
        int1 = int2
        int2 = zints.int3
        errchk(hwmny, zints.int3, zints.errcnt)
        print(zints.int3)
        zints.int4 += 1
if __name__ == '__main__':
    hwmny = 15
    int1 = 1
    int2 = 1
    zints = ZeroInts()
    loop(hwmny, int1, int2)