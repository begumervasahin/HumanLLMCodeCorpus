import os
import csv
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import cohen_kappa_score
from bert import modeling, optimization
import scipy as sp
import pickle
CURDIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = "./bert-japanese/config.ini"
TASK_NAME = "aes"
flags = tf.flags
FLAGS = flags.FLAGS
flags.DEFINE_string("input_csv", None, "Path to input CSV file")
class AESProcessor(DataProcessor):
    def get_test_examples(self, data_file):
        return self._create_examples(
            self._read_tsv(os.path.join(os.path.dirname(data_file), "test.tsv")), "test")
def main(_):
    processors = {"aes": AESProcessor()}
    processor = processors[TASK_NAME]()
    bert_config_file = utils.create_temp_bert_config_file(CONFIG_PATH)
    test_df = pd.read_csv(FLAGS.input_csv)
    result_df = pd.DataFrame()
    result_df["text_id"] = test_df["text_id"]
    cols = ["holistic", "content", "organization", "language"]
    for col in cols:
        model_path = f"./trained_models/BERT/{col}"
        tf.gfile.MakeDirs(model_path)
        tokenizer = tokenization.FullTokenizer(
            model_file=FLAGS.model_file, vocab_file=FLAGS.vocab_file, do_lower_case=FLAGS.do_lower_case)
        model_fn = create_model_fn(bert_config_file, col)
        estimator = tf.contrib.tpu.TPUEstimator(
            use_tpu=FLAGS.use_tpu,
            model_fn=model_fn,
            config=utils.create_run_config(model_path, FLAGS))
        if FLAGS.do_test:
            processor.convert_to_tsv(FLAGS.input_csv)
            test_examples = processor.get_test_examples(FLAGS.input_csv)
            test_features = convert_examples_to_features(
                test_examples, label_list, FLAGS.max_seq_length, tokenizer, shut_up=True)
            test_input_fn = input_fn_builder(
                features=test_features,
                seq_length=FLAGS.max_seq_length,
                is_training=False,
                drop_remainder=True)
            test_steps = int(len(test_examples) / FLAGS.test_batch_size)
            result = estimator.evaluate(input_fn=test_input_fn, steps=test_steps)
            int_pred, thresholds, qwk = process_evaluation_result(result, col)
            result_df[col] = int_pred
    result_df.to_csv(f"./output/BERT.csv", index=False)
    print(result_df)
if __name__ == "__main__":
    tf.app.run()