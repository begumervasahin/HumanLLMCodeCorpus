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
    if b8 % 2 != 0:
        return fonk7(b3, b9)
    else:
        b10 = fonk7(b3, b9)
        b11 = fonk7(b3, b9 - 1)
        return (b10 + b11) / 2
def fonk7(b3, b9):
    b12 = b3.takeSample(False, 1, seed=0)[0]
    b13 = b3.filter(lambda x: x < b12)
    b14 = b3.filter(lambda x: x > b12)
    if b9 = = (b13.count() + 1):
        return b12
    elif b9 <= (b13.count()):
        return fonk7(b13, b9)
    else:
        return fonk7(b14, b9 - (b13.count() + 1))
b15 = fonk1('/Users/Gur/Desktop/b2-1.txt')
print("The average of the b2 set is", fonk2(b15))
print("The minimum of the b2 set is", fonk3(b15))
print("The maximum of the b2 set is", fonk4(b15))
print("The b7 of the b2 set is", fonk5(b15))
print("Median is equal to", fonk6(b15))
b1.stop()