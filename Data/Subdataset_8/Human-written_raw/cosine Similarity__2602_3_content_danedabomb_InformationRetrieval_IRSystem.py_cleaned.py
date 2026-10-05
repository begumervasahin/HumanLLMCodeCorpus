import json
import math
import os
import re
import sys
from PorterStemmer import PorterStemmer
from collections import defaultdict, Counter
class IRSystem:
    def __init__(self):
        self.titles = []
        self.docs = []
        self.vocab = []
        self.alphanum = re.compile('[^a-zA-Z0-9]')
        self.p = PorterStemmer()
    def get_uniq_words(self):
        uniq = set()
        for doc in self.docs:
            for word in doc:
                uniq.add(word)
        return uniq
    def __read_raw_data(self, dirname):
        print("Stemming Documents...")
        titles = []
        docs = []
        os.mkdir('%s/stemmed' % dirname)
        title_pattern = re.compile('(.*) \d+\.txt')
        filenames = []
        for filename in os.listdir('%s/raw' % dirname):
            if filename.endswith(".txt") and not filename.startswith("."):
                filenames.append(filename)
        for i, filename in enumerate(filenames):
            title = title_pattern.search(filename).group(1)
            print("    Doc %d of %d: %s" % (i+1, len(filenames), title))
            titles.append(title)
            contents = []
            f = open('%s/raw/%s' % (dirname, filename), 'r')
            of = open('%s/stemmed/%s.txt' % (dirname, title), 'w')
            for line in f:
                line = line.lower()
                line = [xx.strip() for xx in line.split()]
                line = [self.alphanum.sub('', xx) for xx in line]
                line = [xx for xx in line if xx != '']
                line = [self.p.stem(xx) for xx in line]
                contents.extend(line)
                if len(line) > 0:
                    of.write(" ".join(line))
                    of.write('\n')
            f.close()
            of.close()
            docs.append(contents)
        return titles, docs
    def __read_stemmed_data(self, dirname):
        print("Already stemmed!")
        titles = []
        docs = []
        filenames = []
        for filename in os.listdir('%s/stemmed' % dirname):
            if filename.endswith(".txt") and not filename.startswith("."):
                filenames.append(filename)
        if len(filenames) != 60:
            msg = "There are not 60 documents in ../data/RiderHaggard/stemmed/\n"
            msg += "Remove ../data/RiderHaggard/stemmed/ directory and re-run."
            raise Exception(msg)
        for i, filename in enumerate(filenames):
            title = filename.split('.')[0]
            titles.append(title)
            contents = []
            f = open('%s/stemmed/%s' % (dirname, filename), 'r')
            for line in f:
                line = [xx.strip() for xx in line.split()]
                contents.extend(line)
            f.close()
            docs.append(contents)
        return titles, docs
    def read_data(self, dirname):
        print("Reading in documents...")
        filenames = os.listdir(dirname)
        subdirs = os.listdir(dirname)
        if 'stemmed' in subdirs:
            titles, docs = self.__read_stemmed_data(dirname)
        else:
            titles, docs = self.__read_raw_data(dirname)
        ordering = [idx for idx, title in sorted(enumerate(titles),
            key = lambda xx : xx[1])]
        self.titles = []
        self.docs = []
        numdocs = len(docs)
        for d in range(numdocs):
            self.titles.append(titles[ordering[d]])
            self.docs.append(docs[ordering[d]])
        self.vocab = [xx for xx in self.get_uniq_words()]
    def index(self):
        print("Indexing...")
        inv_index = defaultdict(set)
        self.tf = defaultdict(Counter)
        for word in self.vocab:
            inv_index[word] = {}
        for doc in range(len(self.docs)):
            for word in self.docs[doc]:
                self.tf[doc][word] += 1
        for doc, title in zip(self.docs, self.titles):
            for word in self.vocab:
                inv_index[word][title] = []
            for pos, word in enumerate(doc):
                inv_index[word][title].append(pos)
        self.inv_index = inv_index
        id_to_bag_of_words = {}
        for d, doc in enumerate(self.docs):
            bag_of_words = set(doc)
            id_to_bag_of_words[d] = bag_of_words
        self.docs = id_to_bag_of_words
    def get_posting(self, word):
        posting = [doc_i for doc_i, title in enumerate(self.titles) if len(self.inv_index[word][title]) != 0]
        return posting
    def get_posting_unstemmed(self, word):
        word = self.p.stem(word)
        return self.get_posting(word)
    def boolean_retrieve(self, query):
        docs = set(self.get_posting(query[0]))
        if docs:
            for word in query[1:]:
                docs = docs.intersection(self.get_posting(word))
        docs = list(docs)
        return sorted(docs)
    def phrase_retrieve(self, query):
        docs = []
        first_hash = self.boolean_retrieve(query)
        for doc in first_hash:
            title = self.titles[doc]
            word_list = []
            for word in query:
                word_list.append(self.inv_index[word][title])
            if len(word_list) == 1:
                docs.append(doc)
                break
            is_match = bool
            for i in word_list[0]:
                for j in range(1, len(query)):
                    if (i + j) in word_list[j]:
                        is_match = True
                    else:
                        is_match = False
                        break
                if is_match:
                    docs.append(doc)
                    break
        return sorted(docs)
    def compute_tfidf(self):
        print("Calculating tf-idf...")
        self.tfidf = defaultdict(Counter)
        for word in self.vocab:
            idf = math.log10(float(len(self.docs))/float(len(self.get_posting(word))))
            for d in range(len(self.docs)):
                try:
                    self.tfidf[d][word] = (1 + math.log10(self.tf[d][word])) * idf
                except ValueError:
                    self.tfidf[d][word] = 0
    def get_tfidf(self, word, document):
        tfidf = self.tfidf[document][word]
        return tfidf
    def get_tfidf_unstemmed(self, word, document):
        word = self.p.stem(word)
        return self.get_tfidf(word, document)
    def rank_retrieve(self, query):
        k = 10
        scores = [0.0 for xx in range(len(self.titles))]
        self.d_length = defaultdict(float)
        words_in_query = set()
        for word in query:
            words_in_query.add(word)
        query_words = Counter(words_in_query)
        for word in query:
            q_word_weight = 1 + math.log10(query_words[word])
            posting_list = self.get_posting(word)
            for doc in posting_list:
                scores[doc] += self.tfidf[doc][word] * q_word_weight
        for word in self.vocab:
            for doc in range(len(self.docs)):
                self.d_length[doc] += self.tfidf[doc][word] ** 2
        for doc in range(len(self.docs)):
            scores[doc] /= math.sqrt(self.d_length[doc])
        ranking = [idx for idx, sim in sorted(enumerate(scores),
            key = lambda xx : xx[1], reverse = True)]
        results = []
        for i in range(k):
            results.append((ranking[i], scores[ranking[i]]))
        return results
    def process_query(self, query_str):
        query = query_str.lower()
        query = query.split()
        query = [self.alphanum.sub('', xx) for xx in query]
        query = [self.p.stem(xx) for xx in query]
        return query
    def query_retrieve(self, query_str):
        query = self.process_query(query_str)
        return self.boolean_retrieve(query)
    def phrase_query_retrieve(self, query_str):
        query = self.process_query(query_str)
        return self.phrase_retrieve(query)
    def query_rank(self, query_str):
        query = self.process_query(query_str)
        return self.rank_retrieve(query)
