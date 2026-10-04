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
    if len(b4) > 4 and b4[4]:
        return b4[4].split(" ")[0]
    return None
def fonk3():
    b5 = time.time()
    b6 = SparkConf().setAppName('UkMakerSpaces').setMaster("local[*]")
    b7 = SparkContext(b6=b6)
    b7.setLogLevel("ERROR")
    b8 = fonk1("data/uk-postcode.csv")
    b9 = b7.textFile("data/uk-makerspaces-identifiable-data.csv")
    b10 = b9 \
        .filter(lambda line: line.split(class1.b1)[0] != "Timestamp") \
        .map(lambda line: b8.get(fonk2(line), "Unknown"))
    b11 = b10.countByValue()
    for region, count in b11.items():
        print(f"{region}: {count}")
    print("\nExecution time")
    print(f"--- {time.time() - b5} seconds ---")
if b12 = = "__main__":
    fonk3()