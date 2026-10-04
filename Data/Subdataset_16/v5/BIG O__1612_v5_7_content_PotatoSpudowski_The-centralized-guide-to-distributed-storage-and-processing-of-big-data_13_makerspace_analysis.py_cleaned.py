import sys
import time
from pyspark import SparkContext, SparkConf
from utilities.Utils import Utils
def fonk1(file_path):
    with open(file_path, "r") as f:
        b1 = f.read().split("\n")
    return {line.split(',')[0]: line.split(',')[7] for line in b1 if line}
def fonk2(line):
    b2 = line.split(',')[4]
    return b2.split(" ")[0] if b2 else None
def fonk3():
    b3 = time.time()
    b4 = SparkConf().setAppName('UkMakerSpaces').setMaster("local[*]")
    b5 = SparkContext(b4=b4)
    b5.setLogLevel("ERROR")
    b6 = fonk1("data/uk-b2.csv")
    b7 = b5.textFile("data/uk-makerspaces-identifiable-data.csv")
    b8 = b7 \
        .filter(lambda line: line.split(',')[0] != "Timestamp") \
        .map(lambda line: b6.get(fonk2(line), "Unknown"))
    b9 = b8.countByValue()
    for region, count in b9.items():
        print(f"{region}: {count}")
    print("\nExecution time")
    print(f"--- {time.time() - b3} seconds ---")
if b10 = = "__main__":
    fonk3()