def run_tests(irsys):
    print("===== Running tests =====")
    ff = open('../data/queries.txt')
    questions = [xx.strip() for xx in ff.readlines()]
    ff.close()
    ff = open('../data/solutions.txt')
    solutions = [xx.strip() for xx in ff.readlines()]
    ff.close()
    epsilon = 1e-4
    for part in range(5):
        points = 0
        num_correct = 0
        num_total = 0
        prob = questions[part]
        soln = json.loads(solutions[part])
        if part == 0:
            print("Inverted Index Test (requires both index() and get_posting() to pass)")
            words = prob.split(", ")
            for i, word in enumerate(words):
                num_total += 1
                posting = irsys.get_posting_unstemmed(word)
                if set(posting) == set(soln[i]):
                    num_correct += 1
        elif part == 1:
            print("Boolean Retrieval Test")
            queries = prob.split(", ")
            for i, query in enumerate(queries):
                num_total += 1
                guess = irsys.query_retrieve(query)
                if set(guess) == set(soln[i]):
                    num_correct += 1
        elif part == 2:
            print("Phrase Query Retrieval")
            queries = prob.split(", ")
            for i, query in enumerate(queries):
                num_total += 1
                guess = irsys.phrase_query_retrieve(query)
                if set(guess) == set(soln[i]):
                    num_correct += 1
        elif part == 3:
            print("TF-IDF Test")
            queries = prob.split("; ")
            queries = [xx.split(", ") for xx in queries]
            queries = [(xx[0], int(xx[1])) for xx in queries]
            for i, (word, doc) in enumerate(queries):
                num_total += 1
                guess = irsys.get_tfidf_unstemmed(word, doc)
                if guess >= float(soln[i]) - epsilon and \
                        guess <= float(soln[i]) + epsilon:
                    num_correct += 1
        elif part == 4:
            print("Cosine Similarity Test")
            queries = prob.split(", ")
            for i, query in enumerate(queries):
                num_total += 1
                ranked = irsys.query_rank(query)
                top_rank = ranked[0]
                if top_rank[0] == soln[i][0]:
                    if top_rank[1] >= float(soln[i][1]) - epsilon and \
                            top_rank[1] <= float(soln[i][1]) + epsilon:
                        num_correct += 1
        feedback = "%d/%d Correct. Accuracy: %f" % \
                (num_correct, num_total, float(num_correct)/num_total)
        if num_correct == num_total:
            points = 3
        elif num_correct > 0.75 * num_total:
            points = 2
        elif num_correct > 0:
            points = 1
        else:
            points = 0
        print("    Score: %d Feedback: %s" % (points, feedback))
def main(args):
    irsys = IRSystem()
    irsys.read_data('../data/RiderHaggard')
    irsys.index()
    irsys.compute_tfidf()
    if len(args) == 0:
        run_tests(irsys)
    else:
        query = " ".join(args)
        print("Best matching documents to '%s':" % query)
        results = irsys.query_rank(query)
        for docId, score in results:
            print("%s: %e" % (irsys.titles[docId], score))
if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)