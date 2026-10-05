from pathlib import Path
from preprocess_data import split_into_sentences
class Dataset:
    def __init__(self, name, datapath):
        self.name = name
        self.datapath = Path(datapath)
        self.sentences = self._load_and_parse_data()
    def _load_and_parse_data(self):
        with self.datapath.open() as file:
            raw_data = file.readlines()
        return self._parse_conllu(raw_data)
    def _parse_conllu(self, raw_data):
        sentences = []
        for sentence in split_into_sentences(raw_data):
            tokens = [self._parse_line(line) for line in sentence if self._is_valid_line(line)]
            sentences.append(Sentence(tokens))
        return sentences
    def _parse_line(self, line):
        fields = line.split('\t')
        assert len(fields) == 10, "Each line must have 10 fields according to the CONLL-U format"
        text = fields[1].replace(' ', '')
        lemma = fields[2].replace(' ', '')
        space_after = fields[9] != 'SpaceAfter=No'
        return Token(text, lemma, fields[3], space_after)
    def _is_valid_line(self, line):
        return line and not line.startswith('
    def count_tokens(self):
        return sum(sentence.count_tokens() for sentence in self.sentences)
class Token:
    def __init__(self, text, lemma, pos, space_after=True):
        self.text = text
        self.lemma = lemma
        self.pos = pos
        self.space_after = space_after
class Sentence:
    def __init__(self, tokens):
        self.tokens = tokens
    def text(self):
        return ''.join(token.text + (' ' if token.space_after else '') for token in self.tokens).rstrip()
    def lemmas(self):
        return [token.lemma for token in self.tokens]
    def pos_tags(self):
        return [token.pos for token in self.tokens]
    def count_tokens(self):
        return len(self.tokens)
def gold_path(testset_name):
    paths = {
        'UD_Finnish_TDT': 'data/preprocessed/UD_Finnish-TDT/fi_tdt-ud-test.conllu',
        'ftb1u': 'data/preprocessed/ftb1/ftb1u_sample.tsv',
        'ftb2-news': 'data/preprocessed/ftb2/FinnTreeBank_2/news-samples_tab.txt',
        'ftb2-sofie': 'data/preprocessed/ftb2/FinnTreeBank_2/sofie12_tab.txt',
        'ftb2-wikipedia': 'data/preprocessed/ftb2/FinnTreeBank_2/wikipedia-samples_tab.txt',
    }
    return paths.get(testset_name, '')
all_testsets = [Dataset(name, gold_path(name)) for name in [
    'UD_Finnish_TDT',
    'ftb1u',
    'ftb2-news',
    'ftb2-sofie',
    'ftb2-wikipedia'
]]