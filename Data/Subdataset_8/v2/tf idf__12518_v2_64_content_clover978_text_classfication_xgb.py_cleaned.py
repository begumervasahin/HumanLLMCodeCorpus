import xgboost as xgb
from sklearn.metrics import classification_report, confusion_matrix
train_data_path = '/home/dxx/Backup/STUDY/syd/data/train.txt'
test_data_path = '/home/dxx/Backup/STUDY/syd/data/test.txt'
dtrain = xgb.DMatrix(train_data_path)
dtest = xgb.DMatrix(test_data_path)
xgb_params = {
    'silent': 0,
    'max_depth': 10,
    'eta': 0.1,
    'subsample': 1.0,
    'min_child_weight': 5,
    'colsample_bytree': 0.2,
    'objective': 'multi:softmax',
    'num_class': 6
}
num_round = 100
evals = [(dtrain, 'train')]
def train_model():
    model = xgb.train(xgb_params, dtrain, num_round, evals=evals)
    model.save_model('xtrain.model')
def test_model():
    model = xgb.Booster()
    model.load_model('xtrain.model')
    preds = model.predict(dtest)
    labels = dtest.get_label()
    with open('result.txt', 'w') as f:
        for true_label, pred_label in zip(labels, preds):
            f.write('True Label: {:d}\tPredicted Label: {:d}\n'.format(int(true_label), int(pred_label)))
    print("Classification Report:")
    print(classification_report(labels, preds))
    print("Confusion Matrix:")
    print(confusion_matrix(labels, preds))
def main():
    train_model()
    test_model()
if __name__ == '__main__':
    main()