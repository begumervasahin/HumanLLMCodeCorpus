import sys
import time
from pyspark import SparkContext, SparkConf
from utilities.Utils import Utils
def load_postcode_map():
    lines = open("data/uk-postcode.csv", "r").read().split("\n")
    splits_for_lines = [Utils.COMMA_DELIMITER.split(line) for line in lines if line != ""]
    return {splits[0]: splits[7] for splits in splits_for_lines}
def get_post_prefix(line: str):
    splits = Utils.COMMA_DELIMITER.split(line)
    postcode = splits[4]
    return None if not postcode else postcode.split(" ")[0]
def main():
    start_time = time.time()
    conf = SparkConf().setAppName('UkMakerSpaces').setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")
    post_code_map = load_postcode_map()
    maker_space_rdd = sc.textFile("data/uk-makerspaces-identifiable-data.csv")
    regions = maker_space_rdd \
        .filter(lambda line: Utils.COMMA_DELIMITER.split(line)[0] != "Timestamp") \
        .map(lambda line: post_code_map.get(get_post_prefix(line), "Unknown"))
    for region, count in regions.countByValue().items():
        print(region, str(count))
    print("\nExecution time")
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    main()