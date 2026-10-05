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
from logging import warning, info, debug, error
from util import morpho_dataset
from util.utils import MorphoAnalyzer, Tee, log_time, find_first, AddInputsWrapper
from util.tags import WholeTags, CharTags, DictTags
from model.encoder import encoder_network
from model.tag_decoder import tag_decoder, tag_features
from model.lemma_decoder import lemma_decoder, sense_predictor
class LemmaTagNetwork:
    def __init__(self, threads, seed=42):
        self.graph = tf.Graph()
        self.graph.seed = seed
        self.session = tf.Session(graph=self.graph, config=tf.ConfigProto(inter_op_parallelism_threads=threads,
                                                                         intra_op_parallelism_threads=threads))
    def construct(self, args, num_words, num_chars, lem_num_chars, num_tags, num_senses, bow, eow):
    def _lemma_stats(self, target_seqs, target_lens, target_senses):
    def train_epoch(self, train, args, rate):
    def evaluate(self, dataset_name, dataset, args):
    def predict(self, dataset, args):
if __name__ == "__main__":
