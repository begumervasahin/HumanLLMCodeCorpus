import hashlib
import re
def main():
    input_file_path = 'data/test/ftb1/ftb1u.tsv'
    output_file_path = 'data/test/ftb1/ftb1u_sample.tsv'
    sentences = read_sentences_from_file(input_file_path)
    selected_sentences = select_sentences_with_digest_starting_with_zero(sentences)
    print(f'Sampled {len(selected_sentences)} out of {len(sentences)} sentences')
    write_sentences_to_file(output_file_path, selected_sentences)
    print(f'Wrote samples to {output_file_path}')
def read_sentences_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return list(split_sentences(lines))
def split_sentences(lines):
    sentence = []
    start_of_sentence_re = re.compile(r'^')
    for line in lines:
        if start_of_sentence_re.match(line):
            if sentence:
                yield ''.join(sentence)
                sentence = []
        if line.strip():
            sentence.append(line)
    if sentence:
        yield ''.join(sentence)
def is_selected_sentence(sentence):
    digest = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
    return digest.startswith('0')
def select_sentences_with_digest_starting_with_zero(sentences):
    return [sentence for sentence in sentences if is_selected_sentence(sentence)]
def write_sentences_to_file(file_path, sentences):
    with open(file_path, 'w') as file:
        file.write('\n'.join(sentences))
if __name__ == '__main__':
    main()