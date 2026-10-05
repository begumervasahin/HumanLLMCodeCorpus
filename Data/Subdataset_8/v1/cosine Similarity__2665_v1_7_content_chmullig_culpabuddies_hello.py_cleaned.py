import os
from flask import Flask, render_template
import numpy as np
from pymongo import MongoClient
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import pickle
mongouri = os.environ.get('MONGOLAB_URI')
client = MongoClient(mongouri)
db = client.heroku_app33788183
app = Flask(__name__)
app.debug = True
if os.path.exists("reviews.pickle"):
    print("Loading reviews from reviews.pickle")
    with open("reviews.pickle", "rb") as file:
        reviews, reviews_tfidf, tfidf_vect = pickle.load(file)
else:
    print("Fetching data from database")
    reviews = [dict(x) for x in db.reviews.find().sort("_id", 1)]
    review_texts = [review["review_text"] for review in reviews]
    print("Data fetched, performing training.")
    tfidf_vect = TfidfVectorizer()
    reviews_tfidf = tfidf_vect.fit_transform(review_texts)
    with open("reviews.pickle", "wb") as file:
        pickle.dump((reviews, reviews_tfidf, tfidf_vect), file, protocol=pickle.HIGHEST_PROTOCOL)
print("Data loaded.")
@app.route('/')
def index():
    return "hello"
@app.route('/professor_id/<int:professor_id>')
def professor(professor_id):
    source_reviews_idx = [i for i, x in enumerate(reviews) if professor_id in x['professor_ids']]
    pscore = {}
    grams = []
    for i in source_reviews_idx:
        grams.append(linear_kernel(reviews_tfidf[i], reviews_tfidf).flatten())
    gram = np.median(np.array(grams), axis=0)
    print(type(gram))
    prof_scores = defaultdict(float)
    prof_counts = defaultdict(int)
    for i in range(len(reviews)):
        for profid in reviews[i]["professor_ids"]:
            prof_scores[profid] += gram[i]
            prof_counts[profid] += 1
    for profid in prof_scores.keys():
        prof_scores[profid] = prof_scores[profid] / prof_counts[profid]
    prof = db.professors.find_one({"_id" : professor_id})
    ret = []
    for profid, score in sorted(prof_scores.items(), key=lambda x: x[1], reverse=True)[1:15]:
        ret.append((score, db.professors.find_one({"_id" : profid})))
    return render_template('professor.html', prof=prof, matches=ret, departments=db.departments.find())
if __name__ == '__main__':
    app.run()