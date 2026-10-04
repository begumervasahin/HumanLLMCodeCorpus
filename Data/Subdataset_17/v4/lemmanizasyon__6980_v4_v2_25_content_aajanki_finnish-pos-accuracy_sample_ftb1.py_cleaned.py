import hashlib
import re
def read_sentences(input_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
    return list(split_sentences(lines))
def split_sentences(lines):
    start_re = re.compile(r'^')
    sentence = []
    for line in lines:
        if start_re.match(line):
            if sentence:
                yield ''.join(sentence)
                sentence = []
        if line.strip():
            sentence.append(line)
    if sentence:
        yield ''.join(sentence)
def select_sentences(sentences):
    selected = []
    for sentence in sentences:
        digest = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
        if digest.startswith('0'):
            selected.append(sentence)
    return selected
def write_sentences(output_file_path, sentences):
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(sentences))
def main():
    input_file_path = 'data/test/ftb1/ftb1u.tsv'
    output_file_path = 'data/test/ftb1/ftb1u_sample.tsv'
    sentences = read_sentences(input_file_path)
    selected_sentences = select_sentences(sentences)
    print(f'Sampled {len(selected_sentences)} out of {len(sentences)} sentences')
    write_sentences(output_file_path, selected_sentences)
    print(f'Wrote samples to {output_file_path}')
if __name__ == '__main__':
    main()