import gensim
import random
from gensim.corpora import Dictionary
from gensim import models
class Topic2Vec:
    def __init__(self, sentences, lda_model, flag, filename, size, window, mincount):
        self.sentences = sentences
        self.lda_model = lda_model
        self.filename = filename
        self.size = size
        self.window = window
        self.mincount = mincount
        self.permute_sentences = []
        self.dict_id = Dictionary.load('/path/to/dictionary').token2id
        if flag:
            self._perform_variation()
            self._train_word2vec_model()
        self.topic2vec = models.Word2Vec.load(self.filename)
        self.lda_topics = [self.lda_model.show_topic(x) for x in range(50)]
        self.topic_vecs = [self.topic2vec.most_similar(positive=["u" + str(x)]) for x in range(50)]
        print(f"{self.filename} is finished")
    def _perform_variation(self):
        for sentence in self.sentences:
            sentence_permute = self._generate_permuted_sentence(sentence)
            self.permute_sentences.append(sentence_permute)
    def _generate_permuted_sentence(self, sentence):
        permuted_sentence = []
        for index, word in enumerate(sentence):
            permuted_word = self._permute_word(word)
            permuted_sentence.append(permuted_word)
        return permuted_sentence
    def _permute_word(self, word):
        if word in self.dict_id:
            word_bow = self.lda_model[self.dict_id[word]]
            likely_topic = word_bow[-1][0] if word_bow else ''
            return "u" + str(likely_topic)
        return word
    def _train_word2vec_model(self):
        random.shuffle(self.permute_sentences)
        topic2vec_model = models.Word2Vec(self.permute_sentences, size=self.size, window=self.window, min_count=self.mincount, workers=2)
        topic2vec_model.save(self.filename)
        random.shuffle(self.sentences)
        word2vec_model = models.Word2Vec(self.sentences, size=self.size, window=self.window, min_count=3, workers=2)
        word2vec_model.save(self.filename + "_w2v")
    def most_similar_topic(self, word):
        if word in self.dict_id:
            scores = [(self.topic2vec.similarity("u" + word, "u" + str(x)), "u" + str(x)) for x in range(50)]
            return max(scores, key=lambda x: x[0])
        else:
            print(f"Word {word} not in dictionary")
            return (0, 0)
sentences = [['apple', 'banana', 'orange'], ['dog', 'cat', 'horse'], ['tree', 'flower', 'grass']]
lda_model = gensim.models.ldamodel.LdaModel()
t2v = Topic2Vec(sentences, lda_model, True, 'topic2vec_model', 100, 5, 1)
word = 'apple'
most_similar = t2v.most_similar_topic(word)
print(f"Most similar topic to '{word}': {most_similar[1]} with similarity score {most_similar[0]}")