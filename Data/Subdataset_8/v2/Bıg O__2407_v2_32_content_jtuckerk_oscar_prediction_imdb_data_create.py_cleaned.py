from pyspark import SparkConf, SparkContext
import sys
import re
def create_actor_experience(spark):
    all_movies_path = 'hdfs:
    imdb_file_path = 'hdfs:
    output_path = 'hdfs:
    imdb_data = spark.textFile(imdb_file_path)
    movie_data = spark.textFile(all_movies_path)
    imdb_data = imdb_data.map(parse_imdb_fields) \
                         .filter(lambda x: is_correct_field_size(x, 5)) \
                         .keyBy(lambda x: (x[0], get_clean_year(x[1])))
    movie_data = movie_data.map(parse_movie_fields) \
                           .filter(lambda x: has_title_and_year(x[1], x[2])) \
                           .map(lambda x: (x[1], x[2])) \
                           .keyBy(lambda x: (x[0], get_clean_year(x[1])))
    movie_data.join(imdb_data) \
              .map(lambda key, (key2, info): tuple(info)) \
              .distinct() \
              .saveAsTextFile(output_path)
def is_correct_field_size(item, size):
    return len(item) == size
def has_title_and_year(title, year):
    return not (title == "" or len(year) != 4)
def get_clean_year(item):
    try:
        year = int(re.findall(r'\d{4}', item).pop())
    except Exception as e:
        return 0
    return year
def parse_movie_fields(text):
    return eval(text)
def parse_imdb_fields(text):
    text = text.split('|')
    fields = [x.strip() for x in text]
    return fields
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