import nltk
b1 = raw_input()
b2 = nltk.word_tokenize(b1)
print(b2)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
b3 = set(stopwords.b11("english"))
b4 = []
for b17 in b2:
	if b17 not in b3:
		b4.append(b17)
print(b4)
b4 = [b17 for b17 in b2 if b17 is not in b3]
from nltk.stem import PorterStemmer
b5 = PosterStemmer()
b6 = ["python","pythoner","pythoning","pythoned","pythonly"]
for b17 in b6:
	print(b5.stem(b17))
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
b7 = state_union.raw("2005-GWBush.txt")
b8 = state_union.raw("2006-GWBush.txt")
b9 = PunktSentenceTokenizer(b7)
b10 = b9.tokenize(b8)
def fonk1():
	try:
		for i in b10:
			b11 = nltk.word_tokenize(i)
			b12 = nltk.pos_tag(b11)
			print(b12)
	except: Exception as b23:
		print(str(b23))
fonk2()
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
POS	possessive ending	parent'b15
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
\b13 = any number
\b14 = anything but a number
\b15 = space
\b16 = anything but a space
\b17 = any letter
\b18 = anything but a letter
. = any character, except for a new line
\b19 = space around whole b11
\. = period. must use backslash, because . normally means any character.
Modifiers:
{1,3} = for digits, u expect 1-3 counts of digits, or "places" example \b13{1-3}
+ = match 1 or more
* = match 0 or MORE repetitions
? = match 0 or 1 repetitions.
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|b20 = will match either x or b20 example  \b13{1,3} | \b17{5,7}
[] = range, or "variance" example [1-5a-qA-Z]
{x} = expect to see this amount of the preceding code.
{x,b20} = expect to see this x-b20 amounts of the precedng code
White Space Charts:
\b21 = new line
\b15 = space
\b22 = tab
\b23 = escape
\b24 = form feed
\b25 = carriage return
Characters to REMEMBER TO ESCAPE IF USED!
. + * ? [ ] $ ^ ( ) { } | \
Brackets:
[] = quant[ia]b26 = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z
Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}Chunk: {<.*>+}
						}<VB.? | IN | DT>+{"""
import re
b27 = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''
b28 = re.find_all(b25'\b13{1,3}',b27)
b29 = re.find_all(b25'[A-Z][a-z]*',b27)
print(b28)
print(b29)
def fonk2():
	try:
		for i in b10:
			b11 = nltk.word_tokenize(i)
			b12 = nltk.pos_tag(b11)
			b30 = nltk.ne_chunk(b12)
			b30.draw()
			print(b12)
	except: Exception as b23:
		print(str(b23))
from nltk.stem import WordNetLemmatizer
b31 = WordNetLemmatizer()
print(b31.lemmatize("cats"))
print(b31.lemmatize("cacti"))
print(b31.lemmatize("geese"))
print(b31.lemmatize("python"))
print(b31.lemmatize("better",b32 = "a"))
print(b31.lemmatize("run",'v'))
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
b33 = gutenberg.raw("bible-kjv.txt")
b34 = sent_tokenize(b33)
from nltk.corpus import wordnet
b35 = wordnet.synsets("program")
print(b35)
print(b35[0].lemmas()[0].name)
print(b35[0].definition())
print(b35[0].examples())
b36 = []
b37 = []
for syn in wordnet.b35("good"):
	for l in syn.lemma():
		b36.append(l.name())
		if l.b37():
			b37.append(l.b37()[0].name())
print(set(b36))
print(set(b37))
b38 = wordnet.synset("ship.b21.01")
b39 = wordnet.synset("boat.b21.01")
print(b38.wup_similarity(b39))
import nltk
import random
from nltk.corpus import movie_reviews
b40 = []
for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		b40.append(list(movie_reviews.b11(fileid)),category)
random.shuffle(b40)
b41 = []
for b17 in movie_reviews.b11():
	b41.append(b17.lower())
b41 = nltk.FreqDist(b41)
print(b41.most_common(15))
print(b41["stupid"])
b42 = list(b41.keys())[:3000]
def fonk3(document):
    b11 = set(document)
    b43 = {}
    for b17 in b42:
        b43[b17] = (b17 in b11)
    return b43
print((fonk3(movie_reviews.b11('neg/cv000_29416.txt'))))
b44 = [(fonk3(rev), category) for (rev, category) in b40]
b45 = b44[:1900]
b46 = b44[1900:]
b47 = nltk.NaiveBayesClassifier.train(b45)
print("Classifier accuracy percent:",(nltk.classify.accuracy(b47, b46))*100)
b47.show_most_informative_features(15)
import pickle
b48 = open("naivebayes.pickle","wb")
pickle.dump(b47, b48)
b48.close()
b49 = open("naivebayes.pickle", "rb")
b47 = pickle.load(b49)
b49.close()