import sys
from pyspark import SparkConf, SparkContext
from math import sqrt
def load_movie_names():
    movie_names = {}
    with open("movies.dat") as f:
        for line in f:
            fields = line.split("::")
            movie_names[int(fields[0])] = fields[1].decode('ascii', 'ignore')
    return movie_names
def make_pairs(user_ratings):
    ratings = user_ratings[1]
    return [((ratings[i][0], ratings[j][0]), (ratings[i][1], ratings[j][1])) for i in range(len(ratings)) for j in range(i + 1, len(ratings))]
def filter_duplicates(pair_rating):
    (movie1, rating1), (movie2, rating2) = pair_rating[1]
    return movie1 < movie2
def compute_cosine_similarity(rating_pairs):
    sum_xx = sum_yy = sum_xy = num_pairs = 0
    for ratingX, ratingY in rating_pairs:
        sum_xx += ratingX * ratingX
        sum_yy += ratingY * ratingY
        sum_xy += ratingX * ratingY
        num_pairs += 1
    numerator = sum_xy
    denominator = sqrt(sum_xx) * sqrt(sum_yy)
    score = numerator / denominator if denominator != 0 else 0
    return (score, num_pairs)
conf = SparkConf().setAppName("MovieSimilarities")
sc = SparkContext(conf=conf)
print("\nLoading movie names...")
name_dict = load_movie_names()
data = sc.textFile("s3n:
ratings = data.map(lambda l: l.split("::")).map(lambda l: (int(l[0]), (int(l[1]), float(l[2]))))
ratings_partitioned = ratings.partitionBy(100)
joined_ratings = ratings_partitioned.join(ratings_partitioned).filter(filter_duplicates)
movie_pairs = joined_ratings.flatMap(make_pairs).partitionBy(100)
movie_pair_ratings = movie_pairs.groupByKey().mapValues(list)
movie_pair_similarities = movie_pair_ratings.mapValues(compute_cosine_similarity).persist()
movie_pair_similarities.sortByKey()
movie_pair_similarities.saveAsTextFile("movie-sims")
if len(sys.argv) > 1:
    score_threshold = 0.97
    co_occurrence_threshold = 1000
    movie_id = int(sys.argv[1])
    filtered_results = movie_pair_similarities.filter(lambda x: (x[0][0] == movie_id or x[0][1] == movie_id) \
                                                      and x[1][0] > score_threshold and x[1][1] > co_occurrence_threshold)
    results = filtered_results.map(lambda x: (x[1], x[0])).sortByKey(ascending=False).take(10)
    print("Top 10 similar movies for " + name_dict[movie_id])
    for result in results:
        sim, pair = result
        similar_movie_id = pair[0] if pair[0] != movie_id else pair[1]
        print(name_dict[similar_movie_id] + "\tscore: " + str(sim[0]) + "\tstrength: " + str(sim[1]))
sc.stop()