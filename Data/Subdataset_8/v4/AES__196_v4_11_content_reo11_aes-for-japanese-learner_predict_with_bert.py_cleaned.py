import os
import argparse
import json
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import cohen_kappa_score
import scipy as sp
import pickle
from functools import partial
from tensorflow.keras import backend as K
import tokenization_sentencepiece as tokenization
import utils
from bert import modeling
from bert import optimization
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = "./bert-japanese/config.ini"
TASK_NAME = "aes"
parser = argparse.ArgumentParser(description='Linear SVR Model')
parser.add_argument('input_csv', type=str, help="input file must contain 'text_id', 'prompt' and 'text' column")
args = parser.parse_args()
config = configparser.ConfigParser()
config.read(CONFIG_PATH)
bert_config_file = tempfile.NamedTemporaryFile(mode='w+t', encoding='utf-8', suffix='.json')
bert_config_file.write(json.dumps({k: utils.str_to_value(v) for k, v in config['BERT-CONFIG'].items()}))
bert_config_file.seek(0)
flags = tf.flags
FLAGS = flags.FLAGS
flags.DEFINE_string("data_file", None, "The input data dir. Should contain the .tsv files (or other data files) for the task.")
flags.DEFINE_string("bert_config_file", "./bert-japanese/model/bert-wiki-ja/bert_config.json", "The config json file corresponding to the pre-trained BERT model. This specifies the model architecture.")
flags.DEFINE_string("model_file", "./bert-japanese/model/bert-wiki-ja/wiki-ja.model", "The model file that the SentencePiece model was trained on.")
flags.DEFINE_string("vocab_file", "./bert-japanese/model/bert-wiki-ja/wiki-ja.vocab", "The vocabulary file that the BERT model was trained on.")
flags.DEFINE_string("init_checkpoint", None, "Initial checkpoint (usually from a pre-trained BERT model).")
flags.DEFINE_bool("do_lower_case", True, "Whether to lower case the input text. Should be True for uncased models and False for cased models.")
flags.DEFINE_integer("max_seq_length", 512, "The maximum total input sequence length after WordPiece tokenization. Sequences longer than this will be truncated, and sequences shorter than this will be padded.")
flags.DEFINE_bool("do_train", False, "Whether to run training.")
flags.DEFINE_bool("do_eval", False, "Whether to run eval on the dev set.")
flags.DEFINE_bool("do_test", True, "Whether to run test on the test set.")
flags.DEFINE_integer("train_batch_size", 4, "Total batch size for training.")
flags.DEFINE_integer("eval_batch_size", 4, "Total batch size for eval.")
flags.DEFINE_integer("test_batch_size", 4, "Total batch size for eval.")
flags.DEFINE_float("learning_rate", 5e-5, "The initial learning rate for Adam.")
flags.DEFINE_float("num_train_epochs", 3.0, "Total number of training epochs to perform.")
flags.DEFINE_float("warmup_proportion", 0.1, "Proportion of training to perform linear learning rate warmup for. E.g., 0.1 = 10% of training.")
flags.DEFINE_integer("save_checkpoints_steps", 1000, "How often to save the model checkpoint.")
flags.DEFINE_integer("iterations_per_loop", 1000, "How many steps to make in each estimator call.")
flags.DEFINE_bool("use_tpu", False, "Whether to use TPU or GPU/CPU.")
tf.flags.DEFINE_string("tpu_name", None, "The Cloud TPU to use for training. This should be either the name used when creating the Cloud TPU, or a grpc:
tf.flags.DEFINE_string("tpu_zone", None, "[Optional] GCE zone where the Cloud TPU is located in. If not specified, we will attempt to automatically detect the GCE project from metadata.")
tf.flags.DEFINE_string("gcp_project", None, "[Optional] Project name for the Cloud TPU-enabled project. If not specified, we will attempt to automatically detect the GCE project from metadata.")
tf.flags.DEFINE_string("master", None, "[Optional] TensorFlow master URL.")
flags.DEFINE_integer("num_tpu_cores", 8, "Only used if `use_tpu` is True. Total number of TPU cores to use.")
class InputExample(object):
    def __init__(self, prompt, text, label=None):
        self.prompt = prompt
        self.text = text
        self.label = label
class InputFeatures(object):
    def __init__(self, input_ids, input_mask, segment_ids, label_id):
        self.input_ids = input_ids
        self.input_mask = input_mask
        self.segment_ids = segment_ids
        self.label_id = label_id
class DataProcessor(object):
    def get_train_examples(self, data_dir):
        raise NotImplementedError()
    def get_dev_examples(self, data_dir):
        raise NotImplementedError()
    def get_test_examples(self, data_dir):
        raise NotImplementedError()
    def get_labels(self):
        raise NotImplementedError()
    @classmethod
    def _read_tsv(cls, input_file, quotechar=None):
        with tf.gfile.Open(input_file, "r") as f:
            reader = csv.reader(f, delimiter="\t", quotechar=quotechar)
            lines = []
            for line in reader:
                lines.append(line)
            return lines
class OptimizedRounder(object):
    def __init__(self):
        self.coef_ = 0
    def _kappa_loss(self, coef, X, y):
    def fit(self, X, y):
    def predict(self, X, coef):
    def coefficients(self):
        return self.coef_['x']
class AESProcessor(DataProcessor):
    def get_train_examples(self, data_dir):
        raise NotImplementedError()
    def get_dev_examples(self, data_dir):
        raise NotImplementedError()
    def convert_to_tsv(self, data_file):
    def get_test_examples(self, data_file):
    def _create_examples(self, lines, set_type):
def create_model(bert_config, is_training, input_ids, input_mask, segment_ids, labels, use_one_hot_embeddings):
def model_fn_builder(bert_config, init_checkpoint, learning_rate, num_train_steps, num_warmup_steps, use_tpu, use_one_hot_embeddings):
def input_fn_builder(features, seq_length, is_training, drop_remainder):
def main(_):
if __name__ == "__main__":
    tf.app.run()