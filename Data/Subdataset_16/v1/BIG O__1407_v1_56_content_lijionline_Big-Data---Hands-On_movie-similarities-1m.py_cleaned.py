import sys
from pyspark import SparkConf, SparkContext
from math import sqrt
def fonk1():
    b1 = {}
    with open("movies.dat", b2 = "ascii", errors="ignore") as f:
        for line in f:
            b3 = line.strip().split("::")
            b1[int(b3[0])] = b3[1]
    return b1
def fonk2(user_ratings):
    b4 = list(user_ratings[1])
    (movie1, rating1) = b4[0]
    (movie2, rating2) = b4[1]
    return ((movie1, movie2), (rating1, rating2))
def fonk3(user_ratings):
    b4 = list(user_ratings[1])
    (movie1, rating1) = b4[0]
    (movie2, rating2) = b4[1]
    return movie1 < movie2
def fonk4(rating_pairs):
    a1 = 0
    b5 = sum_yy = sum_xy = 0
    for rating_x, rating_y in rating_pairs:
        b5 += rating_x * rating_x
        sum_yy += rating_y * rating_y
        sum_xy += rating_x * rating_y
        a1 += 1
    b6 = sum_xy
    b7 = sqrt(b5) * sqrt(sum_yy)
    a2 = 0
    if b7:
        a2 = (b6 / float(b7))
    return (a2, a1)
def fonk5():
    b8 = SparkConf().setAppName("MovieSimilarities")
    b9 = SparkContext(b8=b8)
    print("\nLoading movie names...")
    b10 = fonk1()
    b11 = b9.textFile("s3n:
    b4 = b11.map(lambda l: l.split("::")) \
                  .map(lambda l: (int(l[0]), (int(l[1]), float(l[2]))))
    b12 = b4.partitionBy(100)
    b13 = b12.join(b12)
    b14 = b13.filter(filter_duplicates)
    b15 = b14.map(make_pairs).partitionBy(100)
    b16 = b15.groupByKey()
    b17 = b16.mapValues(compute_cosine_similarity).persist()
    b17.sortByKey()
    b17.saveAsTextFile("movie-sims")
    if len(sys.argv) > 1:
        a3 = 0.97
        a4 = 1000
        b18 = int(sys.argv[1])
        b19 = b17.filter(lambda pair_sim: \
            (pair_sim[0][0] == b18 or pair_sim[0][1] == b18) \
            and pair_sim[1][0] > a3 and pair_sim[1][1] > a4)
        b20 = b19.map(lambda pair_sim: (pair_sim[1], pair_sim[0])) \
                                  .sortByKey(b21 = False) \
                                  .take(10)
        print(f"Top 10 similar movies for {b10[b18]}")
        for result in b20:
            (sim, pair) = result
            b22 = pair[0]
            if b22 = = b18:
                b22 = pair[1]
            print(f"{b10[b22]}\tscore: {sim[0]}\tstrength: {sim[1]}")
if b23 = = "__main__":
    fonk5()