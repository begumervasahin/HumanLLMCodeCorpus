from pyspark import SparkConf, SparkContext
import sys
import re
all_movies_path = 'hdfs:
test_path = 'hdfs:
imdb_file_path = 'hdfs:
def create_actor_experience(spark):
    imdb_data = spark.textFile(imdb_file_path)
    movie_data = spark.textFile(all_movies_path)
    imdb_data = imdb_data.map(parse_imdb_data)\
                         .filter(filter_imdb_data)\
                         .keyBy(lambda x: (x[0], get_clean_year(x[1])))
    movie_data = movie_data.map(parse_movie_data)\
                           .filter(filter_movie_data)\
                           .map(lambda x: (x[1], x[2]))\
                           .keyBy(lambda x: (x[0], get_clean_year(x[1])))
    movie_data.join(imdb_data)\
              .map(lambda key, (key2, info): tuple(info))\
              .distinct()\
              .saveAsTextFile(test_path)
def filter_imdb_data(item):
    return len(item) == 5
def filter_movie_data(item):
    title, year = item[1], item[2]
    return title != "" and len(year) == 4
def get_clean_year(item):
    try:
        year = int(re.findall(r'\d{4}', item).pop())
    except Exception as e:
        return 0
    return year
def parse_imdb_data(item):
    return item.split('\t')
def parse_movie_data(item):
    fields = item.split('\t')
    return fields[1], fields[2], fields[3]
if __name__ == '__main__':
    conf = SparkConf()
    if sys.argv[1] == 'local':
        conf.setMaster("local[3]")
        print('Running locally')
    elif sys.argv[1] == 'cluster':
        conf.setMaster("spark:
        print('Running on cluster')
    conf.set("spark.executor.memory", "10g")
    conf.set("spark.driver.memory", "10g")
    spark = SparkContext(conf=conf)
    create_actor_experience(spark)