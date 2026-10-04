import datetime
import logging
import numpy as np
import data_helpers
import model_all_stacked
def configure_logging():
    logging.basicConfig(filename='all_results.log',
                        format='[%(asctime)s] [%(levelname)s] %(message)s',
                        level=logging.DEBUG)
    logger = logging.getLogger("MorphologyRNN")
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
def load_data():
    logger.info('Loading data...')
    (x_train, y_train), (x_test, y_test) = data_helpers.load_relations()
    vocab, reverse_vocab, vocab_size, check = data_helpers.create_vocab_set()
    return (x_train, y_train), (x_test, y_test), vocab, reverse_vocab, vocab_size, check
def build_model(max_sequence_length, vocab_size, latent_dimension):
    logger.info('Building model...')
    return model_all_stacked.construct_model(max_sequence_length, vocab_size * 3, vocab_size, latent_dimension)
def train_model(model, x_train, y_train, x_test, y_test, vocab, vocab_size, check, max_sequence_length, batch_size, test_batch_size, num_epochs, subset=None):
    initial_time = datetime.datetime.now()
    for epoch in range(num_epochs):
        train_batches = data_helpers.mini_batch_generator(
            x_train[:subset] if subset else x_train,
            y_train[:subset] if subset else y_train,
            vocab, vocab_size, check, max_sequence_length, batch_size)
        test_batches = data_helpers.mini_batch_generator(
            x_test, y_test, vocab, vocab_size, check, max_sequence_length, batch_size=test_batch_size)
        total_loss = 0.0
        step = 1
        start_time = datetime.datetime.now()
        logger.info(f'-------- Epoch {epoch} --------')
        for x_train_batch, y_train_batch, x_train_text, y_train_text in train_batches:
            batch_loss = model.train_on_batch(x_train_batch, y_train_batch)
            total_loss += batch_loss
            avg_loss = total_loss / step
            if step % 10 == 0:
                logger.info(f'- TRAINING step {step} \t loss {avg_loss}')
            step += 1
        evaluate_model(model, test_batches, vocab, reverse_vocab, max_sequence_length)
        log_epoch_time(epoch, start_time, initial_time)
def evaluate_model(model, test_batches, vocab, reverse_vocab, max_sequence_length):
    test_loss = 0.0
    test_step = 0
    logger.info(" -- TESTING NOW -- ")
    for x_test_batch, y_test_batch, x_test_text, y_test_text in test_batches:
        batch_test_loss = model.test_on_batch(x_test_batch, y_test_batch)
        test_loss += batch_test_loss
        avg_test_loss = test_loss / test_step if test_step != 0 else 0
        test_step += 1
        logger.info(f'- TESTING step {test_step} \t loss {avg_test_loss}')
        predicted_sequence = model.predict(np.array([x_test_batch[0]]))
        log_prediction(x_test_batch[0], y_test_batch[0], predicted_sequence[0], x_test_text[0], y_test_text[0], reverse_vocab, max_sequence_length)
def log_prediction(x_test, y_true, y_pred, x_text, y_text, reverse_vocab, max_sequence_length):
    logger.info(f'Shapes x {x_test.shape} y_true {y_true.shape} y_pred {y_pred.shape}')
    logger.info(f'Input:       \t[{ "|".join(map(lambda x: x[:max_sequence_length], list(x_text))) }] -> ?')
    logger.info(f'Expected:    \t[{ y_text }]')
    logger.info(f'Predicted: \t[{ data_helpers.decode_data(y_pred, reverse_vocab) }]')
    logger.info('----------------------------------------------------------------')
def log_epoch_time(epoch, start_time, initial_time):
    end_time = datetime.datetime.now()
    epoch_elapsed = end_time - start_time
    total_elapsed = end_time - initial_time
    logger.info(f'Epoch {epoch}. Loss: {test_loss}\nEpoch time: {epoch_elapsed}. Total time: {total_elapsed}\n')
if __name__ == "__main__":
    subset = None
    save_model = False
    model_name_path = 'params/model.json'
    model_weights_path = 'params/model_weights.h5'
    latent_dimension = 125
    max_sequence_length = 25
    batch_size = 80
    test_batch_size = 20
    num_epochs = 10
    logger = configure_logging()
    np.random.seed(123)
    (x_train, y_train), (x_test, y_test), vocab, reverse_vocab, vocab_size, check = load_data()
    model = build_model(max_sequence_length, vocab_size, latent_dimension)
    train_model(model, x_train, y_train, x_test, y_test, vocab, vocab_size, check, max_sequence_length, batch_size, test_batch_size, num_epochs, subset)