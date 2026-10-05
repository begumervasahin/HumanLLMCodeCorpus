
import xgboost as xgb
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix
b1 = '/home/dxx/Backup/STUDY/syd/data/train.txt'
b2 = '/home/dxx/Backup/STUDY/syd/data/test.txt'
b3 = {
    'silent': 0,
    'max_depth': 10,
    'eta': 0.1,
    'subsample': 1.0,
    'min_child_weight': 5,
    'col_sample_bytree': 0.2,
    'objective': 'multi:softmax',
    'num_class': 6
}
a1 = 100
b4 = [(b5, 'train')]
def fonk1():
    b5 = xgb.DMatrix(b1)
    b6 = xgb.train(b3, b5, a1, evals=b4)
    b6.save_model('xtrain.b6')
def fonk2():
    b7 = xgb.DMatrix(b2)
    b6 = xgb.Booster()
    b6.load_model('xtrain.b6')
    b8 = b6.predict(b7)
    b9 = b7.get_label()
    with open('result.txt', 'w') as f:
        for true_label, prediction in zip(b9, b8):
            f.write('True label: {:d}\tPredicted label: {:d}\n'.format(int(true_label), int(prediction)))
    print(classification_report(b9, b8))
    print(confusion_matrix(b9, b8))
def fonk3():
    fonk1()
    fonk2()
if b10 = = '__main__':
    fonk3()