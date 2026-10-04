import sys
from pyspark import SparkConf, SparkContext
from math import sqrt
def load_movie_names():
    movie_names = {}
    with open("movies.dat", encoding="ascii", errors="ignore") as file:
        for line in file:
            fields = line.strip().split("::")
            movie_names[int(fields[0])] = fields[1]
    return movie_names
def make_pairs(user_ratings):
    ratings = list(user_ratings[1])
    (movie1, rating1), (movie2, rating2) = ratings[0], ratings[1]
    return ((movie1, movie2), (rating1, rating2))
def filter_duplicates(user_ratings):
    ratings = list(user_ratings[1])
    movie1, movie2 = ratings[0][0], ratings[1][0]
    return movie1 < movie2
def compute_cosine_similarity(rating_pairs):
    num_pairs = 0
    sum_xx, sum_yy, sum_xy = 0, 0, 0
    for rating_x, rating_y in rating_pairs:
        sum_xx += rating_x * rating_x
        sum_yy += rating_y * rating_y
        sum_xy += rating_x * rating_y
        num_pairs += 1
    denominator = sqrt(sum_xx) * sqrt(sum_yy)
    score = (sum_xy / float(denominator)) if denominator else 0
    return (score, num_pairs)
def main():
    conf = SparkConf().setAppName("MovieSimilarities")
    sc = SparkContext(conf=conf)
    print("\nLoading movie names...")
    name_dict = load_movie_names()
    data = sc.textFile("s3n:
    ratings = data.map(lambda line: line.split("::")) \
                  .map(lambda fields: (int(fields[0]), (int(fields[1]), float(fields[2]))))
    ratings_partitioned = ratings.partitionBy(100)
    joined_ratings = ratings_partitioned.join(ratings_partitioned)
    unique_joined_ratings = joined_ratings.filter(filter_duplicates)
    movie_pairs = unique_joined_ratings.map(make_pairs).partitionBy(100)
    movie_pair_ratings = movie_pairs.groupByKey()
    movie_pair_similarities = movie_pair_ratings.mapValues(compute_cosine_similarity).persist()
    movie_pair_similarities.saveAsTextFile("movie-sims")
    if len(sys.argv) > 1:
        score_threshold = 0.97
        co_occurrence_threshold = 1000
        movie_id = int(sys.argv[1])
        filtered_results = movie_pair_similarities.filter(lambda pair_sim: \
            (pair_sim[0][0] == movie_id or pair_sim[0][1] == movie_id) \
            and pair_sim[1][0] > score_threshold and pair_sim[1][1] > co_occurrence_threshold)
        results = filtered_results.map(lambda pair_sim: (pair_sim[1], pair_sim[0])) \
                                  .sortByKey(ascending=False) \
                                  .take(10)
        print(f"Top 10 similar movies for {name_dict[movie_id]}:")
        for similarity, pair in results:
            similar_movie_id = pair[1] if pair[0] == movie_id else pair[0]
            print(f"{name_dict[similar_movie_id]}\tscore: {similarity[0]}\tstrength: {similarity[1]}")
if __name__ == "__main__":
    main()