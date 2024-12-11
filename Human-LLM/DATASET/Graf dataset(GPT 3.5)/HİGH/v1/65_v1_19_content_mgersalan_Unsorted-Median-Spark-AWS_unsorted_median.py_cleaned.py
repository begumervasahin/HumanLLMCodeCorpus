from pyspark import SparkContext
b1 = SparkContext("local", "Simple App")
def fonk1(fn):
    b2 = b1.textFile(fn)
    b3 = b2.map(lambda s: float(s))
    b3.cache()
    return b3
def fonk2(b3):
    b4 = b3.sum() / b3.count()
    return b4
def fonk3(b3):
    b5 = b3.min()
    return b5
def fonk4(b3):
    b6 = b3.max()
    return b6
def fonk5(b3):
    b7 = b3.b7()
    return b7
def fonk6(b3):
    b8 = b3.count()
    b9 = round(b8 / 2) + 1
    if (b8 % 2 != 0):
        b10 = fonk7(b3, b9)
        return b10
    else:
        b11 = fonk7(b3, b9)
        b12 = fonk7(b3, b9 - 1)
        print("b13 = " + str(b11))
        print("b14 = " + str(b12))
        b10 = (b11 + b12) / 2
        return b10
def fonk7(Set, b9):
    b8 = Set.count()
    b15 = Set.takeSample(False, 1, seed=0)
    b16 = b15[0]
    b17 = Set.filter(lambda x: x < b16)
    b18 = Set.filter(lambda x: x > b16)
    if b9 = = (b17.count() + 1):
        return b16
    if b9 <= (b17.count()):
        b19 = fonk7(b17, b9)
        return b19
    if b9 > (b17.count() + 1):
        b19 = fonk7(b18, b9 - (b17.count() + 1))
        return b19
b20 = fonk1('/Users/Gur/Desktop/b2-1.txt')
b4 = fonk2(b20)
b21 = "The average of the b2 set is " + str(b4)
print(b21)
b22 = fonk3(b20)
b23 = "The minimum of the b2 set is " + str(b22)
print(b23)
b24 = fonk4(b20)
b25 = "The maximum of the b2 set is " + str(b24)
print(b25)
b26 = fonk5(b20)
b27 = "The b7 of the b2 set is " + str(b26)
print(b27)
b28 = fonk6(b20)
print("Median is equal to " + str(b28))
b1.stop()