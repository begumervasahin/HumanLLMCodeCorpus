import hashlib
import re
def main():
    input_file = 'data/test/ftb1/ftb1u.tsv'
    output_file = 'data/test/ftb1/ftb1u_sample.tsv'
    sentences = read_sentences_from_file(input_file)
    selected_sentences = select_sentences_by_hash_prefix(sentences)
    report_sentences(selected_sentences, sentences)
    write_sentences_to_file(output_file, selected_sentences)
    print(f'Sentences written to {output_file}')
def read_sentences_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return list(split_lines_into_sentences(lines))
def split_lines_into_sentences(lines):
    sentence = []
    for line in lines:
        if not line.strip() and sentence:
            yield ''.join(sentence).strip()
            sentence = []
        elif line.strip():
            sentence.append(line)
    if sentence:
        yield ''.join(sentence).strip()
def select_sentences_by_hash_prefix(sentences):
    return [sentence for sentence in sentences if is_hash_starting_with_zero(sentence)]
def is_hash_starting_with_zero(sentence):
    hash_digest = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
    return hash_digest.startswith('0')
def write_sentences_to_file(file_path, sentences):
    with open(file_path, 'w') as file:
        file.write('\n'.join(sentences))
def report_sentences(selected_sentences, all_sentences):
    total_count = len(all_sentences)
    selected_count = len(selected_sentences)
    print(f'Sampled {selected_count} out of {total_count} sentences')
if __name__ == '__main__':
    main()