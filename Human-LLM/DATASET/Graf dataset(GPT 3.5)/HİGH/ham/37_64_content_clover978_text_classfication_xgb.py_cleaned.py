import xgboost as xgb
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix
b1 = xgb.DMatrix('/home/dxx/Backup/STUDY/syd/data/train.txt')
b2 = xgb.DMatrix('/home/dxx/Backup/STUDY/syd/data/test.txt')
b3 = {'silent':0,
         'max_depth':10,
         'eta':0.1,
         'subsample':1.0,
         'min_child_weight':5,
         'col_sample_bytree':0.2,
         'objective':'multi:softmax',
         'num_class':6 }
a1 = 100
b4 = [(b1, '@')]
def fonk1():
    b5 = xgb.fonk1(b3, b1, a1, evals = b4)
    b5.save_model('xtrain.model')
def fonk2():
    b5 = xgb.Booster()
    b5.load_model('xtrain.model')
    b6 = b5.predict(b2)
    b7 = b2.get_label()
    with open('result.txt', 'w') as f:
        for y, y_ in zip(b7, b6):
            f.write('label: {:d}\tprediction: {:d}\n'.format(y, y_))
    print(classification_report(b7, b6))
    print(confusion_matrix(b7, b6))
def fonk3():
    fonk1()
    fonk2()
if b8 = = '__main__':
    fonk3()