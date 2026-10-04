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
        for option in title.split('|'):
            yield gr.replace(f"({title})", option)
    else:
        yield gr
def process_input_file(input_path):
    lines = set()
    with open(input_path, "r", encoding="utf-8") as input_file:
        logging.info("File opened")
        for line in input_file:
            for word in m.analyze(line):
                if 'analysis' in word:
                    for analysis in word['analysis']:
                        for gramm_info in parse_gr(analysis['gr']):
                            entry = "\t".join([gramm_info, analysis['lex'], word['text'].lower()]) + "\n"
                            lines.add(entry)
    return lines
def write_to_file(lines, output_path):
    with open(output_path, "w", encoding="utf-8") as output_file:
        for line in lines:
            output_file.write(line)
def build_dict_from_file(input_path):
    gram_dict = {}
    with open(input_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            if line.strip():
                desc, normal, form = line.strip().split("\t")
                if desc not in gram_dict:
                    gram_dict[desc] = []
                gram_dict[desc].append((normal, form))
    return gram_dict
def write_relation_pairs(gram_dict, output_path):
    with open(output_path, "w", encoding="utf-8") as writer:
        for desc, pairs in gram_dict.items():
            for p0 in pairs:
                for p1 in pairs:
                    if p0 != p1:
                        writer.write("\t".join([p0[0], p0[1], p1[0], p1[1]]) + "\n")
def main():
    input_file_path = "data/test.txt"
    pairs_file_path = "data/pairs_with_grammar.tsv"
    relations_file_path = "data/relations.pairs.tsv"
    lines = process_input_file(input_file_path)
    write_to_file(lines, pairs_file_path)
    gram_dict = build_dict_from_file(pairs_file_path)
    logging.info("Pairs acquired")
    write_relation_pairs(gram_dict, relations_file_path)
    logging.info("Relations pairs acquired")
if __name__ == "__main__":
    main()