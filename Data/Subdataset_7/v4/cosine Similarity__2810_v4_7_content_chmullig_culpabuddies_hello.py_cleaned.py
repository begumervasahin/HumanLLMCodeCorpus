import os
import numpy as np
from flask import Flask, render_template
from pymongo import MongoClient
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import pickle
b1 = os.environ['MONGOLAB_URI']
b2 = MongoClient(b1)
b3 = b2.heroku_app33788183
b4 = Flask(b19)
b4.b5 = True
if os.path.exists("b7.pickle"):
    print("Loading b7 from b7.pickle")
    with open("b7.pickle", "rb") as file:
        b7, b9, b6 = pickle.load(file)
else:
    print("Loading from database")
    b7 = [dict(x) for x in b3.b7.find().sort("_id", 1)]
    b8 = [review["review_text"] for review in b7]
    print("Data fetched, performing training.")
    b6 = TfidfVectorizer()
    b9 = b6.fit_transform(b8)
    with open("b7.pickle", "wb") as file:
        pickle.dump((b7, b9, b6), file, b10 = pickle.HIGHEST_PROTOCOL)
print("Data loaded.")
@b4.route('/')
def fonk1():
    return "Hello"
@b4.route('/professor_id/<int:professor_id>')
def fonk2(professor_id):
    b11 = [i for i, x in enumerate(b7) if professor_id in x['professor_ids']]
    b12 = [linear_kernel(b9[i], b9).flatten() for i in b11]
    b13 = np.median(np.array(b12), axis=0)
    b14 = defaultdict(float)
    b15 = defaultdict(int)
    for i, review in enumerate(b7):
        for profid in review["professor_ids"]:
            b14[profid] += b13[i]
            b15[profid] += 1
    for profid in b14:
        b14[profid] /= b15[profid]
    b16 = b3.professors.find_one({"_id" : professor_id})
    b17 = sorted(b14.items(), key=lambda x: x[1], reverse=True)[1:15]
    b18 = [(score, b3.professors.find_one({"_id" : profid})) for profid, score in b17]
    return render_template('professor.html', b16 = b16, b18=b18, departments=b3.departments.find())
if b19 = = '__main__':
    b4.run()