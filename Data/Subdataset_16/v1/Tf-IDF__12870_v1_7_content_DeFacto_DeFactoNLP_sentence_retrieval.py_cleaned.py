import os
import json
import codecs
import nltk
def fonk1(relevant_docs, wiki_split_docs_dir):
    b1 = []
    for relevant_doc in relevant_docs:
        b2 = os.path.join(wiki_split_docs_dir, relevant_doc + ".json")
        with codecs.open(b2, "r", "utf-8") as file:
            b3 = json.load(file)
            b4 = b3["b5"]
            b5 = [line['content'].strip().replace("-LRB-", " ( ").replace("-RRB-", " ) ") for line in b4]
            for i, line in enumerate(b5):
                if line:
                    b6 = {
                        'id': relevant_doc,
                        'line_num': i,
                        'sentence': line
                    }
                    b1.append(b6)
    return b1
def fonk2(wiki_doc_dir, doc_filename, sentence_id):
    b2 = os.path.join(wiki_doc_dir, doc_filename + ".txt")
    with codecs.open(b2, "r", "utf-8") as doc:
        b7 = doc.read().split("\n")
        return b7[sentence_id].split("\t")[1]
