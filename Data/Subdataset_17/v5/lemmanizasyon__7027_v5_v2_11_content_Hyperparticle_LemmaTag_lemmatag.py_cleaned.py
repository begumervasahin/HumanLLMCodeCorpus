import numpy as np
import tensorflow as tf
import argparse
import datetime
import os
import shutil
import sys
from tqdm import tqdm
from tensorflow.python.client import timeline
import logging
from util import morpho_dataset
from util.utils import MorphoAnalyzer, Tee, log_time, find_first, AddInputsWrapper
from util.tags import WholeTags, CharTags, DictTags
from model.encoder import encoder_network
from model.tag_decoder import tag_decoder, tag_features
from model.lemma_decoder import lemma_decoder, sense_predictor
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class LemmaTagNetwork:
    def __init__(self, threads, seed=42):
        self.graph = tf.Graph()
        self.graph.seed = seed
        config = tf.ConfigProto(inter_op_parallelism_threads=threads,
                                intra_op_parallelism_threads=threads)
        self.session = tf.Session(graph=self.graph, config=config)
    def construct(self, args, num_words, num_chars, lem_num_chars, num_tags, num_senses, bow, eow):
        with self.graph.as_default():
            self.word_ids = tf.placeholder(tf.int32, [None, None], name="word_ids")
            self.char_ids = tf.placeholder(tf.int32, [None, None, None], name="char_ids")
            self.targets = tf.placeholder(tf.int32, [None, None], name="targets")
            self.seq_lengths = tf.placeholder(tf.int32, [None], name="seq_lengths")
            self.char_lengths = tf.placeholder(tf.int32, [None, None], name="char_lengths")
            word_embeddings = encoder_network(self.word_ids, num_words, num_chars, bow, eow)
            tag_logits = tag_decoder(word_embeddings, num_tags)
            lemma_predictions = lemma_decoder(word_embeddings, lem_num_chars)
            sense_predictions = sense_predictor(word_embeddings, num_senses)
            self.loss = self._compute_loss(tag_logits, lemma_predictions, sense_predictions)
            self.optimizer = tf.train.AdamOptimizer(learning_rate=args.learning_rate).minimize(self.loss)
            self.session.run(tf.global_variables_initializer())
    def _compute_loss(self, tag_logits, lemma_predictions, sense_predictions):
        tag_loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=self.targets, logits=tag_logits)
        lemma_loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=self.targets, logits=lemma_predictions)
        sense_loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=self.targets, logits=sense_predictions)
        total_loss = tf.reduce_mean(tag_loss + lemma_loss + sense_loss)
        return total_loss
    def _lemma_stats(self, target_seqs, target_lens, target_senses):
        pass
    def train_epoch(self, train_data, args, learning_rate):
        total_loss = 0
        for batch in tqdm(train_data):
            feed_dict = {
                self.word_ids: batch["word_ids"],
                self.char_ids: batch["char_ids"],
                self.targets: batch["targets"],
                self.seq_lengths: batch["seq_lengths"],
                self.char_lengths: batch["char_lengths"]
            }
            loss, _ = self.session.run([self.loss, self.optimizer], feed_dict=feed_dict)
            total_loss += loss
        return total_loss
    def evaluate(self, dataset_name, dataset, args):
        total_loss = 0
        for batch in dataset:
            feed_dict = {
                self.word_ids: batch["word_ids"],
                self.char_ids: batch["char_ids"],
                self.targets: batch["targets"],
                self.seq_lengths: batch["seq_lengths"],
                self.char_lengths: batch["char_lengths"]
            }
            loss = self.session.run(self.loss, feed_dict=feed_dict)
            total_loss += loss
        return total_loss
    def predict(self, dataset, args):
        predictions = []
        for batch in dataset:
            feed_dict = {
                self.word_ids: batch["word_ids"],
                self.char_ids: batch["char_ids"],
                self.seq_lengths: batch["seq_lengths"],
                self.char_lengths: batch["char_lengths"]
            }
            batch_predictions = self.session.run(self.lemma_predictions, feed_dict=feed_dict)
            predictions.extend(batch_predictions)
        return predictions
def parse_arguments():
    parser = argparse.ArgumentParser(description="Train and evaluate a LemmaTag model.")
    parser.add_argument("--threads", type=int, default=1, help="Number of threads to use.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed.")
    parser.add_argument("--learning_rate", type=float, default=0.001, help="Learning rate for the optimizer.")
    return parser.parse_args()
def main():
    args = parse_arguments()
    logger.info("Initializing the LemmaTag model.")
    network = LemmaTagNetwork(threads=args.threads, seed=args.seed)
    network.construct(args, num_words=10000, num_chars=100, lem_num_chars=50,
                      num_tags=20, num_senses=10, bow='<bow>', eow='<eow>')
    train_data = []
    valid_data = []
    for epoch in range(10):
        train_loss = network.train_epoch(train_data, args, learning_rate=args.learning_rate)
        valid_loss = network.evaluate("validation", valid_data, args)
        logger.info(f"Epoch {epoch + 1}: Train Loss = {train_loss}, Validation Loss = {valid_loss}")
    test_data = []
    predictions = network.predict(test_data, args)
    logger.info(f"Predictions: {predictions}")
if __name__ == "__main__":
    main()