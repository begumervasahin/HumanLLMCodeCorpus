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
def fonk2((user, b10)):
    (movie1, rating1) = b10[0]
    (movie2, rating2) = b10[1]
    return ((movie1, movie2), (rating1, rating2))
def fonk3( (userID, b10) ):
    (movie1, rating1) = b10[0]
    (movie2, rating2) = b10[1]
    return movie1 < movie2
def fonk4(ratingPairs):
    a1 = 0
    b3 = sum_yy = sum_xy = 0
    for ratingX, ratingY in ratingPairs:
        b3 += ratingX * ratingX
        sum_yy += ratingY * ratingY
        sum_xy += ratingX * ratingY
        a1 += 1
    b4 = sum_xy
    b5 = sqrt(b3) * sqrt(sum_yy)
    a2 = 0
    if (b5):
        a2 = (b4 / (float(b5)))
    return (a2, a1)
b6 = SparkConf()
b7 = SparkContext(b6 = b6)
print("\nLoading movie names...")
b8 = fonk1()
b9 = b7.textFile("s3n:
b10 = b9.map(lambda l: l.split("::")).map(lambda l: (int(l[0]), (int(l[1]), float(l[2]))))
b11 = b10.partitionBy(100)
b12 = b11.join(b11)
b13 = b12.filter(filterDuplicates)
b14 = b13.map(makePairs).partitionBy(100)
b15 = b14.groupByKey()
b16 = b15.mapValues(computeCosineSimilarity).persist()
b16.sortByKey()
b16.saveAsTextFile("movie-sims")
if (len(sys.argv) > 1):
    a3 = 0.97
    a4 = 1000
    b17 = int(sys.argv[1])
    b18 = b16.filter(lambda((pair,sim)): \
        (pair[0] == b17 or pair[1] == b17) \
        and sim[0] > a3 and sim[1] > a4)
    b19 = b18.map(lambda((pair,sim)): (sim, pair)).sortByKey(ascending = False).take(10)
    print("Top 10 similar movies for " + b8[b17])
    for result in b19:
        (sim, pair) = result
        b20 = pair[0]
        if (b20 = = b17):
            b20 = pair[1]
        print(b8[b20] + "\tscore: " + str(sim[0]) + "\tstrength: " + str(sim[1]))