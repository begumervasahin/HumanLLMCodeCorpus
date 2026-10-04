from pyspark import SparkConf, SparkContext
import sys
import re
ALL_MOVIES = 'hdfs:
TEST_OUTPUT = 'hdfs:
IMDB_FILE = 'hdfs:
def create_y(spark):
    imdb_data = spark.textFile(IMDB_FILE)
    movie_data = spark.textFile(ALL_MOVIES)
    imdb_data = (imdb_data.map(get_imdb_fields)
                           .filter(lambda x: len(x) == 5)
                           .keyBy(lambda x: (x[0], get_int_clean(x[1]))))
    movie_data = (movie_data.map(get_fields)
                             .filter(lambda x: has_name_and_year(x[1], x[2]))
                             .map(lambda x: (x[1], x[2]))
                             .keyBy(lambda x: (x[0], get_int_clean(x[1]))))
    (movie_data.join(imdb_data)
               .map(lambda key_info: tuple(key_info[1][1]))
               .distinct()
               .saveAsTextFile(TEST_OUTPUT))
def has_name_and_year(title, year):
    return title != "" and len(year) == 4
def get_int_clean(item):
    try:
        return int(re.findall(r'\d{4}', item).pop())
    except Exception:
        return 0
def get_fields(text):
    return eval(text)
def get_imdb_fields(text):
    return [x.strip() for x in text.split('|')]
if __name__ == '__main__':
    conf = SparkConf()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'local':
            conf.setMaster("local[3]")
            print('Running locally')
        elif sys.argv[1] == 'cluster':
            conf.setMaster("spark:
            print('Running on cluster')
    conf.set("spark.executor.memory", "10g")
    conf.set("spark.driver.memory", "10g")
    spark = SparkContext(conf=conf)
    create_y(spark)