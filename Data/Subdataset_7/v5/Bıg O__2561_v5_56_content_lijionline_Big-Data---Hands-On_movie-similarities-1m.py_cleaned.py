import sys
from pyspark import SparkConf, SparkContext
from math import sqrt
def fonk1():
    b1 = {}
    with open("movies.dat") as file:
        for line in file:
            b17, movie_name, b2 = line.strip().split("::")
            b1[int(b17)] = movie_name
    return b1
def fonk2(user_ratings):
    (movie1, rating1), (movie2, rating2) = user_ratings
    return ((movie1, movie2), (rating1, rating2))
def fonk3(user_ratings):
    (movie1, b2), (movie2, b2) = user_ratings
    return movie1 < movie2
def fonk4(rating_pairs):
    b3 = sum_xx = sum_yy = sum_xy = 0
    for rating_x, rating_y in rating_pairs:
        sum_xx += rating_x * rating_x
        sum_yy += rating_y * rating_y
        sum_xy += rating_x * rating_y
        b3 += 1
    b4 = sum_xy
    b5 = sqrt(sum_xx) * sqrt(sum_yy)
    a1 = 0
    if b5:
        a1 = b4 / float(b5)
    return (a1, b3)
b6 = SparkConf().setAppName("MovieSimilarities")
b7 = SparkContext(b6=b6)
print("\nLoading movie names...")
b8 = fonk1()
b9 = b7.textFile("s3n:
b10 = b9.map(lambda line: line.split("::")).map(lambda line: (int(line[0]), (int(line[1]), float(line[2]))))
b11 = b10.partitionBy(100)
b12 = b11.join(b11)
b13 = b12.filter(filter_duplicates)
b14 = b13.map(make_pairs).partitionBy(100)
b15 = b14.groupByKey()
b16 = b15.mapValues(compute_cosine_similarity).persist()
b16.sortByKey()
b16.saveAsTextFile("movie-sims")
if len(sys.argv) > 1:
    a2 = 0.97
    a3 = 1000
    b17 = int(sys.argv[1])
    b18 = b16.filter(lambda pair_sim: \
        (pair_sim[0][0] == b17 or pair_sim[0][1] == b17) \
        and pair_sim[1][0] > a2 and pair_sim[1][1] > a3)
    b19 = b18.map(lambda pair_sim: (pair_sim[1], pair_sim[0])).sortByKey(ascending=False).take(10)
    print("Top 10 similar movies for " + b8[b17])
    for result in b19:
        (similarity, pair) = result
        b20 = pair[0] if pair[0] != b17 else pair[1]
        print(b8[b20] + "\tscore: " + str(similarity[0]) + "\tstrength: " + str(similarity[1]))