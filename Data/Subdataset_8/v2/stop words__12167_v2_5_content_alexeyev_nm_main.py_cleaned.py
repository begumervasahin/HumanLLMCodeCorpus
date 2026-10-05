import datetime
import logging
import numpy as np
import data_helpers
import model_all_stacked
logging.basicConfig(filename='all_results.log',
                    format='[%(asctime)s] [%(levelname)s] %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger("L")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
np.random.seed(123)
subset = None
save = False
model_name_path = 'params/model.json'
model_weights_path = 'params/model_weights.h5'
latent_dimension = 125
maxlen = 25
batch_size = 80
test_batch_size = 20
nb_epochs = 10
logger.info('Loading data...')
(x_train, y_train), (x_test, y_test) = data_helpers.load_relations()
vocab, reverse_vocab, vocab_size, check = data_helpers.create_vocab_set()
logger.info('Building the model...')
model = model_all_stacked.construct_model(maxlen, vocab_size * 3, vocab_size, latent_dimension)
logger.info('Fitting the model...')
initial_time = datetime.datetime.now()
for epoch in range(nb_epochs):
    x_train_data, y_train_data = x_train, y_train
    x_test_data, y_test_data = x_test, y_test
    if subset:
        training_batches = data_helpers.mini_batch_generator(x_train_data[:subset], y_train_data[:subset],
                                                             vocab, vocab_size, check, maxlen,
                                                             batch_size=batch_size)
    else:
        training_batches = data_helpers.mini_batch_generator(x_train_data, y_train_data,
                                                             vocab, vocab_size, check, maxlen,
                                                             batch_size=batch_size)
    test_batches = data_helpers.mini_batch_generator(x_test_data, y_test_data, vocab,
                                                     vocab_size, check, maxlen,
                                                     batch_size=test_batch_size)
    train_loss = 0.0
    train_steps = 1
    start_time = datetime.datetime.now()
    logger.info('-------- Epoch {} --------'.format(epoch))
    for x_train_batch, y_train_batch, _, _ in training_batches:
        train_loss += model.train_on_batch(x_train_batch, y_train_batch)
        train_loss_avg = train_loss / train_steps
        if train_steps % 10 == 0:
            logger.info('- TRAINING Step {} \t Loss {}'.format(train_steps, train_loss_avg))
        train_steps += 1
    test_loss = 0.0
    test_steps = 0
    logger.info(" -- TESTING NOW -- ")
    for x_test_batch, y_test_batch, x_text, y_text in test_batches:
        test_loss += model.test_on_batch(x_test_batch, y_test_batch)
        test_loss_avg = test_loss / test_steps
        test_steps += 1
        logger.info('- TESTING Step {}\t Loss {}'.format(test_steps, test_loss_avg))
        predicted_sequence = model.predict(np.array([x_test_batch[0]]))
        logger.info('Shapes x {} y_true {} y_pred {}'.format(x_test_batch[0].shape,
                                                              y_test_batch[0].shape,
                                                              predicted_sequence[0].shape))
        logger.info(u'Input:       \t[' + "|".join(map(lambda x: x[:maxlen], list(x_text[0]))) + "] -> ? ")
        logger.info(u'Expected:    \t[' + y_text[0] + "]")
        logger.info(u'Predicted: \t[' + data_helpers.decode_data(predicted_sequence, reverse_vocab) + "]")
        logger.info('----------------------------------------------------------------')
    stop_time = datetime.datetime.now()
    epoch_elapsed_time = stop_time - start_time
    total_elapsed_time = stop_time - initial_time
    logger.info('Epoch {}. Loss: {}\nEpoch time: {}. Total time: {}\n'.format(epoch, test_loss, epoch_elapsed_time,
                                                                                total_elapsed_time))