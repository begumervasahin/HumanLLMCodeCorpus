import sys
def load_lt_lemmas_dict(filename):
    lt_lemmas = set()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip().split('\t')[0]
            lt_lemmas.add(word)
    return lt_lemmas
def correct_lemmas(input_file, output_file, lt_lemmas):
    with open(input_file, 'r', encoding='utf-8') as f:
        with open(output_file, 'w', encoding='utf-8') as doc:
            for line in f:
                line_parts = line.strip().split('\t')
                if len(line_parts) == 10:
                    lemma = line_parts[2]
                    if line_parts[3] == 'VERB':
                        if lemma.startswith('nebe'):
                            if lemma.startswith('nebesi'):
                                if 'Reflex=Yes' in line_parts[5]:
                                    if lemma[6:] + 's' in lt_lemmas:
                                        line_parts[2] = lemma[6:] + 's'
                            elif lemma[4:] in lt_lemmas:
                                line_parts[2] = lemma[4:]
                            elif lemma[2:] in lt_lemmas:
                                line_parts[2] = lemma[2:]
                        elif lemma.startswith('ne'):
                            if 'Reflex=Yes' in line_parts[5]:
                                line_parts[2] = lemma[4:] + 's'
                            elif lemma[2:] in lt_lemmas:
                                line_parts[2] = lemma[2:]
                        elif lemma.startswith('tebe'):
                            if 'Reflex=Yes' in line_parts[5]:
                                line_parts[2] = lemma[6:] + 's'
                            elif lemma[2:] in lt_lemmas:
                                line_parts[2] = lemma[2:]
                            else:
                                line_parts[2] = lemma[4:]
                        elif lemma.startswith('be'):
                            if 'Reflex=Yes' in line_parts[5]:
                                line_parts[2] = lemma[4:] + 's'
                            elif lemma[2:] in lt_lemmas:
                                line_parts[2] = lemma[2:]
                    corrected_line = '\t'.join(line_parts)
                    doc.write(corrected_line + '\n')
                else:
                    doc.write(line)
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file output_file dictionary_file")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    dictionary_file = sys.argv[3]
    lt_lemmas = load_lt_lemmas_dict(dictionary_file)
    correct_lemmas(input_file, output_file, lt_lemmas)