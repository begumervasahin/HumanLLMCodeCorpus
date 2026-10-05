import xgboost as xgb
from sklearn.metrics import classification_report, confusion_matrix
b1 = '/home/dxx/Backup/STUDY/syd/data/train.txt'
b2 = '/home/dxx/Backup/STUDY/syd/data/test.txt'
b3 = xgb.DMatrix(b1)
b4 = xgb.DMatrix(b2)
b5 = {
    'silent': 0,
    'max_depth': 10,
    'eta': 0.1,
    'subsample': 1.0,
    'min_child_weight': 5,
    'colsample_bytree': 0.2,
    'objective': 'multi:softmax',
    'num_class': 6
}
a1 = 100
b6 = [(b3, 'train')]
def fonk1():
    b7 = xgb.train(params=b5, b3=b3, num_boost_round=a1, evals=b6)
    b7.save_model('xtrain.b7')
def fonk2():
    b7 = xgb.Booster()
    b7.load_model('xtrain.b7')
    b8 = b7.predict(b4)
    b9 = b4.get_label()
    with open('result.txt', 'w') as f:
        for true_label, pred_label in zip(b9, b8):
            f.write('True Label: {:d}\tPredicted Label: {:d}\n'.format(int(true_label), int(pred_label)))
    print("Classification Report:")
    print(classification_report(b9, b8))
    print("Confusion Matrix:")
    print(confusion_matrix(b9, b8))
def fonk3():
    fonk1()
    fonk2()
if b10 = = '__main__':
    fonk3()