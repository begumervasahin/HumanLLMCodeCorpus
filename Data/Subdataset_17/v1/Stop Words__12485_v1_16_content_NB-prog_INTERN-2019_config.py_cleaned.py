import gensim
import logging
from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
corpus_file = 'corpus.txt'
max_vocab_size = 50000
max_corpus_size = int(1e12)
fw_subsampling_th = None
embedding_dims = 50
neg_samples = 20
epochs = 3
mini_batch_size = 256
window_size = 5
cont_traning = False
words_to_plot = 1000
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = PathLineSentences(corpus_file)
if max_corpus_size < int(1e12):
    sentences = (sentence for i, sentence in enumerate(sentences) if i < max_corpus_size)
def calculate_subsampling_probability(word_freq, threshold):
    return 1 - (threshold / word_freq) ** 0.5
model = Word2Vec(
    vector_size=embedding_dims,
    window=window_size,
    sg=1,
    negative=neg_samples,
    min_count=1,
    max_final_vocab=max_vocab_size,
    sample=fw_subsampling_th
)
model.build_vocab(sentences, progress_per=1000)
model.train(
    sentences,
    total_examples=model.corpus_count,
    epochs=epochs,
    compute_loss=True
)
model.save("skipgram_model.model")
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
def plot_words(model, words_to_plot):
    labels = []
    tokens = []
    for word in model.wv.index_to_key[:words_to_plot]:
        tokens.append(model.wv[word])
        labels.append(word)
    tsne_model = TSNE(n_components=2, random_state=0)
    new_values = tsne_model.fit_transform(np.array(tokens))
    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
    plt.figure(figsize=(16, 16))
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()
plot_words(model, words_to_plot)