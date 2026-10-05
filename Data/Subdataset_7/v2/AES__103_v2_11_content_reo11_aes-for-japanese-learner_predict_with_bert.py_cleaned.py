import os
import csv
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import cohen_kappa_score
from bert import modeling, optimization
import scipy as sp
import pickle
b1 = os.path.dirname(os.path.abspath(__file__))
b2 = "./bert-japanese/b18.ini"
b3 = "aes"
b4 = tf.b4
b5 = b4.b5
b4.DEFINE_string("input_csv", None, "Path to input CSV file")
class class1(DataProcessor):
    def fonk1(self, data_file):
        return self._create_examples(
            self._read_tsv(os.path.join(os.path.dirname(data_file), "test.tsv")), "test")
def fonk2(_):
    b6 = {"aes": class1()}
    b7 = b6[b3]()
    b8 = utils.create_temp_bert_config_file(b2)
    b9 = pd.read_csv(b5.input_csv)
    b10 = pd.DataFrame()
    b10["text_id"] = b9["text_id"]
    b11 = ["holistic", "content", "organization", "language"]
    for col in b11:
        b12 = f"./trained_models/BERT/{col}"
        tf.gfile.MakeDirs(b12)
        b13 = tokenization.FullTokenizer(
            b14 = b5.b14, vocab_file=b5.vocab_file, do_lower_case=b5.do_lower_case)
        b15 = create_model_fn(b8, col)
        b16 = tf.contrib.tpu.TPUEstimator(
            b17 = b5.b17,
            b15 = b15,
            b18 = utils.create_run_config(b12, b5))
        if b5.do_test:
            b7.convert_to_tsv(b5.input_csv)
            b19 = b7.fonk1(b5.input_csv)
            b20 = convert_examples_to_features(
                b19, label_list, b5.max_seq_length, b13, b21 = True)
            b22 = input_fn_builder(
                b23 = b20,
                b24 = b5.max_seq_length,
                b25 = False,
                b26 = True)
            b27 = int(len(b19) / b5.test_batch_size)
            b28 = b16.evaluate(input_fn=b22, steps=b27)
            int_pred, thresholds, b29 = process_evaluation_result(b28, col)
            b10[col] = int_pred
    b10.to_csv(f"./output/BERT.csv", b30 = False)
    print(b10)
if b31 = = "__main__":
    tf.app.run()