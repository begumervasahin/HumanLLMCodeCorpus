import logging
import re
from pymystem3 import Mystem
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logging.info("Loading mystem")
m = Mystem()
logging.info("Loaded mystem")
def parse_gr(gr):
    options = re.search(r'\(([^\)]*)\)', gr)
    if options:
        title = options.group(1)
        for stuff in title.split('|'):
            yield gr.replace("(" + title + ")", stuff)
    else:
        yield gr
def main():
    lines = set()
    with open("data/test.txt", "r", encoding="utf-8") as input_file:
        logging.info("File opened")
        for line in input_file:
            for w in m.analyze(line):
                if 'analysis' in w:
                    for item in w['analysis']:
                        for gramm_info in parse_gr(item['gr']):
                            lines.add("\t".join(
                                [gramm_info, item['lex'], w['text'].lower()]) + "\n")
    with open("data/pairs_with_grammar.tsv", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
    dict = {}
    with open("data/pairs_with_grammar.tsv", "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                desc, normal, form = line.strip().split("\t")
                if desc not in dict:
                    dict[desc] = []
                dict[desc].append((normal, form))
    logging.info("Pairs acquired")
    with open("data/relations.pairs.tsv", "w", encoding="utf-8") as writer:
        for desc in dict:
            for p0 in dict[desc]:
                for p1 in dict[desc]:
                    if p0 != p1:
                        writer.write("\t".join([p0[0], p0[1], p1[0], p1[1]]) + "\n")
    logging.info("Relations pairs acquired")
if __name__ == "__main__":
    main()