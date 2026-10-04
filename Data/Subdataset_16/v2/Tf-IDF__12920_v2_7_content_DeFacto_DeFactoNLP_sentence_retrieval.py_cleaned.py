
import os
import json
import codecs
def fonk1(relevant_docs, wiki_split_docs_dir):
    b1 = []
    for doc in relevant_docs:
        b2 = os.path.join(wiki_split_docs_dir, f"{doc}.json")
        with codecs.open(b2, "r", "utf-8") as file:
            b3 = json.load(file)
            b4 = b3["b4"]
            for i, line in enumerate(b4):
                b5 = line['b3'].strip().replace("-LRB-", " ( ").replace("-RRB-", " ) ")
                if b5:
                    b1.append({
                        'id': doc,
                        'line_num': i,
                        'b5': b5
                    })
    return b1
def fonk2(wiki_doc_dir, doc_filename, sentence_id):
    b2 = os.path.join(wiki_doc_dir, f"{doc_filename}.txt")
    with codecs.open(b2, "r", "utf-8") as doc:
        b4 = doc.read().split("\n")
        if sentence_id < len(b4):
            return b4[sentence_id].split("\t")[1]
        else:
            raise IndexError("Sentence ID out of range")
