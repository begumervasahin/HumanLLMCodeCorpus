from pyspark import SparkContext
def fonk1(file_name, b16):
    b1 = b16.textFile(file_name)
    b2 = b1.map(lambda s: float(s))
    b2.cache()
    return b2
def fonk2(b2):
    b3 = b2.sum() / b2.count()
    return b3
def fonk3(b2):
    b4 = b2.min()
    return b4
def fonk4(b2):
    b5 = b2.max()
    return b5
def fonk5(b2):
    b6 = b2.b6()
    return b6
def fonk6(b2):
    b7 = b2.count()
    b8 = round(b7 / 2) + 1
    if b7 % 2 != 0:
        b9 = fonk7(b2, b8)
        return b9
    else:
        b10 = fonk7(b2, b8)
        b11 = fonk7(b2, b8 - 1)
        b9 = (b10 + b11) / 2
        return b9
def fonk7(Set, b8):
    b12 = Set.takeSample(False, 1, seed=0)[0]
    b13 = Set.filter(lambda x: x < b12)
    b14 = Set.filter(lambda x: x > b12)
    if b8 = = (b13.count() + 1):
        return b12
    if b8 <= (b13.count()):
        b15 = fonk7(b13, b8)
        return b15
    if b8 > (b13.count() + 1):
        b15 = fonk7(b14, b8 - (b13.count() + 1))
        return b15
b16 = SparkContext()
b17 = fonk1('/Users/Gur/Desktop/b1-1.txt', b16)
b3 = fonk2(b17)
print("The average of the b1 set is", b3)
b18 = fonk3(b17)
print("The minimum of the b1 set is", b18)
b19 = fonk4(b17)
print("The maximum of the b1 set is", b19)
b20 = fonk5(b17)
print("The b6 of the b1 set is", b20)
b21 = fonk6(b17)
print("The b21 is equal to", b21)