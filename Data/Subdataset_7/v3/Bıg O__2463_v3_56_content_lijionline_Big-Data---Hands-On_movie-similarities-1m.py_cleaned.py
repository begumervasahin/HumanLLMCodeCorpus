import sys
from pyspark import SparkConf, SparkContext
from math import sqrt
def fonk1():
    b1 = {}
    with open("movies.dat") as f:
        for line in f:
            b2 = line.split("::")
            b1[int(b2[0])] = b2[1].decode('ascii', 'ignore')
    return b1
def fonk2(user_ratings):
    b3 = user_ratings[1]
    return [((b3[i][0], b3[j][0]), (b3[i][1], b3[j][1])) for i in range(len(b3)) for j in range(i + 1, len(b3))]
def fonk3(pair_rating):
    (movie1, rating1), (movie2, rating2) = pair_rating[1]
    return movie1 < movie2
def fonk4(rating_pairs):
    b4 = sum_yy = sum_xy = num_pairs = 0
    for ratingX, ratingY in rating_pairs:
        b4 += ratingX * ratingX
        sum_yy += ratingY * ratingY
        sum_xy += ratingX * ratingY
        num_pairs += 1
    b5 = sum_xy
    b6 = sqrt(b4) * sqrt(sum_yy)
    b7 = b5 / b6 if b6 != 0 else 0
    return (b7, num_pairs)
b8 = SparkConf().setAppName("MovieSimilarities")
b9 = SparkContext(b8=b8)
print("\nLoading movie names...")
b10 = fonk1()
b11 = b9.textFile("s3n:
b3 = b11.map(lambda l: l.split("::")).map(lambda l: (int(l[0]), (int(l[1]), float(l[2]))))
b12 = b3.partitionBy(100)
b13 = b12.join(b12).filter(filter_duplicates)
b14 = b13.flatMap(make_pairs).partitionBy(100)
b15 = b14.groupByKey().mapValues(list)
b16 = b15.mapValues(compute_cosine_similarity).persist()
b16.sortByKey()
b16.saveAsTextFile("movie-sims")
if len(sys.argv) > 1:
    a1 = 0.97
    a2 = 1000
    b17 = int(sys.argv[1])
    b18 = b16.filter(lambda x: (x[0][0] == b17 or x[0][1] == b17) \
                                                      and x[1][0] > a1 and x[1][1] > a2)
    b19 = b18.map(lambda x: (x[1], x[0])).sortByKey(ascending=False).take(10)
    print("Top 10 similar movies for " + b10[b17])
    for result in b19:
        sim, b20 = result
        b21 = b20[0] if b20[0] != b17 else b20[1]
        print(b10[b21] + "\tscore: " + str(sim[0]) + "\tstrength: " + str(sim[1]))
b9.stop()