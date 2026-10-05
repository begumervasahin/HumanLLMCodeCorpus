from pyspark import SparkContext
b1 = SparkContext("local", "Simple App")
def fonk1(file_path):
    b2 = b1.textFile(file_path)
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
        b10 = (b11 + b12) / 2
        return b10
def fonk7(b3, b9):
    b13 = b3.takeSample(False, 1, seed=0)[0]
    b14 = b3.filter(lambda x: x < b13)
    b15 = b3.filter(lambda x: x > b13)
    if b9 = = (b14.count() + 1):
        return b13
    if b9 <= (b14.count()):
        b16 = fonk7(b14, b9)
        return b16
    if b9 > (b14.count() + 1):
        b16 = fonk7(b15, b9 - (b14.count() + 1))
        return b16
b17 = fonk1('/Users/Gur/Desktop/b2-1.txt')
b4 = fonk2(b17)
b18 = "The average of the b2 set is " + str(b4)
print(b18)
b19 = fonk3(b17)
b20 = "The minimum of the b2 set is " + str(b19)
print(b20)
b21 = fonk4(b17)
b22 = "The maximum of the b2 set is " + str(b21)
print(b22)
b23 = fonk5(b17)
b24 = "The b7 of the b2 set is " + str(b23)
print(b24)
b25 = fonk6(b17)
print("Median is equal to " + str(b25))
b1.stop()