import nltk
sentence = raw_input()
tokens = nltk.word_tokenize(sentence)
print(tokens)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words("english"))
filtered_tokens=[]
for w in tokens:
	if w not in stop_words:
		filtered_tokens.append(w)
print(filtered_tokens)
filtered_tokens = [w for w in tokens if w is not in stop_words]
from nltk.stem import PorterStemmer
ps = PosterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
	print(ps.stem(w))
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
def process_content():
	try:
		for i in tokenized:
			words= nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)
	except: Exception as e:
		print(str(e))
process_content()
"""
POS tag list:
CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
Identifiers:
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.
Modifiers:
{1,3} = for digits, u expect 1-3 counts of digits, or "places" example \d{1-3}
+ = match 1 or more
* = match 0 or MORE repetitions
? = match 0 or 1 repetitions.
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y example  \d{1,3} | \w{5,7}
[] = range, or "variance" example [1-5a-qA-Z]
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code
White Space Charts:
\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return
Characters to REMEMBER TO ESCAPE IF USED!
. + * ? [ ] $ ^ ( ) { } | \
Brackets:
[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z
Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}Chunk: {<.*>+}
						}<VB.? | IN | DT>+{"""
import re
examplestring = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''
ages = re.find_all(r'\d{1,3}',examplestring)
names = re.find_all(r'[A-Z][a-z]*',examplestring)
print(ages)
print(names)
def process_content():
	try:
		for i in tokenized:
			words= nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			namedEnt = nltk.ne_chunk(tagged)
			namedEnt.draw()
			print(tagged)
	except: Exception as e:
		print(str(e))
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better",pos="a"))
print(lemmatizer.lemmatize("run",'v'))
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)
from nltk.corpus import wordnet
syns = wordnet.synsets("program")
print(syns)
print(syns[0].lemmas()[0].name)
print(syns[0].definition())
print(syns[0].examples())
synonyms = []
antonyms = []
for syn in wordnet.syns("good"):
	for l in syn.lemma():
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))
import nltk
import random
from nltk.corpus import movie_reviews
documents = []
for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append(list(movie_reviews.words(fileid)),category)
random.shuffle(documents)
all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())
all_words=nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])
word_features = list(all_words.keys())[:3000]
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]
training_set = featuresets[:1900]
testing_set = featuresets[1900:]
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)
import pickle
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()