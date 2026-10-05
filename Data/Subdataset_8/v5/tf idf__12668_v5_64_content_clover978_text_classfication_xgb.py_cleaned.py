import xgboost as xgb
from sklearn.metrics import classification_report, confusion_matrix
TRAIN_DATA_PATH = '/home/dxx/Backup/STUDY/syd/data/train.txt'
TEST_DATA_PATH = '/home/dxx/Backup/STUDY/syd/data/test.txt'
XGB_PARAMETERS = {
    'silent': 0,
    'max_depth': 10,
    'eta': 0.1,
    'subsample': 1.0,
    'min_child_weight': 5,
    'col_sample_bytree': 0.2,
    'objective': 'multi:softmax',
    'num_class': 6
}
NUM_ROUNDS = 100
def train_model(train_data_path, parameters, num_rounds):
    dtrain = xgb.DMatrix(train_data_path)
    watchlist = [(dtrain, 'train')]
    model = xgb.train(parameters, dtrain, num_rounds, evals=watchlist)
    model.save_model('xtrain.model')
def test_model(test_data_path):
    dtest = xgb.DMatrix(test_data_path)
    model = xgb.Booster()
    model.load_model('xtrain.model')
    predictions = model.predict(dtest)
    true_labels = dtest.get_label()
    with open('result.txt', 'w') as f:
        for true_label, prediction in zip(true_labels, predictions):
            f.write(f'True label: {int(true_label)}\tPredicted label: {int(prediction)}\n')
    print(classification_report(true_labels, predictions))
    print(confusion_matrix(true_labels, predictions))
def main():
    train_model(TRAIN_DATA_PATH, XGB_PARAMETERS, NUM_ROUNDS)
    test_model(TEST_DATA_PATH)
if __name__ == '__main__':
    main()