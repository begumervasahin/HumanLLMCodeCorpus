
import xgboost as xgb
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix
train_data_path = '/home/dxx/Backup/STUDY/syd/data/train.txt'
test_data_path = '/home/dxx/Backup/STUDY/syd/data/test.txt'
parameters = {
    'silent': 0,
    'max_depth': 10,
    'eta': 0.1,
    'subsample': 1.0,
    'min_child_weight': 5,
    'col_sample_bytree': 0.2,
    'objective': 'multi:softmax',
    'num_class': 6
}
num_rounds = 100
watchlist = [(dtrain, 'train')]
def train_model():
    dtrain = xgb.DMatrix(train_data_path)
    model = xgb.train(parameters, dtrain, num_rounds, evals=watchlist)
    model.save_model('xtrain.model')
def test_model():
    dtest = xgb.DMatrix(test_data_path)
    model = xgb.Booster()
    model.load_model('xtrain.model')
    predictions = model.predict(dtest)
    true_labels = dtest.get_label()
    with open('result.txt', 'w') as f:
        for true_label, prediction in zip(true_labels, predictions):
            f.write('True label: {:d}\tPredicted label: {:d}\n'.format(int(true_label), int(prediction)))
    print(classification_report(true_labels, predictions))
    print(confusion_matrix(true_labels, predictions))
def main():
    train_model()
    test_model()
if __name__ == '__main__':
    main()