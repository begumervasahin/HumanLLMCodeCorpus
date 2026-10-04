import hashlib
import re
def main():
    input_file = 'data/test/ftb1/ftb1u.tsv'
    output_file = 'data/test/ftb1/ftb1u_sample.tsv'
    with open(input_file) as file:
        lines = file.readlines()
        sentences = list(split_sentences(lines))
    selected_sentences = filter_selected_sentences(sentences)
    print(f'Sampled {len(selected_sentences)} out of {len(sentences)} sentences')
    write_selected_sentences(output_file, selected_sentences)
    print(f'Wrote samples to {output_file}')
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
def filter_selected_sentences(sentences):
    selected = []
    for sentence in sentences:
        digest = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
        if digest.startswith('0'):
            selected.append(sentence)
    return selected
def write_selected_sentences(output_file, selected_sentences):
    with open(output_file, 'w') as file:
        file.write('\n'.join(selected_sentences))
if __name__ == '__main__':
    main()