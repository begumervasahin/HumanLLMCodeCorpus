import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras import optimizers
import matplotlib.pyplot as plt
def load_data(filename, skip_rows=1):
    print(f'Reading data from {filename}')
    data = np.loadtxt(filename, skiprows=skip_rows)
    return data
data = load_data('training_data.txt')
y_train = data[:, 0]
x_train = data[:, 1:]
test_data = load_data('test_data.txt')
x_test = x_train[-1000:]
y_test = y_train[-1000:]
x_train = x_train[:-1000]
y_train = y_train[:-1000]
val_err = []
train_err = []
drop = []
def build_model(dropout_rate, input_dim):
    model = Sequential([
        Dense(1000, activation='relu', input_dim=input_dim),
        Dropout(dropout_rate),
        Dense(800, activation='relu'),
        Dropout(dropout_rate),
        Dense(200, activation='relu'),
        Dropout(dropout_rate),
        Dense(1, activation='sigmoid')
    ])
    sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
    return model
dropout_rates = np.arange(0, 1, 0.1)
for dropout_rate in dropout_rates:
    model = build_model(dropout_rate, input_dim=x_train.shape[1])
    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=20, batch_size=128)
    val_score = model.evaluate(x_test, y_test, batch_size=128)
    train_score = model.evaluate(x_train, y_train, batch_size=128)
    print(f'Dropout: {dropout_rate}, Validation accuracy: {val_score[1]}')
    val_err.append(val_score[1])
    train_err.append(train_score[1])
    drop.append(dropout_rate)
plt.plot(drop, val_err, label='Testing Error')
plt.plot(drop, train_err, label='Training Error')
plt.xlabel('Dropout percentage')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('neural_net_dropout.png')
best_val_accuracy = val_err[np.argmax(val_err)]
best_dropout = drop[np.argmax(val_err)]
print(f'Test accuracy = {best_val_accuracy} maximized at dropout percentage = {best_dropout}')
preds = model.predict_classes(test_data)
print('Writing predictions')
with open('neural_net_pred.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for it, pred in enumerate(preds, start=1):
        f.write(f'{it},{int(pred[0])}\n')