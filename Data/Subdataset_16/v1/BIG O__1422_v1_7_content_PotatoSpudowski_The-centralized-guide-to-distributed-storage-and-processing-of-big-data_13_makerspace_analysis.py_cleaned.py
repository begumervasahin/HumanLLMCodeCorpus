import sys
import time
from pyspark import SparkContext, SparkConf
class class1:
    b1 = ','
def fonk1():
    b2 = open("data/uk-b5.csv", "r").read().split("\n")
    b3 = [class1.b1.split(line) for line in b2 if line != ""]
    return {b4[0]: b4[7] for b4 in b3}
def fonk2(line: str):
    b4 = class1.b1.split(line)
    b5 = b4[4]
    return None if not b5 else b5.split(" ")[0]
if b6 = = "__main__":
    b7 = time.time()
    b8 = SparkConf().setAppName('UkMakerSpaces').setMaster("local[*]")
    b9 = SparkContext(b8 = b8)
    b9.setLogLevel("ERROR")
    b10 = fonk1()
    b11 = b9.textFile("data/uk-makerspaces-identifiable-data.csv")
    b12 = b11 \
        .filter(lambda line: class1.b1.split(line)[0] != "Timestamp") \
        .map(lambda line: b10[fonk2(line)] \
        if fonk2(line) in b10 else "Unknown")
    for region, count in b12.countByValue().items():
        print(region, str(count))
    print("\nExecution time")
    print("--- %s seconds ---" % (time.time() - b7))