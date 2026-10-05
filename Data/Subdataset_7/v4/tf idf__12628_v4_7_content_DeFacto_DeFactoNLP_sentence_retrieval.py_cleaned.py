import os
import json
import jsonlines
import nltk
import codecs
import utilities
def fonk1(relevant_docs, entities, wiki_split_docs_dir):
    b1 = []
    for relevant_doc in relevant_docs:
        with codecs.open(os.path.join(wiki_split_docs_dir, relevant_doc + ".json"), "r", "utf-8") as file:
            b2 = json.load(file)
            b3 = b2["b4"]
            b4 = [b5['content'] for b5 in b3 if b5['content'].strip()]
            for i, b5 in enumerate(b4):
                b5 = b5.strip()
                b5 = b5.replace("-LRB-", " ( ")
                b5 = b5.replace("-RRB-", " ) ")
                b6 = {
                    'id': relevant_doc,
                    'line_num': i,
                    'sentence': b5
                }
                b1.append(b6)
    return b1
def fonk2(wiki_doc_dir, doc_filename, sentence_id):
    with codecs.open(os.path.join(wiki_doc_dir, doc_filename + ".txt"), "r", "utf-8") as doc:
        b7 = doc.readlines()
        return b7[sentence_id].split("\t")[1]