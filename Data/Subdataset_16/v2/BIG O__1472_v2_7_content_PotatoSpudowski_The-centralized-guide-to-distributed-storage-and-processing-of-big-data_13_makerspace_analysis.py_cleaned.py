import sys
import time
from pyspark import SparkContext, SparkConf
class class1:
    b1 = ','
def fonk1(file_path):
    with open(file_path, "r") as file:
        b2 = file.read().split("\n")
        b3 = [line.split(class1.b1) for line in b2 if line]
        return {b4[0]: b4[7] for b4 in b3}
def fonk2(line):
    b4 = line.split(class1.b1)
    b5 = b4[4]
    return b5.split(" ")[0] if b5 else None
def fonk3():
    b6 = time.time()
    b7 = SparkConf().setAppName('UkMakerSpaces').setMaster("local[*]")
    b8 = SparkContext(b7=b7)
    b8.setLogLevel("ERROR")
    b9 = fonk1("data/uk-b5.csv")
    b10 = b8.textFile("data/uk-makerspaces-identifiable-data.csv")
    b11 = b10 \
        .filter(lambda line: line.split(class1.b1)[0] != "Timestamp") \
        .map(lambda line: b9.get(fonk2(line), "Unknown"))
    b12 = b11.countByValue()
    for region, count in b12.items():
        print(f"{region}: {count}")
    print("\nExecution time")
    print(f"--- {time.time() - b6} seconds ---")
if b13 = = "__main__":
    fonk3()