import datetime
import logging
import numpy as np
import data_helpers
import model_all_stacked
def setup_logging():
    logging.basicConfig(
        filename='all_results.log',
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        level=logging.DEBUG
    )
    logger = logging.getLogger("ModelTrainingLogger")
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
def load_data():
    logger.info('Loading data...')
    (x_train, y_train), (x_test, y_test) = data_helpers.load_relations()
    vocab, reverse_vocab, vocab_size, check = data_helpers.create_vocab_set()
    return (x_train, y_train), (x_test, y_test), vocab, reverse_vocab, vocab_size, check
def build_model(maxlen, vocab_size, latent_dimension):
    logger.info('Building model...')
    return model_all_stacked.construct_model(maxlen, vocab_size * 3, vocab_size, latent_dimension)
def log_predictions(x_test_batch, y_test_batch, x_text, y_text, predicted_seq):
    logger.info(
        'Shapes x {} y_true {} y_pred {}'.format(
            x_test_batch[0].shape,
            y_test_batch[0].shape,
            predicted_seq[0].shape
        )
    )
    logger.info(
        u'Input:       \t[' + "|".join(map(lambda x: x[:maxlen], list(x_text[0]))) + "] -> ? "
    )
    logger.info(u'Expected:    \t[' + y_text[0] + "]")
    logger.info(
        u'Predicted: \t[' + data_helpers.decode_data(predicted_seq, reverse_vocab) + "]"
    )
    logger.info('----------------------------------------------------------------')
def evaluate_model(test_batches, start_time, initial_time):
    total_test_loss = 0.0
    test_step = 0
    logger.info(" -- Testing Now -- ")
    for x_test_batch, y_test_batch, x_text, y_text in test_batches:
        test_loss = model.test_on_batch(x_test_batch, y_test_batch)
        total_test_loss += test_loss
        avg_test_loss = total_test_loss / (test_step + 1)
        test_step += 1
        logger.info('- Testing step {} \t loss {}'.format(test_step, avg_test_loss))
        predicted_seq = model.predict(np.array([x_test_batch[0]]))
        log_predictions(x_test_batch, y_test_batch, x_text, y_text, predicted_seq)
    stop_time = datetime.datetime.now()
    epoch_elapsed_time = stop_time - start_time
    total_elapsed_time = stop_time - initial_time
    logger.info(
        'Epoch {}. Loss: {}\nEpoch time: {}. Total time: {}\n'.format(
            epoch, avg_test_loss, epoch_elapsed_time, total_elapsed_time
        )
    )
def train_and_evaluate_model(x_train, y_train, x_test, y_test, vocab, vocab_size, check, maxlen, batch_size, test_batch_size, nb_epoch):
    initial_time = datetime.datetime.now()
    for epoch in range(nb_epoch):
        batches = data_helpers.mini_batch_generator(
            x_train, y_train, vocab, vocab_size, check, maxlen, batch_size=batch_size
        )
        test_batches = data_helpers.mini_batch_generator(
            x_test, y_test, vocab, vocab_size, check, maxlen, batch_size=test_batch_size
        )
        total_loss = 0.0
        step = 1
        start_time = datetime.datetime.now()
        logger.info('-------- Epoch {} --------'.format(epoch))
        for x_train_batch, y_train_batch, x_text_train, y_text_train in batches:
            batch_loss = model.train_on_batch(x_train_batch, y_train_batch)
            total_loss += batch_loss
            avg_loss = total_loss / step
            if step % 10 == 0:
                logger.info('- Training step {} \t loss {}'.format(step, avg_loss))
            step += 1
        evaluate_model(test_batches, start_time, initial_time)
if __name__ == "__main__":
    logger = setup_logging()
    np.random.seed(123)
    subset = None
    save = False
    model_name_path = 'params/model.json'
    model_weights_path = 'params/model_weights.h5'
    latent_dimension = 125
    maxlen = 25
    batch_size = 80
    test_batch_size = 20
    nb_epoch = 10
    (x_train, y_train), (x_test, y_test), vocab, reverse_vocab, vocab_size, check = load_data()
    model = build_model(maxlen, vocab_size, latent_dimension)
    train_and_evaluate_model(x_train, y_train, x_test, y_test, vocab, vocab_size, check, maxlen, batch_size, test_batch_size, nb_epoch)