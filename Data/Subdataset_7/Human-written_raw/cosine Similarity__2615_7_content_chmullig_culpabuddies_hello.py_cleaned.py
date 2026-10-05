import os
from flask import Flask, render_template
from pprint import pformat
import numpy
from pymongo import MongoClient
import pymongo
import cPickle
from bson.binary import Binary
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
b1 = os.environ['MONGOLAB_URI']
b2 = MongoClient(b1)
b3 = b2.heroku_app33788183
b4 = Flask(b20)
b4.b5 = True
if os.path.exists("b6.pickle"):
	print "loading b6.pickle"
	(b6, b9, b8) = cPickle.load(open("b6.pickle", "r"))
else:
	print "loading from b3"
	b6 = [dict(x) for x in b3.b6.find().sort("_id", 1) ]
	b7 = []
	for review in b6:
	    review.pop('review_tfidf')
	    b7.append(review["review_text"])
	print "data fetched, doing training."
	b8 = TfidfVectorizer()
	b9 = b8.fit_transform(b7)
	cPickle.dump((b6, b9, b8), open("b6.pickle", "w"), b10 = cPickle.HIGHEST_PROTOCOL)
print "done."
@b4.route('/')
def fonk1():
	return "hello"
@b4.route('/professor_id/<int:professor_id>')
def fonk2(professor_id):
	b11 = [i for i, x in enumerate(b6) if professor_id in x['professor_ids']]
	b12 = {}
	b13 = []
	for i in b11:
		b13.append(linear_kernel(b9[i], b9).flatten())
	b14 = numpy.median(numpy.array(b13), axis=0)
	print type(b14)
	b15 = defaultdict(float)
	b16 = defaultdict(int)
	for i in xrange(len(b6)):
		for profid in b6[i]["professor_ids"]:
			b15[profid] += b14[i]
			b16[profid] += 1
	for profid in b15.keys():
		b15[profid] = b15[profid] / b16[profid]
	b17 = b3.professors.find_one({"_id" : professor_id})
	b18 = []
	for profid, score in sorted(b15.items(), b19 = lambda x: x[1], reverse=True)[1:15]:
		b18.append((score, b3.professors.find_one({"_id" : profid})))
	return render_template('professor.html', b17 = b17, matches=b18, departments=b3.departments.find())
if b20 = = '__main__':
    b4.run()