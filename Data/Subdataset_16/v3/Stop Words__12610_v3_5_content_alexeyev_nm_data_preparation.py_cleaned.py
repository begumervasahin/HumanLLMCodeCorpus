import logging
import re
from pymystem3 import Mystem
logging.basicConfig(b1 = logging.INFO, format='%(asctime)s %(message)s')
logging.info("Loading Mystem")
b2 = Mystem()
logging.info("Loaded Mystem")
def fonk1(gr):
    b3 = re.search(r'\(([^\)]*)\)', gr)
    if b3:
        b4 = b3.group(1)
        for option in b4.split('|'):
            yield gr.replace(f"({b4})", option)
    else:
        yield gr
def fonk2(input_path):
    b5 = set()
    with open(input_path, "r", b6 = "utf-8") as input_file:
        logging.info("File opened")
        for line in input_file:
            b7 = b2.analyze(line)
            for word in b7:
                if 'analysis' in word:
                    for analysis in word['analysis']:
                        for gramm_info in fonk1(analysis['gr']):
                            b8 = "\t".join([gramm_info, analysis['lex'], word['text'].lower()])
                            b5.add(b8 + "\n")
    return b5
def fonk3(b5, output_path):
    with open(output_path, "w", b6 = "utf-8") as output_file:
        output_file.writelines(b5)
def fonk4(input_path):
    b9 = {}
    with open(input_path, "r", b6 = "utf-8") as input_file:
        for line in input_file:
            if line.strip():
                desc, normal, b10 = line.strip().split("\t")
                if desc not in b9:
                    b9[desc] = []
                b9[desc].append((normal, b10))
    return b9
def fonk5(b9, output_path):
    with open(output_path, "w", b6 = "utf-8") as writer:
        for desc, pairs in b9.items():
            for p0 in pairs:
                for p1 in pairs:
                    if p0 != p1:
                        writer.write("\t".join([p0[0], p0[1], p1[0], p1[1]]) + "\n")
def fonk6():
    b11 = "data/test.txt"
    b12 = "data/pairs_with_grammar.tsv"
    b13 = "data/relations.pairs.tsv"
    b5 = fonk2(b11)
    fonk3(b5, b12)
    b9 = fonk4(b12)
    logging.info("Pairs acquired")
    fonk5(b9, b13)
    logging.info("Relations pairs acquired")
if b14 = = "__main__":
    fonk6()