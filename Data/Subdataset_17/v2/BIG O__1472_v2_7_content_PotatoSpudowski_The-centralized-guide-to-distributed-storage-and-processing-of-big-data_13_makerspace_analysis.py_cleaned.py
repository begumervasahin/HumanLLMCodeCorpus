import sys
import time
from pyspark import SparkContext, SparkConf
class Utils:
    COMMA_DELIMITER = ','
def load_post_code_map(file_path):
    with open(file_path, "r") as file:
        lines = file.read().split("\n")
        splits_for_lines = [line.split(Utils.COMMA_DELIMITER) for line in lines if line]
        return {splits[0]: splits[7] for splits in splits_for_lines}
def get_post_prefix(line):
    splits = line.split(Utils.COMMA_DELIMITER)
    postcode = splits[4]
    return postcode.split(" ")[0] if postcode else None
def main():
    start_time = time.time()
    conf = SparkConf().setAppName('UkMakerSpaces').setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")
    post_code_map = load_post_code_map("data/uk-postcode.csv")
    maker_space_rdd = sc.textFile("data/uk-makerspaces-identifiable-data.csv")
    regions = maker_space_rdd \
        .filter(lambda line: line.split(Utils.COMMA_DELIMITER)[0] != "Timestamp") \
        .map(lambda line: post_code_map.get(get_post_prefix(line), "Unknown"))
    region_counts = regions.countByValue()
    for region, count in region_counts.items():
        print(f"{region}: {count}")
    print("\nExecution time")
    print(f"--- {time.time() - start_time} seconds ---")
if __name__ == "__main__":
    main()