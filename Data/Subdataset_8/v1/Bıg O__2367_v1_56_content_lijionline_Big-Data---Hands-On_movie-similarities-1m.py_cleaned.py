import sys
from pyspark import SparkConf, SparkContext
from math import sqrt
def loadMovieNames():
    movieNames = {}
    with open("movies.dat") as f:
        for line in f:
            fields = line.split("::")
            movieNames[int(fields[0])] = fields[1].decode('ascii', 'ignore')
    return movieNames
def makePairs(user_ratings):
    ratings = user_ratings[1]
    return [((ratings[i][0], ratings[j][0]), (ratings[i][1], ratings[j][1])) for i in range(len(ratings)) for j in range(i+1, len(ratings))]
def filterDuplicates(pair_rating):
    (movie1, rating1), (movie2, rating2) = pair_rating[1]
    return movie1 < movie2
def computeCosineSimilarity(ratingPairs):
    sum_xx = sum_yy = sum_xy = numPairs = 0
    for ratingX, ratingY in ratingPairs:
        sum_xx += ratingX * ratingX
        sum_yy += ratingY * ratingY
        sum_xy += ratingX * ratingY
        numPairs += 1
    numerator = sum_xy
    denominator = sqrt(sum_xx) * sqrt(sum_yy)
    score = numerator / denominator if denominator != 0 else 0
    return (score, numPairs)
conf = SparkConf().setAppName("MovieSimilarities")
sc = SparkContext(conf=conf)
print("\nLoading movie names...")
nameDict = loadMovieNames()
data = sc.textFile("s3n:
ratings = data.map(lambda l: l.split("::")).map(lambda l: (int(l[0]), (int(l[1]), float(l[2]))))
ratingsPartitioned = ratings.partitionBy(100)
joinedRatings = ratingsPartitioned.join(ratingsPartitioned).filter(filterDuplicates)
moviePairs = joinedRatings.flatMap(makePairs).partitionBy(100)
moviePairRatings = moviePairs.groupByKey().mapValues(list)
moviePairSimilarities = moviePairRatings.mapValues(computeCosineSimilarity).persist()
moviePairSimilarities.sortByKey()
moviePairSimilarities.saveAsTextFile("movie-sims")
if len(sys.argv) > 1:
    scoreThreshold = 0.97
    coOccurenceThreshold = 1000
    movieID = int(sys.argv[1])
    filteredResults = moviePairSimilarities.filter(lambda x: (x[0][0] == movieID or x[0][1] == movieID) \
                                                  and x[1][0] > scoreThreshold and x[1][1] > coOccurenceThreshold)
    results = filteredResults.map(lambda x: (x[1], x[0])).sortByKey(ascending=False).take(10)
    print("Top 10 similar movies for " + nameDict[movieID])
    for result in results:
        sim, pair = result
        similarMovieID = pair[0] if pair[0] != movieID else pair[1]
        print(nameDict[similarMovieID] + "\tscore: " + str(sim[0]) + "\tstrength: " + str(sim[1]))
sc.stop()