import sys
from pyspark import SparkConf, SparkContext
from math import sqrt
def fonk1():
    b1 = {}
    with open("movies.dat", b2 = "ascii", errors="ignore") as file:
        for line in file:
            b3 = line.strip().split("::")
            b1[int(b3[0])] = b3[1]
    return b1
def fonk2(user_ratings):
    b4 = list(user_ratings[1])
    (movie1, rating1), (b5, rating2) = b4[0], b4[1]
    return ((movie1, b5), (rating1, rating2))
def fonk3(user_ratings):
    b4 = list(user_ratings[1])
    movie1, b5 = b4[0][0], b4[1][0]
    return movie1 < b5
def fonk4(rating_pairs):
    a1 = 0
    sum_xx, sum_yy, b6 = 0, 0, 0
    for rating_x, rating_y in rating_pairs:
        sum_xx += rating_x * rating_x
        sum_yy += rating_y * rating_y
        b6 += rating_x * rating_y
        a1 += 1
    b7 = sqrt(sum_xx) * sqrt(sum_yy)
    b8 = (b6 / float(b7)) if b7 else 0
    return (b8, a1)
def fonk5():
    b9 = SparkConf().setAppName("MovieSimilarities")
    b10 = SparkContext(b9=b9)
    print("\nLoading movie names...")
    b11 = fonk1()
    b12 = b10.textFile("s3n:
    b4 = b12.map(lambda line: line.split("::")) \
                  .map(lambda b3: (int(b3[0]), (int(b3[1]), float(b3[2]))))
    b13 = b4.partitionBy(100)
    b14 = b13.join(b13)
    b15 = b14.filter(filter_duplicates)
    b16 = b15.map(make_pairs).partitionBy(100)
    b17 = b16.groupByKey()
    b18 = b17.mapValues(compute_cosine_similarity).persist()
    b18.saveAsTextFile("movie-sims")
    if len(sys.argv) > 1:
        a2 = 0.97
        a3 = 1000
        b19 = int(sys.argv[1])
        b20 = b18.filter(lambda pair_sim: \
            (pair_sim[0][0] == b19 or pair_sim[0][1] == b19) \
            and pair_sim[1][0] > a2 and pair_sim[1][1] > a3)
        b21 = b20.map(lambda pair_sim: (pair_sim[1], pair_sim[0])) \
                                  .sortByKey(b22 = False) \
                                  .take(10)
        print(f"Top 10 similar movies for {b11[b19]}:")
        for similarity, pair in b21:
            b23 = pair[1] if pair[0] == b19 else pair[0]
            print(f"{b11[b23]}\tscore: {similarity[0]}\tstrength: {similarity[1]}")
if b24 = = "__main__":
    fonk5()