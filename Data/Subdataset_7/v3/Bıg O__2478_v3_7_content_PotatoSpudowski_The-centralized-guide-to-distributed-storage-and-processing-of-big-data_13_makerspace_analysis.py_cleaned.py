import sys
import time
from pyspark import SparkContext, SparkConf
from utilities.Utils import Utils
def fonk1():
    b1 = open("data/uk-b4.csv", "r").read().split("\n")
    b2 = [Utils.COMMA_DELIMITER.split(line) for line in b1 if line != ""]
    return {b3[0]: b3[7] for b3 in b2}
def fonk2(line):
    b3 = Utils.COMMA_DELIMITER.split(line)
    b4 = b3[4]
    return None if not b4 else b4.split(" ")[0]
b5 = time.time()
b6 = SparkConf().setAppName('UkMakerSpaces').setMaster("local[*]")
b7 = SparkContext(b6=b6)
b7.setLogLevel("ERROR")
b8 = fonk1()
b9 = b7.textFile("data/uk-makerspaces-identifiable-data.csv")
b10 = b9 \
    .filter(lambda line: Utils.COMMA_DELIMITER.split(line)[0] != "Timestamp") \
    .map(lambda line: b8[fonk2(line)] if fonk2(line) in b8 else "Unknown")
for region, count in b10.countByValue().items():
    print(region, str(count))
print("\nExecution time")
print("--- %s seconds ---" % (time.time() - b5))