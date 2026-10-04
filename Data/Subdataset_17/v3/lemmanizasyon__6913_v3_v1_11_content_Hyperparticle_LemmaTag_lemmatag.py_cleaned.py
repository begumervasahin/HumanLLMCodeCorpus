import numpy as np
import tensorflow as tf
import argparse
import os
import sys
from tqdm import tqdm
from tensorflow.python.client import timeline
import logging
from logging import warning, info, debug, error
from util import morpho_dataset
from util.utils import MorphoAnalyzer, Tee, log_time, find_first, AddInputsWrapper
from util.tags import WholeTags, CharTags, DictTags
from model.encoder import encoder_network
from model.tag_decoder import tag_decoder
from model.lemma_decoder import lemma_decoder, sense_predictor
class LemmaTagNetwork:
    def __init__(self, threads, seed=42):
        self.graph = tf.Graph()
        self.graph.seed = seed
        self.session = tf.Session(graph=self.graph, config=tf.ConfigProto(
            inter_op_parallelism_threads=threads,
            intra_op_parallelism_threads=threads
        ))
    def construct(self, args, num_words, num_chars, lem_num_chars, num_tags, num_senses, bow, eow):
        with self.graph.as_default():
            self.words = tf.placeholder(tf.int32, [None, None], name="words")
            self.word_lens = tf.placeholder(tf.int32, [None], name="word_lens")
            self.chars = tf.placeholder(tf.int32, [None, None], name="chars")
            self.char_lens = tf.placeholder(tf.int32, [None, None], name="char_lens")
            self.tags = tf.placeholder(tf.int32, [None, None], name="tags")
            self.lemmas = tf.placeholder(tf.int32, [None, None], name="lemmas")
            self.senses = tf.placeholder(tf.int32, [None], name="senses")
            self.learning_rate = tf.placeholder(tf.float32, [], name="learning_rate")
            encoded_words = encoder_network(self.words, self.word_lens, num_words, args.embedding_size, args.rnn_size)
            tag_logits = tag_decoder(encoded_words, num_tags, args.rnn_size)
            lemma_logits, sense_logits = lemma_decoder(encoded_words, num_chars, lem_num_chars, args.rnn_size)
            self.loss = tf.reduce_mean(
                tf.nn.sparse_softmax_cross_entropy_with_logits(logits=tag_logits, labels=self.tags)
            )
            self.train_op = tf.train.AdamOptimizer(learning_rate=self.learning_rate).minimize(self.loss)
            self.session.run(tf.global_variables_initializer())
    def train_epoch(self, train, args, rate):
        total_loss = 0
        for batch in train.batches(args.batch_size):
            feed_dict = {
                self.words: batch["words"],
                self.word_lens: batch["word_lens"],
                self.chars: batch["chars"],
                self.char_lens: batch["char_lens"],
                self.tags: batch["tags"],
                self.lemmas: batch["lemmas"],
                self.senses: batch["senses"],
                self.learning_rate: rate
            }
            loss, _ = self.session.run([self.loss, self.train_op], feed_dict=feed_dict)
            total_loss += loss
        return total_loss
    def evaluate(self, dataset_name, dataset, args):
        pass
    def predict(self, dataset, args):
        pass
def main():
    parser = argparse.ArgumentParser(description="Train and evaluate LemmaTagNetwork.")
    parser.add_argument("--threads", default=1, type=int, help="Number of threads to use.")
    parser.add_argument("--seed", default=42, type=int, help="Random seed.")
    parser.add_argument("--embedding_size", default=128, type=int, help="Size of word embeddings.")
    parser.add_argument("--rnn_size", default=128, type=int, help="Size of RNN hidden layer.")
    parser.add_argument("--batch_size", default=64, type=int, help="Batch size.")
    parser.add_argument("--epochs", default=10, type=int, help="Number of epochs.")
    parser.add_argument("--learning_rate", default=0.001, type=float, help="Learning rate.")
    args = parser.parse_args()
    train = morpho_dataset.load("train")
    dev = morpho_dataset.load("dev")
    num_words = train.num_words()
    num_chars = train.num_chars()
    lem_num_chars = train.lem_num_chars()
    num_tags = train.num_tags()
    num_senses = train.num_senses()
    bow, eow = train.bow(), train.eow()
    network = LemmaTagNetwork(threads=args.threads, seed=args.seed)
    network.construct(args, num_words, num_chars, lem_num_chars, num_tags, num_senses, bow, eow)
    for epoch in range(args.epochs):
        rate = args.learning_rate * (0.5 ** (epoch
        train_loss = network.train_epoch(train, args, rate)
        print(f"Epoch: {epoch + 1}, Train Loss: {train_loss:.4f}")
if __name__ == "__main__":
    main()