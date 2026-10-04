import sys
import time
from pyspark import SparkContext, SparkConf
from utilities.Utils import Utils
def load_post_code_map(file_path):
    with open(file_path, "r") as f:
        lines = f.read().split("\n")
    return {line.split(',')[0]: line.split(',')[7] for line in lines if line}
def get_post_prefix(line):
    postcode = line.split(',')[4]
    return postcode.split(" ")[0] if postcode else None
def main():
    start_time = time.time()
    conf = SparkConf().setAppName('UkMakerSpaces').setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")
    post_code_map = load_post_code_map("data/uk-postcode.csv")
    maker_space_rdd = sc.textFile("data/uk-makerspaces-identifiable-data.csv")
    regions = maker_space_rdd \
        .filter(lambda line: line.split(',')[0] != "Timestamp") \
        .map(lambda line: post_code_map.get(get_post_prefix(line), "Unknown"))
    region_counts = regions.countByValue()
    for region, count in region_counts.items():
        print(f"{region}: {count}")
    print("\nExecution time")
    print(f"--- {time.time() - start_time} seconds ---")
if __name__ == "__main__":
    main()