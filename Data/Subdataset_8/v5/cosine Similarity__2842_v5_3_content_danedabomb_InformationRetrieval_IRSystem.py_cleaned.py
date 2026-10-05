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
        self.alphanumeric_pattern = re.compile('[^a-zA-Z0-9]')
        self.stemmer = PorterStemmer()
    def get_unique_words(self):
        unique_words = set()
        for doc in self.docs:
            unique_words.update(doc)
        return unique_words
    def stem_document(self, document):
        stemmed_doc = []
        for line in document:
            line = line.lower().split()
            line = [self.alphanumeric_pattern.sub('', word) for word in line]
            line = [self.stemmer.stem(word) for word in line if word]
            stemmed_doc.extend(line)
        return stemmed_doc
    def read_raw_data(self, dirname):
        print("Stemming Documents...")
        titles = []
        docs = []
        os.makedirs(f'{dirname}/stemmed', exist_ok=True)
        title_pattern = re.compile('(.*) \d+\.txt')
        filenames = [filename for filename in os.listdir(f'{dirname}/raw') if filename.endswith(".txt") and not filename.startswith(".")]
        for i, filename in enumerate(filenames):
            title = title_pattern.search(filename).group(1)
            print(f"    Doc {i+1} of {len(filenames)}: {title}")
            titles.append(title)
            contents = []
            with open(f'{dirname}/raw/{filename}', 'r') as f:
                with open(f'{dirname}/stemmed/{title}.txt', 'w') as of:
                    contents = self.stem_document(f)
                    of.write('\n'.join(contents))
            docs.append(contents)
        return titles, docs
    def read_stemmed_data(self, dirname):
        print("Already stemmed!")
        titles = []
        docs = []
        filenames = [filename for filename in os.listdir(f'{dirname}/stemmed') if filename.endswith(".txt") and not filename.startswith(".")]
        if len(filenames) != 60:
            msg = "There are not 60 documents in ../data/RiderHaggard/stemmed/\n"
            msg += "Remove ../data/RiderHaggard/stemmed/ directory and re-run."
            raise Exception(msg)
        for i, filename in enumerate(filenames):
            title = filename.split('.')[0]
            titles.append(title)
            with open(f'{dirname}/stemmed/{filename}', 'r') as f:
                contents = f.read().splitlines()
            docs.append(contents)
        return titles, docs
    def read_data(self, dirname):
        print("Reading in documents...")
        filenames = os.listdir(dirname)
        subdirs = os.listdir(dirname)
        if 'stemmed' in subdirs:
            titles, docs = self.read_stemmed_data(dirname)
        else:
            titles, docs = self.read_raw_data(dirname)
        ordering = sorted(range(len(titles)), key=lambda k: titles[k])
        self.titles = [titles[i] for i in ordering]
        self.docs = [docs[i] for i in ordering]
        self.vocab = list(self.get_unique_words())
    def index(self):
        print("Indexing...")
        self.inv_index = defaultdict(lambda: defaultdict(list))
        self.tf = defaultdict(Counter)
        for idx, doc in enumerate(self.docs):
            for pos, word in enumerate(doc):
                self.inv_index[word][self.titles[idx]].append(pos)
                self.tf[idx][word] += 1
    def get_posting(self, word):
        return [idx for idx, title in enumerate(self.titles) if self.inv_index[word][title]]
    def boolean_retrieve(self, query):
        if not query: return []
        docs = set(self.get_posting(query[0]))
        for word in query[1:]:
            docs.intersection_update(self.get_posting(word))
        return sorted(docs)
    def phrase_retrieve(self, query):
        first_hash = self.boolean_retrieve(query)
        phrase_docs = []
        for doc in first_hash:
            word_positions = [self.inv_index[word][self.titles[doc]] for word in query]
            match = any(all(pos + i in word_positions[j] for j, pos in enumerate(word_positions[0])) for i in range(1, len(query)))
            if match:
                phrase_docs.append(doc)
        return phrase_docs
    def compute_tfidf(self):
        print("Calculating tf-idf...")
        self.tfidf = defaultdict(Counter)
        for word in self.vocab:
            idf = math.log10(len(self.docs) / len(self.get_posting(word)))
            for idx, doc in enumerate(self.docs):
                tf = 1 + math.log10(self.tf[idx][word]) if self.tf[idx][word] else 0
                self.tfidf[idx][word] = tf * idf
    def rank_retrieve(self, query):
        if not query: return []
        scores = defaultdict(float)
        query_words = Counter(query)
        for word in query:
            q_word_weight = 1 + math.log10(query_words[word])
            for idx, doc in enumerate(self.docs):
                if word in doc:
                    scores[idx] += self.tfidf[idx][word] * q_word_weight
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
    def process_query(self, query_str):
        query = query_str.lower().split()
        query = [self.alphanumeric_pattern.sub('', word) for word in query]
        query = [self.stemmer.stem(word) for word in query if word]
        return query
def main(args):
    irsys = IRSystem()
    irsys.read_data('../data/RiderHaggard')
    irsys.index()
    irsys.compute_tfidf()
    if not args:
        run_tests(irsys)
    else:
        query = " ".join(args)
        print("Best matching documents to '%s':" % query)
        results = irsys.rank_retrieve(irsys.process_query(query))
        for docId, score in results:
            print("%s: %e" % (irsys.titles[docId], score))
if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)