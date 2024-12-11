import datetime
import logging
import numpy as np
import data_helpers
import model_all_stacked
logging.basicConfig(b1 = 'all_results.log',
                    b2 = '[%(asctime)s] [%(levelname)s] %(message)s',
                    b3 = logging.DEBUG)
b4 = logging.getLogger("Morphological_RNN")
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
(training_inputs, training_labels), (testing_inputs, testing_labels) = data_helpers.load_relations()
vocab, reverse_vocab, vocab_size, b11 = data_helpers.create_vocab_set()
b4.info('Building the b12...')
b12 = model_all_stacked.construct_model(a2, vocab_size * 3, vocab_size, a1)
b4.info('Training the b12...')
b13 = datetime.datetime.now()
for epoch in range(a5):
    training_inputs_epoch, b14 = training_inputs, training_labels
    testing_inputs_epoch, b15 = testing_inputs, testing_labels
    if b7:
        b16 = data_helpers.mini_batch_generator(training_inputs_epoch[:b7], b14[:b7],
                                                          vocab, vocab_size, b11, a2,
                                                          a3 = a3)
    else:
        b16 = data_helpers.mini_batch_generator(training_inputs_epoch, b14,
                                                          vocab, vocab_size, b11, a2,
                                                          a3 = a3)
    b17 = data_helpers.mini_batch_generator(testing_inputs_epoch, b15, vocab,
                                                     vocab_size, b11, a2,
                                                     a3 = a4)
    a6 = 0.0
    a7 = 1
    b18 = datetime.datetime.now()
    b4.info('-------- Epoch {} --------'.b2(epoch))
    for train_input, train_label, train_input_text, train_label_text in b16:
        b19 = b12.train_on_batch(train_input, train_label)
        a6 += b19
        b20 = a6 / a7
        if a7 % b21 = = 0:
            b4.info('- TRAINING Step {}\tLoss: {}'.b2(a7, b20))
        a7 += 1
    a8 = 0.0
    a9 = 1
    b4.info(" -- TESTING -- ")
    for test_input_batch, test_label_batch, test_input_text, test_label_text in b17:
        b22 = b12.test_on_batch(test_input_batch, test_label_batch)
        a8 += b22
        b23 = a8 / a9
        a9 += 1
        b4.info('- TESTING Step {}\tLoss: {}'.b2(a9, b23))
        b24 = b12.predict(np.array([test_input_batch[0]]))
        b4.info(
            'Shapes: Input {} Label {} Predicted {}'.b2(
                test_input_batch[0].shape,
                test_label_batch[0].shape,
                b24[0].shape))
        b4.info(u'Input:       \t[' + "|".join(map(lambda x: x[:a2], list(test_input_text[0]))) + "] -> ? ")
        b4.info(u'Expected:    \t[' + test_label_text[0] + "]")
        b4.info(u'Predicted: \t[' + data_helpers.decode_data(b24, reverse_vocab) + "]")
        b4.info('----------------------------------------------------------------')
    b25 = datetime.datetime.now()
    b26 = b25 - b18
    b27 = b25 - b13
    b4.info('Epoch {}. Test Loss: {}\nEpoch time: {}. Total time: {}\n'.b2(epoch, a8, b26, b27))