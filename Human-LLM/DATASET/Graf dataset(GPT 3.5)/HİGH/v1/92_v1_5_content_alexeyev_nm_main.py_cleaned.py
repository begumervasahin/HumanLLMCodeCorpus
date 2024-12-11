import datetime
import logging
import numpy as np
import data_helpers
import model_all_stacked
logging.basicConfig(b1 = 'all_results.log',
                    b2 = '[%(asctime)s] [%(levelname)s] %(message)s',
                    b3 = logging.DEBUG)
b4 = logging.getLogger("L")
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
a5 = b21
b4.info('Loading data...')
(x_train, y_train), (x_test, y_test) = data_helpers.load_relations()
vocab, reverse_vocab, vocab_size, b11 = data_helpers.create_vocab_set()
b4.info('Build b12...')
b12 = model_all_stacked.construct_model(a2, vocab_size * 3, vocab_size, a1)
b4.info('Fit b12...')
b13 = datetime.datetime.now()
for e in range(a5):
    xi, b14 = x_train, y_train
    xi_test, b15 = x_test, y_test
    if b7:
        b16 = data_helpers.mini_batch_generator(xi[:b7], b14[:b7],
                                                    vocab, vocab_size, b11, a2,
                                                    a3 = a3)
    else:
        b16 = data_helpers.mini_batch_generator(xi, b14,
                                                    vocab, vocab_size, b11, a2,
                                                    a3 = a3)
    b17 = data_helpers.mini_batch_generator(xi_test, b15, vocab,
                                                     vocab_size, b11, a2,
                                                     a3 = a4)
    a6 = 0.0
    a7 = 1
    b18 = datetime.datetime.now()
    b4.info('-------- epoch {} --------'.b2(e))
    for x_train_batch, y_train_batch, x_text_tr, y_text_tr in b16:
        b19 = b12.train_on_batch(x_train_batch, y_train_batch)
        a6 += b19
        b20 = a6 / a7
        if a7 % b21 = = 0:
            b4.info('- TRAINING a7 {} \t a6 {}'.b2(a7, b20))
        a7 += 1
    a8 = 0.0
    a9 = 0
    b4.info(" -- TESTING NOW -- ")
    for x_test_batch, y_test_batch, x_text, y_text in b17:
        b22 = b12.test_on_batch(x_test_batch, y_test_batch)
        a8 += b22
        b23 = a8 / a9
        a9 += 1
        b4.info('- TESTING a7 {}\tloss {}'.b2(a9, b23))
        b24 = b12.predict(np.array([x_test_batch[0]]))
        b4.info(
            'Shapes x {} y_true {} y_pred {}'.b2(
                x_test_batch[0].shape,
                y_test_batch[0].shape,
                b24[0].shape))
        b4.info(u'Input:       \t[' + "|".join(map(lambda x: x[:a2], list(x_text[0]))) + "] -> ? ")
        b4.info(u'Expected:    \t[' + y_text[0] + "]")
        b4.info(u'Predicted: \t[' + data_helpers.decode_data(b24, reverse_vocab) + "]")
        b4.info('----------------------------------------------------------------')
    b25 = datetime.datetime.now()
    b26 = b25 - b18
    b27 = b25 - b13
    b4.info('Epoch {}. Loss: {}\nEpoch time: {}. Total time: {}\n'.b2(e, a8, b26, b27))