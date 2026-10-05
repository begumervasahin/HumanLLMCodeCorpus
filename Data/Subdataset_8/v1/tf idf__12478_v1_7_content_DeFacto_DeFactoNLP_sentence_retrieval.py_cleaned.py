import os
import json
import codecs
def getRelevantSentences(relevant_docs, entities, wiki_split_docs_dir):
    relevant_sentences = []
    for relevant_doc in relevant_docs:
        with codecs.open(os.path.join(wiki_split_docs_dir, f"{relevant_doc}.json"), "r", "utf-8") as file:
            data = json.load(file)
            full_lines = data["lines"]
            for line in full_lines:
                content = line.get('content', '').strip()
                if content:
                    content = content.replace("-LRB-", " ( ").replace("-RRB-", " ) ")
                    temp = {'id': relevant_doc, 'line_num': line['line_num'], 'sentence': content}
                    relevant_sentences.append(temp)
    return relevant_sentences
def getSentence(wiki_doc_dir, doc_filename, sentence_id):
    with codecs.open(os.path.join(wiki_doc_dir, f"{doc_filename}.txt"), "r", "utf-8") as doc:
        doc_lines = doc.read().splitlines()
        return doc_lines[sentence_id].split("\t")[1] if sentence_id < len(doc_lines) else None
relevant_docs = ["doc1", "doc2"]
entities = ["entity1", "entity2"]
wiki_split_docs_dir = "path/to/wiki/split/docs"
relevant_sentences = getRelevantSentences(relevant_docs, entities, wiki_split_docs_dir)
print(relevant_sentences)
sentence = getSentence("path/to/wiki/docs", "example_doc", 3)
print(sentence)