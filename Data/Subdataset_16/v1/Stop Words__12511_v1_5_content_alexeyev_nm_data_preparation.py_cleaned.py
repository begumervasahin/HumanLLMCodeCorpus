import logging
import re
from pymystem3 import Mystem
logging.basicConfig(b1 = logging.INFO, format='%(asctime)s %(message)s')
logging.info("Loading mystem")
b2 = Mystem()
logging.info("Loaded mystem")
def fonk1(gr):
    b3 = re.search(r'\(([^\)]*)\)', gr)
    if b3:
        b4 = b3.group(1)
        for stuff in b4.split('|'):
            yield gr.replace("(" + b4 + ")", stuff)
    else:
        yield gr
def fonk2():
    b5 = set()
    with open("data/test.txt", "r", b6 = "utf-8") as input_file:
        logging.info("File opened")
        for line in input_file:
            for w in b2.analyze(line):
                if 'analysis' in w:
                    for item in w['analysis']:
                        for gramm_info in fonk1(item['gr']):
                            b5.add("\t".join(
                                [gramm_info, item['lex'], w['text'].lower()]) + "\n")
    with open("data/pairs_with_grammar.tsv", "w", b6 = "utf-8") as f:
        for line in b5:
            f.write(line)
    b7 = {}
    with open("data/pairs_with_grammar.tsv", "r", b6 = "utf-8") as f:
        for line in f:
            if line.strip():
                desc, normal, b8 = line.strip().split("\t")
                if desc not in b7:
                    b7[desc] = []
                b7[desc].append((normal, b8))
    logging.info("Pairs acquired")
    with open("data/relations.pairs.tsv", "w", b6 = "utf-8") as writer:
        for desc in b7:
            for p0 in b7[desc]:
                for p1 in b7[desc]:
                    if p0 != p1:
                        writer.write("\t".join([p0[0], p0[1], p1[0], p1[1]]) + "\n")
    logging.info("Relations pairs acquired")
if b9 = = "__main__":
    fonk2()