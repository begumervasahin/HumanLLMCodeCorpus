import datetime
import logging
import numpy as np
import data_helpers
import model_all_stacked
logging.basicConfig(filename='all_results.log',
                    format='[%(asctime)s] [%(levelname)s] %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger("L")
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
def load_data():
    logger.info('Loading data...')
    return data_helpers.load_relations()
def build_model():
    logger.info('Building the model...')
    vocab, _, vocab_size, check = data_helpers.create_vocab_set()
    return model_all_stacked.construct_model(maxlen, vocab_size * 3, vocab_size, latent_dimension), vocab
def generate_batches(data, vocab, vocab_size, check, batch_size):
    return data_helpers.mini_batch_generator(data[0], data[1], vocab, vocab_size, check, maxlen, batch_size=batch_size)
def train(model, training_batches):
    logger.info('Fitting the model...')
    initial_time = datetime.datetime.now()
    for epoch in range(nb_epochs):
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
        test_loss = test(model)
        stop_time = datetime.datetime.now()
        epoch_elapsed_time = stop_time - start_time
        total_elapsed_time = stop_time - initial_time
        logger.info('Epoch {}. Loss: {}\nEpoch time: {}. Total time: {}\n'.format(epoch, test_loss,
                                                                                    epoch_elapsed_time,
                                                                                    total_elapsed_time))
def test(model):
    test_loss = 0.0
    test_steps = 0
    logger.info(" -- TESTING NOW -- ")
    test_batches = generate_batches((x_test, y_test), vocab, vocab_size, check, batch_size=test_batch_size)
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
    return test_loss
if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = load_data()
    model, vocab = build_model()
    training_batches = generate_batches((x_train, y_train), vocab, vocab_size, check, batch_size=batch_size)
    train(model, training_batches)