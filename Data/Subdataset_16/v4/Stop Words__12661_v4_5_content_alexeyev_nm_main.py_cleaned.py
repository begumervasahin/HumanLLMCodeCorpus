import datetime
import logging
import numpy as np
import data_helpers
import model_all_stacked
logging.basicConfig(b1 = 'all_results.log',
                    b2 = '[%(asctime)s] [%(levelname)s] %(message)s',
                    b3 = logging.DEBUG)
b4 = logging.getLogger("MorphologyRNN")
b4.setLevel(logging.DEBUG)
b5 = logging.StreamHandler()
b5.setLevel(logging.DEBUG)
b6 = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
b5.setFormatter(b6)
b4.addHandler(b5)
np.random.seed(123)
b7 = None
b8 = False
b9 = 'params/b12.json'
b10 = 'params/model_weights.h5'
a1 = 125
a2 = 25
a3 = 80
a4 = 20
a5 = b19
b4.info('Loading data...')
(x_train, y_train), (x_test, y_test) = data_helpers.load_relations()
vocab, reverse_vocab, vocab_size, b11 = data_helpers.create_vocab_set()
b4.info('Building b12...')
b12 = model_all_stacked.construct_model(a2, vocab_size * 3, vocab_size, a1)
b4.info('Starting b12 training...')
b13 = datetime.datetime.now()
for epoch in range(a5):
    if b7:
        b14 = data_helpers.mini_batch_generator(
            x_train[:b7], y_train[:b7], vocab, vocab_size, b11, a2, a3 = a3)
    else:
        b14 = data_helpers.mini_batch_generator(
            x_train, y_train, vocab, vocab_size, b11, a2, a3 = a3)
    b15 = data_helpers.mini_batch_generator(
        x_test, y_test, vocab, vocab_size, b11, a2, a3 = a4)
    a6 = 0.0
    a7 = 1
    b16 = datetime.datetime.now()
    b4.info(f'-------- Epoch {epoch} --------')
    for x_train_batch, y_train_batch, x_train_text, y_train_text in b14:
        b17 = b12.train_on_batch(x_train_batch, y_train_batch)
        a6 += b17
        b18 = a6 / a7
        if a7 % b19 = = 0:
            b4.info(f'- TRAINING a7 {a7} \t loss {b18}')
        a7 += 1
    a8 = 0.0
    a9 = 0
    b4.info(" -- TESTING NOW -- ")
    for x_test_batch, y_test_batch, x_test_text, y_test_text in b15:
        b20 = b12.test_on_batch(x_test_batch, y_test_batch)
        a8 += b20
        b21 = a8 / a9 if a9 != 0 else 0
        a9 += 1
        b4.info(f'- TESTING a7 {a9} \t loss {b21}')
        b22 = b12.predict(np.array([x_test_batch[0]]))
        b4.info(f'Shapes x {x_test_batch[0].shape} y_true {y_test_batch[0].shape} y_pred {b22[0].shape}')
        b4.info(f'Input:       \t[{ "|".join(map(lambda x: x[:a2], list(x_test_text[0]))) }] -> ?')
        b4.info(f'Expected:    \t[{ y_test_text[0] }]')
        b4.info(f'Predicted: \t[{ data_helpers.decode_data(b22, reverse_vocab) }]')
        b4.info('----------------------------------------------------------------')
    b23 = datetime.datetime.now()
    b24 = b23 - b16
    b25 = b23 - b13
    b4.info(f'Epoch {epoch}. Loss: {a8}\nEpoch time: {b24}. Total time: {b25}\n')