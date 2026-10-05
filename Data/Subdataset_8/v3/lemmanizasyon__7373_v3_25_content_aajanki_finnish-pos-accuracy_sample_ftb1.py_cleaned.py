import hashlib
import re
def main():
    input_file = 'data/test/ftb1/ftb1u.tsv'
    output_file = 'data/test/ftb1/ftb1u_sample.tsv'
    with open(input_file) as file:
        sentences = list(split_sentences(file.readlines()))
    selected_sentences = filter_sentences(sentences)
    print_summary(len(selected_sentences), len(sentences))
    write_to_file(output_file, selected_sentences)
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
def filter_sentences(sentences):
    selected = []
    for sentence in sentences:
        digest = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
        if digest.startswith('0'):
            selected.append(sentence)
    return selected
def print_summary(selected_count, total_count):
    print(f'Sampled {selected_count} out of {total_count} sentences')
def write_to_file(file_path, sentences):
    with open(file_path, 'w') as file:
        file.write('\n'.join(sentences))
if __name__ == '__main__':
    main()