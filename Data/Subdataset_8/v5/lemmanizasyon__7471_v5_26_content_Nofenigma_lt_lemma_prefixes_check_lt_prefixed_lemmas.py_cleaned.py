import sys
def read_lemmas_from_dictionary(dictionary_path):
    lemmas = []
    previous_word = ''
    with open(dictionary_path, 'r', encoding='utf-8') as dictionary_file:
        for line in dictionary_file:
            word, *_ = line.split('\t')
            if word != previous_word:
                lemmas.append(word)
            previous_word = word
    return lemmas
def correct_lemma(lemma, pos_tag, morph_info, lemmas_list):
    if pos_tag != 'VERB':
        return lemma
    is_reflexive = 'Reflex=Yes' in morph_info
    base_lemma = None
    if lemma.startswith('nebesi') and is_reflexive:
        base_lemma = lemma[6:] + 's' if lemma[6:] + 's' in lemmas_list else None
    elif lemma.startswith('nebe'):
        base_lemma = lemma[4:] if lemma[4:] in lemmas_list else lemma[2:] if lemma[2:] in lemmas_list else None
    elif lemma.startswith('ne') or lemma.startswith('be'):
        base_lemma = (lemma[4:] + 's' if is_reflexive else lemma[2:]) if lemma[2:] in lemmas_list else None
    elif lemma.startswith('tebe'):
        base_lemma = lemma[6:] + 's' if is_reflexive else lemma[4:] if lemma[4:] in lemmas_list else lemma[2:]
    return base_lemma if base_lemma in lemmas_list else lemma
def process_file(input_file_path, output_file_path, lemmas_list):
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            parts = line.strip().split('\t')
            if len(parts) == 10:
                lemma, pos_tag, morph_info = parts[2], parts[3], parts[5]
                corrected_lemma = correct_lemma(lemma, pos_tag, morph_info, lemmas_list)
                parts[2] = corrected_lemma
            output_file.write('\t'.join(parts) + '\n')
def main():
    if len(sys.argv) != 3:
        print("Usage: script.py <input_file> <output_file>")
        sys.exit(1)
    dictionary_path = 'dazninis.utf8.txt'
    input_file_path, output_file_path = sys.argv[1], sys.argv[2]
    lemmas_list = read_lemmas_from_dictionary(dictionary_path)
    process_file(input_file_path, output_file_path, lemmas_list)
if __name__ == '__main__':
    main()