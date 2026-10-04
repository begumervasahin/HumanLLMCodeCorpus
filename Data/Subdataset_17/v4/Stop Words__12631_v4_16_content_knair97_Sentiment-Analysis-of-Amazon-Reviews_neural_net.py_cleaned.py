import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras import optimizers
import matplotlib.pyplot as plt
print('Reading training data')
data = np.loadtxt('training_data.txt', skiprows=1)
y_train = data[:, 0]
x_train = data[:, 1:]
print('Reading testing data')
test = np.loadtxt('test_data.txt', skiprows=1)
x_test = x_train[-1000:]
y_test = y_train[-1000:]
x_train = x_train[:-1000]
y_train = y_train[:-1000]
val_err = []
train_err = []
drop = []
for i in np.arange(0, 1, 0.1):
    model = Sequential()
    model.add(Dense(1000, activation='relu', input_dim=x_train.shape[1]))
    model.add(Dropout(i))
    model.add(Dense(800, activation='relu'))
    model.add(Dropout(i))
    model.add(Dense(200, activation='relu'))
    model.add(Dropout(i))
    model.add(Dense(1, activation='sigmoid'))
    sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=20, batch_size=128)
    score = model.evaluate(x_test, y_test, batch_size=128)
    score_train = model.evaluate(x_train, y_train, batch_size=128)
    print('Dropout:', i, 'Validation accuracy:', score[1])
    val_err.append(score[1])
    train_err.append(score_train[1])
    drop.append(i)
plt.plot(drop, val_err, label='Testing Error')
plt.plot(drop, train_err, label='Training Error')
plt.xlabel('Dropout percentage')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('neural_net_dropout.png')
best_val_accuracy = val_err[np.argmax(val_err)]
best_dropout = drop[np.argmax(val_err)]
print(f'Test accuracy = {best_val_accuracy} maximized at dropout percentage = {best_dropout}')
preds = model.predict_classes(test)
print('Writing predictions')
with open('neural_net_pred.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for it, pred in enumerate(preds, start=1):
        f.write(f'{it},{int(pred[0])}\n')